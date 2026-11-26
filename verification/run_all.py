"""Reproduce the finite decoder checks using only the Python standard library."""

from fractions import Fraction
from itertools import product
from math import atan2, cos, fsum, hypot, isclose, prod, sin, sqrt

EVEN = (0, 3)
ODD = (1, 2)
INV_SQRT_2 = 1 / sqrt(2)


def require_close(actual, expected, context):
    if not isclose(actual, expected, rel_tol=2e-12, abs_tol=5e-14):
        raise AssertionError(f"{context}: expected {expected!r}, got {actual!r}")


def flag(bit, overlap):
    """Return a real qubit flag with the declared overlap convention."""
    phase = -1 if bit else 1
    return sqrt((1 + overlap) / 2), phase * sqrt((1 - overlap) / 2)


def dot(left, right):
    return fsum(a * b for a, b in zip(left, right, strict=True))


def tensor(left, right):
    return tuple(a * b for a, b in product(left, right))


def fusion_kraus(left_overlap, right_overlap):
    """Return (weight, even input, odd input, nonzero Kraus coefficients)."""
    amps = tensor(flag(0, left_overlap), flag(0, right_overlap))
    even_prob = fsum(amps[z] ** 2 for z in EVEN)
    odd_prob = fsum(amps[z] ** 2 for z in ODD)
    even_first = amps[EVEN[0]] ** 2 / even_prob
    odd_first = amps[ODD[0]] ** 2 / odd_prob
    even_second = amps[EVEN[1]] ** 2 / even_prob
    odd_second = amps[ODD[1]] ** 2 / odd_prob

    # A coupling of two Bernoulli laws with at most three nonzero outcomes.
    # Compute the imbalance from the smaller probabilities when both
    # first coordinates are near one.
    if min(even_first, odd_first) > 0.5:
        imbalance = odd_second - even_second
    else:
        imbalance = even_first - odd_first
    weights = (
        (min(even_first, odd_first), max(imbalance, 0)),
        (max(-imbalance, 0), min(even_second, odd_second)),
    )
    operators = []
    for i, u in enumerate(EVEN):
        for j, v in enumerate(ODD):
            weight = weights[i][j]
            if weight > 0:
                operators.append(
                    (weight, u, v, sqrt(weight * even_prob) / amps[u],
                     sqrt(weight * odd_prob) / amps[v])
                )
    return operators


def apply_fusion(operator, amplitude):
    """Return the branch probability and normalized two-component output."""
    _, u, v, coeff_0, coeff_1 = operator
    output = coeff_0 * amplitude[u], coeff_1 * amplitude[v]
    probability = dot(output, output)
    return probability, tuple(value / sqrt(probability) for value in output)


def check_fusion():
    overlaps = (0.01, 0.25, 0.55, 0.99, 0.9999)
    for left_overlap, right_overlap in product(overlaps, repeat=2):
        operators = fusion_kraus(left_overlap, right_overlap)
        if not 2 <= len(operators) <= 3:
            raise AssertionError("the sparse coupling needs at most three Kraus operators")
        diagonal = [0.0] * 4
        for _, u, v, coeff_0, coeff_1 in operators:
            # The other entries of K†K vanish because the two images
            # are in orthogonal output basis directions.
            diagonal[u] += coeff_0 ** 2
            diagonal[v] += coeff_1 ** 2
        for entry in diagonal:
            require_close(entry, 1.0, "Kraus completeness")

        for left_bit, right_bit in product((0, 1), repeat=2):
            inputs = tensor(flag(left_bit, left_overlap), flag(right_bit, right_overlap))
            for operator in operators:
                weight, u, v, _, _ = operator
                probability, output = apply_fusion(operator, inputs)
                require_close(probability, weight, "label-independent branch probability")
                chosen_bit = left_bit if u ^ v == 2 else right_bit
                expected = flag(chosen_bit, left_overlap * right_overlap)
                require_close(abs(dot(output, expected)), 1.0, "output ray")
                require_close(output[1] / output[0], expected[1] / expected[0], "output sign")
    print(f"Fusion obeys completeness, phase, and probability checks for {len(overlaps) ** 2} overlap pairs.")


