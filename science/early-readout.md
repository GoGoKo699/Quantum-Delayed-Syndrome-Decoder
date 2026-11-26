# Early flag readout

This comparison gives every decoder the same error distribution, flag ensemble and exact repetition-code syndrome. The only difference is whether a quantum system may survive until the syndrome arrives. An early joint decoder can measure all flags together and keep an unlimited classical record. An early local decoder measures each flag once, with its choice of measurement and flag order allowed to depend on earlier outcomes. Neither decoder sees the syndrome before finishing its flag measurements.

## A four-flag memory separation

For each syndrome $s$, choose one compatible string $r_s$ and write its complement as $\bar r_s$. Let $|\psi_x\rangle=\bigotimes_i |f_{x_i}^{(i)}\rangle$ be the product of the flags from the [error model](model.md). Write $a_s=\Pr(r_s)$ and $b_s=\Pr(\bar r_s)$, and define the unnormalized Helstrom difference on the full flag register by

```math
D_s=a_s|\psi_{r_s}\rangle\langle\psi_{r_s}|-b_s|\psi_{\bar r_s}\rangle\langle\psi_{\bar r_s}|.
```

Its nonzero eigenvalues are $\lambda_{s,+}>0$ and $-\lambda_{s,-}<0$, with normalized eigenvectors $u_{s,+}$ and $u_{s,-}$. The delayed decoder attains the sum of the conditional Helstrom risks, each weighted by its syndrome probability. The one-qubit streaming instrument attains this same risk.

Any single early POVM, followed by a classical decision for each syndrome, can be coarse-grained to one outcome for each table of syndrome decisions. A randomized decision is included by adding classical randomness to the POVM. For two syndromes $s,t$, retain only their two entries, giving four effects $M_{ij}$ with $i,j\in\{+,-\}$. Put $G_{ij}=\langle u_{s,i}|u_{t,j}\rangle$ and let $|G|$ denote entrywise absolute values. Define $d_{s,i}$ as the probability of the wrong $s$-decision on the eigenvector $u_{s,i}$, and define $d_{t,j}$ analogously. The excess logical error over delayed Helstrom is at least

```math
\sum_i\lambda_{s,i}d_{s,i}+\sum_j\lambda_{t,j}d_{t,j}.
```

This follows by evaluating the marginal decision effects in each $D_s$ eigenbasis and subtracting the minimum error. The eigenvalues already include syndrome probabilities, so the expression needs no further probability factor.

For the contribution of the effect $M_{ij}$ alone, Cauchy–Schwarz for positive effects gives

```math
|\langle u_{s,i}|M_{ij}|u_{t,j}\rangle|
\le \sqrt{\langle u_{s,i}|M_{ij}|u_{s,i}\rangle\langle u_{t,j}|M_{ij}|u_{t,j}\rangle}.
```

Against any two nonnegative unit vectors $x,y$, the sum of these upper bounds weighted by $x_i y_j$ is at most one. Apply scalar Cauchy–Schwarz over $i,j$, using the row normalization for the $s$-vectors and column normalization for the $t$-vectors. The effects other than $M_{ij}$ can be partitioned into those with incorrect $s$-decision and those with correct $s$-decision but incorrect $t$-decision. Their contributions to $G_{ij}$ have magnitude at most $\sqrt{d_{s,i}}+\sqrt{d_{t,j}}$. Consequently

```math
\big\|\,|G|\,\big\|_2\le 1+2\sqrt{\sum_i d_{s,i}+\sum_j d_{t,j}}.
```

Here $\|\cdot\|_2$ is the largest singular value. The factor two follows by weighting the entrywise bounds with nonnegative unit vectors and using $\sum_i x_i,\sum_j y_j\le\sqrt 2$. If $\lambda_*$ is the least of the four positive eigenvalue magnitudes for $s,t$, every early joint measurement has excess logical error at least

```math
\frac{\lambda_*}{4}\left(\max\left\{0,\big\|\,|G|\,\big\|_2-1\right\}\right)^2.
```

### Explicit instance

Set $n=4$, $p=1/4$, $c=99/100$ and compare representatives $0001$ and $0011$. For each representative $r$, use the even and odd components of the flag vector $|\psi_r\rangle$, separately normalized, as an orthonormal pair. Its flag vector and the complementary flag vector then have coordinates $(\sqrt A,\sqrt B)$ and $(\sqrt A,-\sqrt B)$, where $A=(1+c^4)/2$ and $B=(1-c^4)/2$. Between the two pairs of basis vectors, the overlaps are diagonal, with entries

```math
e=\frac{c+c^3}{1+c^4},\qquad o=\frac{c-c^3}{1-c^4}=\frac{c}{1+c^2}.
```

These follow by projecting $|\psi_{0001}\rangle$ and $|\psi_{0011}\rangle$ onto each Fourier parity sector. The representatives differ at one site, while $0001$ differs from the complement of $0011$ at three sites.

The weight-one representative has prior odds $9$ and diagonalizes its $D_s$ by a rotation through $\theta\in(0,\pi/4)$, with

```math
\tan(2\theta)=\frac{5\sqrt{1-c^8}}{4c^4}.
```

