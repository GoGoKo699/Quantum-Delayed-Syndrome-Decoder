# Project understanding map

This route contains **30 milestones**. The first 11 build the task and its mathematical vocabulary, starting with one physical error and ending with the timed decoding problem. The next 19 develop the fusion operation, compare it with early readout, then extend the model to imperfect storage and more general syndromes. This allocation reflects where the project needs its own arguments.

The single educational anchor is John Watrous's *The Theory of Quantum Information*. The [Watrous bridge](WATROUS_BRIDGE.md) links specific sections, translates the notation and works through a complete two-flag example. The linked scientific account gives the exact claims and proofs.

| Phase | Milestones | Connection established |
|---|---|---|
| Background and preliminaries | [M01](#m01-a-physical-bit-flip)–[M04](#m04-the-late-syndrome) | The data error, its syndrome and the remaining logical ambiguity |
| Background and preliminaries | [M05](#m05-a-single-quantum-flag)–[M08](#m08-an-instrument-retains-two-kinds-of-output) | Pure flag states, pattern probabilities and physical instruments |
| Background and preliminaries | [M09](#m09-the-optimal-binary-readout)–[M11](#m11-the-matched-decoding-problem) | From conditional discrimination to matched timing and memory budgets |
| Narrative and innovation | [M12](#m12-split-the-input-amplitudes-by-parity)–[M19](#m19-match-the-full-record-optimum) | The branch operator, streaming invariant and exact risk |
| Narrative and innovation | [M20](#m20-one-parent-measurement)–[M25](#m25-compare-reliability-rates-under-local-readout) | Finite comparison, balanced-prior case and per-flag rate |
| Narrative and innovation | [M26](#m26-a-phase-flip-in-storage)–[M30](#m30-the-complete-decoding-story) | Perturbations, linear syndromes and the complete scope |

## Phase I. Background and preliminaries

### M01 A physical bit flip

**Central question.** What happens to an unknown quantum data qubit when one physical bit flips?

**Understanding target.** Describe how a Pauli $X$ acts on one physical site of an encoded register. Associate each possible error event with a classical hidden bit while the data state can remain an arbitrary quantum superposition.

**Prerequisites.** None within this map.

**Conceptual connection.** Separate the input quantum information, which the decoder must protect, from the stochastic error bit, which the decoder tries to infer.

**Canonical sources.** [Model](../science/model.md) · [Watrous, §2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf).

### M02 Adjacent parity checks

**Central question.** What does a repetition-code check say about errors at adjacent sites?

**Understanding target.** Starting from the $+1$ eigenspace of $Z_iZ_{i+1}$, use Pauli anticommutation to obtain the parity $x_i\oplus x_{i+1}$ of the two physical flip bits. Use a chain of these check values to reconstruct a candidate pattern from one chosen bit.

**Prerequisites.** [M01](#m01-a-physical-bit-flip).

**Conceptual connection.** A check can learn a relative error bit without measuring the logical data in its computational basis.

**Canonical sources.** [Model](../science/model.md).

### M03 Complementary errors and logical failure

**Central question.** Why does one logical choice remain after reading all the adjacent checks?

**Understanding target.** Show that the two patterns in the syndrome class differ by the all-ones error. Applying the inverse of one candidate corrects the data if the guess is correct and applies a logical bit flip if the other candidate occurred.

**Prerequisites.** [M02](#m02-adjacent-parity-checks).

**Conceptual connection.** Reduce the decoder's logical failure rate to the probability of choosing the wrong member of a pair.

**Canonical sources.** [Model](../science/model.md).

### M04 The late syndrome

**Central question.** What changes when the syndrome arrives after all the flags?

**Understanding target.** List the information available during flag acquisition, at the point where the retained memory is counted, and at final readout. An acquisition rule may use earlier flag outcomes. Its input still excludes the late check values.

**Prerequisites.** [M03](#m03-complementary-errors-and-logical-failure).

**Conceptual connection.** Distinguish using side information to choose the quantum measurement from using it to interpret an existing classical record.

**Canonical sources.** [Model](../science/model.md) · [Early readout comparison](../science/early-readout.md).

### M05 A single quantum flag

**Central question.** How can two different errors give flag states that cannot be perfectly distinguished?

**Understanding target.** Put two pure flag states in a basis where a change of error bit flips the relative sign and leaves both squared amplitudes unchanged. Compute their inner product $c_i$ from those two weights.

**Prerequisites.** [M01](#m01-a-physical-bit-flip).

**Conceptual connection.** A computational-basis readout samples the weights and therefore yields identical distributions for the two flags. The evidence lies in the relative sign.

**Canonical sources.** [Model](../science/model.md) · [Watrous bridge](WATROUS_BRIDGE.md).

### M06 Product flags and phase characters

**Central question.** How does an entire pattern act on the product flag?

**Understanding target.** For a basis string $z$, derive a coefficient with a fixed magnitude and sign $(-1)^{x\cdot z}$. Compute the inner product of two product flags as the product of the individual overlaps at the sites where their patterns differ.

**Prerequisites.** [M02](#m02-adjacent-parity-checks), [M05](#m05-a-single-quantum-flag).

**Conceptual connection.** For complementary patterns, every factor contributes an overlap. The squared amplitude distribution can stay fixed even if the full-record inner product becomes very small.

**Canonical sources.** [Model](../science/model.md) · [Streaming decoder](../science/streaming-decoder.md).

### M07 Pattern weights and conditional priors

**Central question.** How do original error probabilities become the priors for a binary readout?

**Understanding target.** For a pair of pattern weights $a,b$, identify $a+b$ as the probability of seeing their syndrome and $a/(a+b),b/(a+b)$ as the probabilities once that syndrome is known. Under independent equal-rate physical flips, connect the weights to the number of flipped sites.

**Prerequisites.** [M03](#m03-complementary-errors-and-logical-failure).

**Conceptual connection.** Syndromes with the same pair overlap can lead to different decision rules because their priors differ.

**Canonical sources.** [Model](../science/model.md) · [Watrous bridge](WATROUS_BRIDGE.md).

### M08 An instrument retains two kinds of output

**Central question.** How does a branch operator specify the classical outcome and the surviving qubit?

**Understanding target.** Relate $K_y$ to its effect $K_y^\dagger K_y$, its probability and its normalized output state. Use the sum of effects to check that the operation accepts all inputs.

**Prerequisites.** [M05](#m05-a-single-quantum-flag).

**Conceptual connection.** The effects describe measured outcome probabilities. The branch operators also describe which coherence is available for a later decision.

**Canonical sources.** [Streaming decoder](../science/streaming-decoder.md) · [Watrous, §§2.2.2 and 2.3.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf).

### M09 The optimal binary readout

**Central question.** What measurement minimizes the chance of choosing the wrong error pattern?

**Understanding target.** Form the weighted state difference and identify the positive and negative eigenspaces used by a Holevo–Helstrom measurement. For two pure states, reduce the calculation to their two-dimensional span and relate the resulting risk to the overlap and the two priors.

**Prerequisites.** [M05](#m05-a-single-quantum-flag), [M07](#m07-pattern-weights-and-conditional-priors), [M08](#m08-an-instrument-retains-two-kinds-of-output).

**Conceptual connection.** Changing the priors changes the weighted state difference even when the candidate flags themselves stay fixed.

**Canonical sources.** [Watrous, Theorem 3.4](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) · [Watrous bridge](WATROUS_BRIDGE.md).

### M10 Add risks across syndromes

**Central question.** How does optimal performance within one syndrome class determine a full decoder's error?

**Understanding target.** Multiply each conditional binary error by the probability of receiving that syndrome. Sum once over the distinct classes. Recognize when a formula already uses unnormalized weights and therefore already includes that factor.

**Prerequisites.** [M07](#m07-pattern-weights-and-conditional-priors), [M09](#m09-the-optimal-binary-readout).

**Conceptual connection.** An early decoder must account for every positive-weight syndrome, including ones that prefer different readout rules.

**Canonical sources.** [Model](../science/model.md) · [Watrous bridge](WATROUS_BRIDGE.md).

### M11 The matched decoding problem

**Central question.** What must be held fixed when comparing different amounts of coherent memory?

**Understanding target.** Specify the same flag ensemble, syndrome timing, prior and logical loss for three receivers: a full-record receiver, a streaming receiver with persistent coherence, and a receiver that converts every flag into one classical transcript before the checks arrive.

**Prerequisites.** [M04](#m04-the-late-syndrome), [M06](#m06-product-flags-and-phase-characters), [M08](#m08-an-instrument-retains-two-kinds-of-output), [M10](#m10-add-risks-across-syndromes).

**Conceptual connection.** Unlimited classical storage and arbitrary temporary quantum processing are available to the early receiver. The comparison isolates coherence retained across the timing cut.

**Canonical sources.** [Model](../science/model.md) · [Early readout comparison](../science/early-readout.md).

## Phase II. Narrative and innovation

### M12 Split the input amplitudes by parity

**Central question.** Which basis amplitudes respond differently when the two candidate errors are complements?

**Understanding target.** Identify the even and odd sectors of the flag basis. Show that complementing all error bits changes the phase precisely on the odd sector. Compute the two sector weights $A,B$ and read their difference as the full candidate overlap.

**Prerequisites.** [M03](#m03-complementary-errors-and-logical-failure), [M06](#m06-product-flags-and-phase-characters).

**Conceptual connection.** Relative phase between the sectors carries the distinction used in the final decision.

**Canonical sources.** [Streaming decoder](../science/streaming-decoder.md).

### M13 Couple the sector weights

**Central question.** How can each branch select one coordinate from each sector while respecting the full input weights?

**Understanding target.** Normalize the squared amplitudes within each sector. Choose a joint distribution with those two marginals, for example their independent product. Explain what the row sums and column sums prescribe.

**Prerequisites.** [M08](#m08-an-instrument-retains-two-kinds-of-output), [M12](#m12-split-the-input-amplitudes-by-parity).

**Conceptual connection.** The marginals allocate each input basis direction across branch operators. The freedom in the coupling allows several implementations of the same discrimination guarantee.

**Canonical sources.** [Streaming decoder](../science/streaming-decoder.md) · [Two-flag example](WATROUS_BRIDGE.md#work-through-two-flags).

### M14 Build a complete fusion instrument

**Central question.** Why does the proposed pair-selection operation define a valid instrument?

**Understanding target.** Follow one even component to the output zero state and one odd component to the output one state, with weights chosen using the coupling. Calculate the resulting diagonal effect, then sum across all branches to recover the identity.

**Prerequisites.** [M08](#m08-an-instrument-retains-two-kinds-of-output), [M13](#m13-couple-the-sector-weights).

**Conceptual connection.** Completeness makes the operation deterministic as an instrument. Each run produces a branch and a conditional qubit without requiring a successful postselection event.

**Canonical sources.** [Streaming decoder](../science/streaming-decoder.md) · [Watrous, §2.2.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf).

### M15 Read what survives in a branch

**Central question.** What do the classical branch and its qubit tell the decoder?

**Understanding target.** Apply one branch operator to the product flag. Show that its probability is independent of the hidden error pattern and its normalized output has sector weights $A,B$ and relative sign $(-1)^{x\cdot(u\oplus v)}$.

**Prerequisites.** [M06](#m06-product-flags-and-phase-characters), [M14](#m14-build-a-complete-fusion-instrument).

**Conceptual connection.** Independence leaves the case priors unchanged. The label still identifies the coordinate dependence of the phase.

**Canonical sources.** [Streaming decoder](../science/streaming-decoder.md) · [Two-flag example](WATROUS_BRIDGE.md#work-through-two-flags).

### M16 Keep the phase index

**Central question.** Why does the repetition decoder need only one running index?

**Understanding target.** In a two-input fusion, show that an even coordinate and an odd coordinate differ at exactly one of their two positions. Interpret that choice as either retaining the old sign bit's index or selecting the new flag's index.

**Prerequisites.** [M15](#m15-read-what-survives-in-a-branch).

**Conceptual connection.** The transcript can be updated online. At the end, the sign depends on one known site even though the overlap contains contributions from every site.

**Canonical sources.** [Streaming decoder](../science/streaming-decoder.md).

### M17 Iterate the overlap product

**Central question.** What stays true after every streaming step, and what memory does it require?

**Understanding target.** Establish the running invariant: after each flag, the retained state has the product overlap over all processed sites, a relative phase indexed by one of those sites, and classical branch probabilities independent of the hidden pattern. Count the persistent qubit and index, the arriving flag, and the temporary workspace separately.

**Prerequisites.** [M12](#m12-split-the-input-amplitudes-by-parity), [M16](#m16-keep-the-phase-index).

**Conceptual connection.** A narrow persistent register can carry an increasingly distinguishable pair without retaining a coherent register per site.

**Canonical sources.** [Streaming decoder](../science/streaming-decoder.md).

### M18 Use the late syndrome

**Central question.** How does the syndrome turn the running phase into a decision about the logical error?

**Understanding target.** Choose a representative of the received syndrome, compute its bit at the retained index, and remove the corresponding known sign. The other candidate has the opposite sign. Set the Helstrom measurement using the two conditional priors.

**Prerequisites.** [M03](#m03-complementary-errors-and-logical-failure), [M09](#m09-the-optimal-binary-readout), [M17](#m17-iterate-the-overlap-product).

**Conceptual connection.** The index fixes how to interpret the phase. The syndrome fixes both the pair and its weights before the decoder chooses the final measurement.

**Canonical sources.** [Streaming decoder](../science/streaming-decoder.md) · [Watrous bridge](WATROUS_BRIDGE.md).

### M19 Match the full-record optimum

**Central question.** Why does the decoder lose no discrimination performance by fusing the flags?

**Understanding target.** Compare the overlap and priors of the streamed pair with those of the stored full pair for each syndrome. Convert equality of those quantities into equality of logical error after summing over all syndrome classes.

**Prerequisites.** [M10](#m10-add-risks-across-syndromes), [M11](#m11-the-matched-decoding-problem), [M18](#m18-use-the-late-syndrome).

**Conceptual connection.** Exact losslessness concerns the task conditioned on the syndrome. The decoder need not reconstruct every flag to meet that task.

**Canonical sources.** [Streaming decoder](../science/streaming-decoder.md) · [Watrous bridge](WATROUS_BRIDGE.md).

### M20 One parent measurement

**Central question.** What measurement structure is forced by a wholly classical early record?

**Understanding target.** Describe a fixed early POVM followed by a syndrome-dependent choice made from its classical outcome. For two selected syndromes, gather outcomes into the four possible pairs of binary decisions and identify the two marginal measurements.

**Prerequisites.** [M08](#m08-an-instrument-retains-two-kinds-of-output), [M11](#m11-the-matched-decoding-problem).

**Conceptual connection.** Even a fully collective early measurement must provide both late decisions through a common positive measurement.

**Canonical sources.** [Early readout comparison](../science/early-readout.md).

### M21 Optimality on each syndrome span

**Central question.** What must an early marginal do to reproduce the Helstrom optimum for a given syndrome?

**Understanding target.** Explain why the positive and negative eigenvectors of the weighted difference must give their respective optimal outcomes with probability one when neither eigenvalue vanishes. Identify the two-dimensional span on which this conclusion is constrained.

**Prerequisites.** [M09](#m09-the-optimal-binary-readout), [M20](#m20-one-parent-measurement).

**Conceptual connection.** The constraints on different syndrome spans can conflict even when there is freedom in how an effect acts outside either span.

**Canonical sources.** [Early readout comparison](../science/early-readout.md) · [Watrous, Theorem 3.4](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf).

### M22 A test using cross-syndrome overlaps

**Central question.** How can the relative geometry of two optimal decision bases rule out a common measurement?

**Understanding target.** Form the matrix of overlaps between the two signed eigenbases. Use certainty on each individual basis vector to isolate the single joint POVM effect that can contribute to each overlap. Apply positivity and Cauchy–Schwarz to obtain the operator-norm bound on the matrix of absolute overlaps.

**Prerequisites.** [M20](#m20-one-parent-measurement), [M21](#m21-optimality-on-each-syndrome-span).

**Conceptual connection.** A violation of the bound suffices to prove an early readout loss. A matrix that satisfies this particular bound still needs a compatibility test.

**Canonical sources.** [Early readout comparison](../science/early-readout.md).

### M23 Four flags give a strict memory advantage

**Central question.** Where do the incompatible measurements come from in the finite example?

**Understanding target.** Compare the representative patterns $0001$ and $0011$, each with its complement, at physical error probability $1/4$. Explain why one syndrome has biased pattern weights and the other equal weights. Trace the resulting Bloch-axis rotations into the overlap matrix and use its norm violation to certify a strict total-risk gap.

**Prerequisites.** [M07](#m07-pattern-weights-and-conditional-priors), [M12](#m12-split-the-input-amplitudes-by-parity), [M22](#m22-a-test-using-cross-syndrome-overlaps).

**Conceptual connection.** This gap concerns one declared finite instance and applies to arbitrary early collective measurements. At flag overlap $99/100$, the certificate lower-bounds the logical error gap by $2.5\times10^{-6}$.

**Canonical sources.** [Early readout comparison](../science/early-readout.md) · [Verification](../verification/README.md).

### M24 When balanced priors remove the gap

**Central question.** When can the receiver measure the streamed qubit early and still attain the full-record optimum?

**Understanding target.** Show that equal priors within every syndrome pair select the same sign-sensitive measurement on the streamed qubit. Store the outcome and index classically, then use the syndrome representative to interpret the outcome after the checks arrive.

**Prerequisites.** [M09](#m09-the-optimal-binary-readout), [M18](#m18-use-the-late-syndrome), [M23](#m23-four-flags-give-a-strict-memory-advantage).

**Conceptual connection.** The finite necessity result depends on prior structure. The streaming instrument itself works with either balanced or biased priors.

**Canonical sources.** [Early readout comparison](../science/early-readout.md) · [Streaming decoder](../science/streaming-decoder.md).

### M25 Compare reliability rates under local readout

**Central question.** How much faster can the ideal delayed error fall than the error of a receiver that measures flags individually?

**Understanding target.** For independent bit flips and a fixed overlap, connect the conditional pure-state error to the ordinary repetition-code tail multiplied, up to constants, by a squared overlap product. For immediate one-flag readout, relate the classical overlap of the two possible outcome distributions to the quantum flag overlap.

**Prerequisites.** [M10](#m10-add-risks-across-syndromes), [M19](#m19-match-the-full-record-optimum), [M20](#m20-one-parent-measurement).

**Conceptual connection.** The local asymptotic comparison charges one-flag consumption. A finite gap against every early joint POVM and an asymptotic exponent gap against such joint POVMs are different claims.

**Canonical sources.** [Early readout comparison](../science/early-readout.md) · [Watrous, §3.2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf).

### M26 A phase flip in storage

**Central question.** How does dephasing of the retained qubit affect the final logical correction?

**Understanding target.** Model a storage phase flip as a random reversal of the qubit's relative sign. Compute the attenuated off-diagonal element and explain why final quantum discrimination cannot outperform an observer given the noisy sign directly.

**Prerequisites.** [M15](#m15-read-what-survives-in-a-branch), [M18](#m18-use-the-late-syndrome).

**Conceptual connection.** Excellent flag overlap does not prevent randomization of the very phase that carries the logical choice.

**Canonical sources.** [Noise analysis](../science/noise.md).

### M27 Add operating errors to the benchmark

**Central question.** How can an ideal strict gap give a quantitative test for an imperfect decoder?

**Understanding target.** Relate circuit or state perturbations to changes in guessing risk using trace distance. Track whether an error bound applies to the stored qubit or to the entire branch-and-index instrument. Compare the resulting risk budget with a certified ideal gap against the matched early receiver. Distinguish a final phase flip from one that an intervening fusion can discard when it refreshes the phase index.

**Prerequisites.** [M17](#m17-iterate-the-overlap-product), [M23](#m23-four-flags-give-a-strict-memory-advantage), [M26](#m26-a-phase-flip-in-storage).

**Conceptual connection.** A robustness statement requires quantitative control of the operations in the proposed experiment as well as a positive ideal separation.

**Canonical sources.** [Noise analysis](../science/noise.md) · [Early readout comparison](../science/early-readout.md).

### M28 Replace parity by kernel characters

**Central question.** How can the fusion idea handle a linear syndrome with more than two possible patterns?

**Understanding target.** Write a syndrome class as an affine translate of the kernel of the binary check map. Group computational-basis coordinates by their restriction to this kernel. Recognize the even and odd sectors of the repetition code as the case of a one-dimensional kernel.

**Prerequisites.** [M02](#m02-adjacent-parity-checks), [M06](#m06-product-flags-and-phase-characters), [M12](#m12-split-the-input-amplitudes-by-parity).

**Conceptual connection.** Each character sector is an amplitude component whose pattern-dependent phase can be tracked through the delayed syndrome.

**Canonical sources.** [Linear syndromes](../science/linear-syndromes.md).

### M29 Preserve the conditional ensemble

**Central question.** What guarantee replaces equal pair overlaps when a syndrome leaves several candidates?

**Understanding target.** Follow a branch with one representative basis index per character and explain how the received syndrome removes the resulting known phases. Compare the conditional Gram matrices of the original and compressed ensembles. Use equality to recover optimal discrimination with $k$ persistent qubits for a kernel of dimension $k$. For an instrument required to preserve the optimum for every prior, explain how two prior ratios force an isometry on each candidate-pair span and how the pair constraints make the width sharp.

**Prerequisites.** [M13](#m13-couple-the-sector-weights), [M19](#m19-match-the-full-record-optimum), [M28](#m28-replace-parity-by-kernel-characters).

**Conceptual connection.** Matching an entire Gram matrix preserves the conditional pure-state ensemble up to an isometry. In a degenerate stabilizer problem, several candidate physical patterns may correspond to one logical class, so the relevant memory requirement can be a separate question.

**Canonical sources.** [Linear syndromes](../science/linear-syndromes.md) · [Watrous, §3.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf).

### M30 The complete decoding story

**Central question.** When is retained coherence exactly enough, when is it indispensable, and what could change these conclusions?

**Understanding target.** Explain the full chain from stochastic flips and late checks through parity-sector fusion, indexed phase recovery and conditional discrimination. Give the exact finite memory separation and its balanced-prior special case. State the scope of the local rate, the noise comparison and the linear-syndrome extension.

**Prerequisites.** [M19](#m19-match-the-full-record-optimum), [M23](#m23-four-flags-give-a-strict-memory-advantage), [M24](#m24-when-balanced-priors-remove-the-gap), [M25](#m25-compare-reliability-rates-under-local-readout), [M27](#m27-add-operating-errors-to-the-benchmark), [M29](#m29-preserve-the-conditional-ensemble).

**Conceptual connection.** Identify whether a new proposal changes the input flag states, the timing, the desired logical decision or the charged implementation resources. These changes can move the proposal outside the scope of the demonstrated memory advantage.

**Canonical sources.** [Model](../science/model.md) · [Streaming decoder](../science/streaming-decoder.md) · [Early readout comparison](../science/early-readout.md) · [Noise analysis](../science/noise.md) · [Linear syndromes](../science/linear-syndromes.md).