def pure_error(a, b, overlap):
    """Unnormalized binary Bayes error of two pure states."""
    if not a or not b:
        return 0.0
    overlap_squared = min(1.0, overlap ** 2)
    trace_norm = sqrt((a - b) ** 2 + 4 * a * b * (1 - overlap_squared))
    return 2 * a * b * overlap_squared / (a + b + trace_norm)


def syndrome_pairs(n):
    """Enumerate pairs of error strings with the same repetition syndrome."""
    for suffix in product((0, 1), repeat=n - 1):
        left = (0, *suffix)
        yield left, tuple(1 - bit for bit in left)


def iid_priors(n, p):
    return {x: p ** sum(x) * (1 - p) ** (n - sum(x)) for x in product((0, 1), repeat=n)}


def product_flag(x, overlaps):
    state = (1.0,)
    for bit, overlap in zip(x, overlaps, strict=True):
        state = tensor(state, flag(bit, overlap))
    return state


def full_error(overlaps, priors):
    """Compute the full-record risk from explicit product-state amplitudes."""
    terms = []
    for left, right in syndrome_pairs(len(overlaps)):
        overlap = dot(product_flag(left, overlaps), product_flag(right, overlaps))
        terms.append(pure_error(priors[left], priors[right], overlap))
    return fsum(terms)


def streamed_pair(left, right, overlaps):
    """Enumerate both hypotheses through the same explicit fusion tree."""
    prior_overlap = overlaps[0]
    branches = [(1.0, 1.0, flag(left[0], prior_overlap), flag(right[0], prior_overlap), 0)]
    for i, overlap in enumerate(overlaps[1:], start=1):
        operators = fusion_kraus(prior_overlap, overlap)
        new_branches = []
        left_flag, right_flag = flag(left[i], overlap), flag(right[i], overlap)
        for p_left, p_right, state_left, state_right, j in branches:
            inputs_left, inputs_right = tensor(state_left, left_flag), tensor(state_right, right_flag)
            for operator in operators:
                _, u, v, _, _ = operator
                q_left, out_left = apply_fusion(operator, inputs_left)
                q_right, out_right = apply_fusion(operator, inputs_right)
                selected = j if u ^ v == 2 else i
                new_branches.append((p_left * q_left, p_right * q_right, out_left, out_right, selected))
        prior_overlap *= overlap
        branches = new_branches
    return branches


def x_readout(state):
    return ((state[0] + state[1]) ** 2 / 2, (state[0] - state[1]) ** 2 / 2)


def streamed_error(overlaps, priors, *, measure_early=False):
    terms = []
    for left, right in syndrome_pairs(len(overlaps)):
        branches = streamed_pair(left, right, overlaps)
        require_close(fsum(branch[0] for branch in branches), 1, "left branch normalization")
        require_close(fsum(branch[1] for branch in branches), 1, "right branch normalization")
        for p_left, p_right, out_left, out_right, selected in branches:
            require_close(p_left, p_right, "common branch probability")
            require_close(abs(dot(out_left, flag(left[selected], prod(overlaps)))), 1, "left retained index")
            require_close(abs(dot(out_right, flag(right[selected], prod(overlaps)))), 1, "right retained index")
            a, b = priors[left] * p_left, priors[right] * p_right
            if measure_early:
                left_prob, right_prob = x_readout(out_left), x_readout(out_right)
                terms.extend(min(a * u, b * v) for u, v in zip(left_prob, right_prob, strict=True))
            else:
                terms.append(pure_error(a, b, dot(out_left, out_right)))
    return fsum(terms)