The weight-two representative has equal weights and its two eigenvectors are the sum and difference of its even and odd basis vectors divided by $\sqrt 2$. Since $\tan\theta<o/e$ here, applying $|G|$ to $(1,1)^{\mathsf T}/\sqrt 2$ gives a vector of norm $\cos\theta\sqrt{e^2+o^2}$. The strict rational inequalities

```math
e>\frac{9995}{10000},\qquad o>\frac{4995}{10000},\qquad
\cos^2\theta>\frac{97}{100}
```

establish both the sign condition and $\big\|\,|G|\,\big\|_2>11/10$. For the last inequality, use $\cos(2\theta)=4c^4/\sqrt{25-9c^8}$ and square the positive bounds. Squaring the product lower bound gives a rational number larger than $121/100$.

The unequal-prior syndrome has weights $(a,b)=(27,3)/256$. Its smaller eigenvalue magnitude $z$ solves $z(z+a-b)=ab(1-c^8)$. Substituting $z=1/1000$ gives a strictly smaller left-hand side, so both eigenvalue magnitudes exceed $1/1000$. The equal-prior syndrome has both magnitudes $9\sqrt{1-c^8}/256>1/1000$. Thus $\lambda_*>1/1000$ and the early joint error exceeds the delayed error by more than $1/400000=2.5\times 10^{-6}$. The overlap expressions also give a strict gap at $c=19/20$. Zero retained qubits are insufficient at these parameters, even with a collective early readout.

At $p=1/2$ the compression qubit can be measured in the $X$ basis before syndrome arrival. The later syndrome and classical transcript determine whether to flip the recorded result. This attains delayed Helstrom exactly, so bias is essential to the finite counterexample above.

## Exponent for early single-flag measurements

For fixed $0<p<1$ and $0<c<1$, let $R_{\mathrm{loc}}(n)$ be the optimum logical error among policies that measure flags one at a time before the syndrome. With natural logarithms,

```math
\lim_{n\to\infty}-\frac1n\log R_{\mathrm{loc}}(n)
=-\log\!\left(2\sqrt{p(1-p)}c\right).
```

The ideal delayed exponent is $-\log\!\left(2\sqrt{p(1-p)}c^2\right)$. For the early-local upper bound on risk, repeat a measurement with single-flag classical Bhattacharyya coefficient $c$. The projective measurement along the $X$ axis in the symmetric flag representation has this coefficient. The bound follows from $\min(P,Q)\le\sqrt{PQ}$.

For the delayed exponent, orient each syndrome so $a_s\ge b_s$. Rationalizing its Helstrom risk bounds it between $b_s c^{2n}/2$ and $b_s c^{2n}$. The sum of the $b_s$ is the syndrome-only risk. For biased independent errors, it is the binomial tail above $n/2$ plus half the probability at $n/2$ when $n$ is even, after exchanging bit labels if necessary so $p<1/2$. Its exponent is $-\log(2\sqrt{p(1-p)})$. The equal-prior syndrome-only risk is $1/2$, which gives the same formula at $p=1/2$.

For the converse, fix an early local policy. Write $P(x,y)$ for the joint distribution of the error string $x$ and measurement record $y$, and $Q(x,y)=P(\bar x,y)$. The decoder sees the unordered pair $\{x,\bar x\}$ through the syndrome. Its optimal risk is therefore $\frac12\sum_{x,y}\min(P(x,y),Q(x,y))$. At measurement step $i$, conditional on preceding outcomes, denote the two flag outcome distributions by $f_{0,i}$ and $f_{1,i}$, and their Bhattacharyya coefficient by $B_i$. Including the current flag index in the record covers adaptive measurement order. The triangle inequality and positive-effect Cauchy–Schwarz give $B_i\ge c$ for any such measurement.

Define an auxiliary process using $g_i(y_i)=\sqrt{f_{0,i}(y_i)f_{1,i}(y_i)}/B_i$ as the outcome law at step $i$, with the measured error bit independently fair. Let $L=\log(P/Q)$ on the joint support. Under the auxiliary law, denoted by $\mathbb E_g$, the exact risk expression becomes

```math
R_{\text{policy}}=\frac12\left(2\sqrt{p(1-p)}\right)^n
\mathbb E_g\!\left[\left(\prod_i B_i\right)e^{-|L|/2}\right].
```

Given the complete record, $L$ is a sum of independent signed increments, with fair signs and magnitudes given by

```math
\left|\log\!\left(\frac{p\,f_{1,i}(y_i)}{(1-p)f_{0,i}(y_i)}\right)\right|.
```

The expected square of each increment is uniformly bounded at fixed $p,c$. Indeed, for $u,v>0$ the ratio $\sqrt{uv}\log^2(u/v)/(u+v)$ is bounded, so the integral against $g_i$ is bounded using $B_i\ge c$ and $\sum f_{0,i}=\sum f_{1,i}=1$. Outcomes outside the joint support have zero auxiliary weight. Hence $\mathbb E_g[L^2]\le C(p,c)n$. Jensen's inequality yields

```math
R_{\text{policy}}\ge \frac12\left(2\sqrt{p(1-p)}c\right)^n
\exp\left(-\frac{\sqrt{C(p,c)n}}2\right).
```

The bound holds uniformly over policies, including policies that change with $n$. The calculation extends to general outcome measures by using densities with respect to the sum of the two conditional outcome measures at each step. The exponent applies to immediate single-flag measurements and leaves the optimal asymptotic performance of immediate joint POVMs open.