def check_decoder():
    benchmark = (0.99,) * 4, iid_priors(4, 0.25)
    # Non-i.i.d. weights ensure that no product-prior identity is used by
    # the streaming check. One string has zero prior.
    custom_weights = {x: i * i + i % 3 for i, x in enumerate(product((0, 1), repeat=4))}
    total_weight = sum(custom_weights.values())
    custom_priors = {x: weight / total_weight for x, weight in custom_weights.items()}
    require_close(fsum(custom_priors.values()), 1, "correlated prior normalization")
    examples = (
        ((0.77,), iid_priors(1, 0.37)),
        ((0.15, 0.49), iid_priors(2, 0.0)),
        ((0.2, 0.55, 0.95, 0.3), custom_priors),
        ((0.87, 0.99, 0.25, 0.62, 0.91), iid_priors(5, 0.15)),
        benchmark,
    )
    for overlaps, priors in examples:
        require_close(streamed_error(overlaps, priors), full_error(overlaps, priors), "optimal risk")

    # Early X readout of the compressed state suffices for pairwise balanced priors.
    overlaps = (0.15, 0.55, 0.92)
    weights = (0.07, 0.10, 0.11, 0.22)
    pairwise_balanced = {
        x: weight
        for pair, weight in zip(syndrome_pairs(len(overlaps)), weights, strict=True)
        for x in pair
    }
    require_close(
        streamed_error(overlaps, pairwise_balanced, measure_early=True),
        full_error(overlaps, pairwise_balanced),
        "balanced prior early readout",
    )
    print(f"Streamed and full-record optimal risk agree on {len(examples)} models and the balanced early-readout case.")
    return full_error(*benchmark), streamed_error(*benchmark, measure_early=True)


def parity_basis(x, c):
    """Return the normalized even and odd components of a product flag."""
    state = product_flag(x, (c,) * len(x))
    components = []
    for parity in range(2):
        part = tuple(a if i.bit_count() % 2 == parity else 0.0 for i, a in enumerate(state))
        norm = sqrt(dot(part, part))
        components.append(tuple(a / norm for a in part))
    return components


def helstrom_axis(x, a, b, c):
    even, odd = parity_basis(x, c)
    overlap = c ** len(x)
    angle = atan2((a + b) * sqrt(1 - overlap ** 2), (a - b) * overlap) / 2
    return (
        tuple(cos(angle) * e + sin(angle) * o for e, o in zip(even, odd, strict=True)),
        tuple(-sin(angle) * e + cos(angle) * o for e, o in zip(even, odd, strict=True)),
    )


def abs_cross_gram_norm(left_basis, right_basis):
    row_0, row_1 = [
        tuple(abs(dot(left, right)) for right in right_basis)
        for left in left_basis
    ]
    diag_0, diag_1 = dot(row_0, row_0), dot(row_1, row_1)
    off_diag = dot(row_0, row_1)
    return sqrt((diag_0 + diag_1 + hypot(diag_0 - diag_1, 2 * off_diag)) / 2)


def check_early_certificate():
    c = Fraction(99, 100)
    p = Fraction(1, 4)
    r = (0, 0, 0, 1)
    t = (0, 0, 1, 1)
    a, b, w = p * (1 - p) ** 3, p ** 3 * (1 - p), p ** 2 * (1 - p) ** 2
    overlap = c ** 4
    transverse_squared = 1 - overlap ** 2

    # Apply the entrywise absolute cross-Gram matrix to (1,1)/sqrt(2).
    # Its norm is at least cos(theta) sqrt(e^2+o^2). Check rational bounds
    # on e, o and cos(theta)^2, leaving square roots out of the certificate.
    even_overlap = (c + c ** 3) / (1 + c ** 4)
    odd_overlap = c / (1 + c ** 2)
    parallel_squared = ((a - b) * overlap) ** 2
    rotation_denominator_squared = parallel_squared + (a + b) ** 2 * transverse_squared
    e_min = Fraction(9995, 10000)
    o_min = Fraction(4995, 10000)
    g_min = Fraction(11, 10)
    if not (
        even_overlap > e_min
        and odd_overlap > o_min
        and parallel_squared > Fraction(94, 100) ** 2 * rotation_denominator_squared
        and Fraction(97, 100) * (e_min ** 2 + o_min ** 2) > g_min ** 2
    ):
        raise AssertionError("exact cross-Gram lower bound")

    # The smaller eigenvalue magnitude exceeds h exactly when
    # ab(1-c^(2n)) > h(|a-b|+h).
    h = Fraction(1, 1000)
    if not (a * b * transverse_squared > h * (abs(a - b) + h)
            and w * w * transverse_squared > h * h):
        raise AssertionError("exact positive eigenvalue-magnitude bound")
    rational_gap = h * (g_min - 1) ** 2 / 4

    # Independent floating-point computation from the actual flag amplitudes.
    norm = abs_cross_gram_norm(
        helstrom_axis(r, float(a), float(b), float(c)),
        helstrom_axis(t, float(w), float(w), float(c)),
    )
    require_close(norm, 1.101099216498264, "four-flag cross-Gram witness")
    eigen_r = 2 * a * b * transverse_squared / (sqrt((a - b) ** 2 + 4 * a * b * transverse_squared) + a - b)
    eigen_t = w * sqrt(transverse_squared)
    spectral_gap = min(eigen_r, eigen_t) * (norm - 1) ** 2 / 4
    if spectral_gap <= rational_gap:
        raise AssertionError("numerical spectral witness conflicts with the rational threshold")
    print(f"Four-flag absolute cross-Gram norm: {norm:.12f}")
    print(f"Early-readout excess risk is greater than {float(rational_gap):.7g} (exact rational certificate).")
    print(f"Spectral lower bound evaluated numerically: {spectral_gap:.8g}")
    return rational_gap


def phase_noise_error(overlaps, priors, q):
    """Risk of the compressed decoder after a final Pauli Z with probability q."""
    overlap = prod(overlaps)
    ideal = noisy = classical_bsc = no_readout = 0.0
    for left, right in syndrome_pairs(len(overlaps)):
        a, b = priors[left], priors[right]
        d = a - b
        ideal += pure_error(a, b, overlap)
        bloch_norm = hypot(d * overlap, (a + b) * (1 - 2 * q) * sqrt(1 - overlap ** 2))
        noisy += (a + b - max(abs(d), bloch_norm)) / 2
        classical_bsc += min(a * (1 - q), b * q) + min(a * q, b * (1 - q))
        no_readout += min(a, b)
    return ideal, noisy, classical_bsc, no_readout


def certify_phase_noise_threshold(certified_gap):
    """Check an exact upper bound on the tangent slope of the noisy risk."""
    p = Fraction(1, 4)
    overlap = Fraction(99, 100) ** 4
    slope_bound = Fraction(13, 100)
    multiplicities = (1, 4, 3)
    caps = tuple(Fraction(n, 10_000) for n in (254, 111, 196))
    for weight, cap in enumerate(caps):
        a = p ** weight * (1 - p) ** (4 - weight)
        b = p ** (4 - weight) * (1 - p) ** weight
        transverse_squared = (a + b) ** 2 * (1 - overlap ** 2)
        bloch_squared = ((a - b) * overlap) ** 2 + transverse_squared
        if transverse_squared ** 2 >= cap ** 2 * bloch_squared:
            raise AssertionError(f"phase-noise slope bound for weight class {weight}")
    threshold = Fraction(19, 1_000_000)
    total_cap = sum(count * cap for count, cap in zip(multiplicities, caps, strict=True))
    if total_cap >= slope_bound or threshold * slope_bound >= certified_gap:
        raise AssertionError("phase-noise increase must stay below the certified early gap")
    return float(threshold)


def check_phase_noise(certified_gap):
    threshold = certify_phase_noise_threshold(certified_gap)
    overlap = (0.99,) * 4
    priors = iid_priors(4, 0.25)
    previous = 0.0
    for q in (0.0, threshold, 0.01, 0.05, 0.1, 0.2, 0.49, 0.5):
        ideal, noisy, classical_bsc, no_readout = phase_noise_error(overlap, priors, q)
        if not max(previous, ideal, classical_bsc) - 5e-14 <= noisy <= ideal + classical_bsc + 5e-14:
            raise AssertionError(f"phase noise risk sandwich or monotonicity at q={q}: {noisy}")
        if q == 0:
            require_close(noisy, ideal, "no phase faults")
        if q == 0.5:
            require_close(noisy, no_readout, "complete dephasing")
        if q == threshold and not noisy < ideal + certified_gap:
            raise AssertionError("small phase-fault probability should preserve the certified gap")
        previous = noisy
    print(f"Final-accumulator phase flips retain the certified gap through q={threshold:.7g}.")


def main():
    check_fusion()
    ideal, feasible_early = check_decoder()
    print(f"Four-flag optimal logical error: {ideal:.12f}")
    certificate = check_early_certificate()
    if feasible_early <= ideal + certificate:
        raise AssertionError("the feasible early risk must exceed the lower certificate")
    print(f"Four-flag error of a feasible early policy: {feasible_early:.12f}")
    check_phase_noise(certificate)
    print("All verification checks passed.")


if __name__ == "__main__":
    main()
