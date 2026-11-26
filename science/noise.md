# Noise on the retained qubit

The ideal streaming decoder preserves the discrimination problem conditional on each repetition-code syndrome. Two concrete deviations admit separate bounds. A phase flip after compression corrupts the final readout. Phase flips between ideal fusion steps can also propagate, but a fusion can discard the old sign and replace it with the sign of a fresh flag.

## Final storage dephasing

Write $`a,b`$ for the unnormalized probabilities of the two strings compatible with a syndrome. After correcting the syndrome-dependent sign convention, the stored states are

```math
|\phi_\pm\rangle=\sqrt{\frac{1+c^n}{2}}|0\rangle\ \pm\
\sqrt{\frac{1-c^n}{2}}|1\rangle .
```

Their overlap is $`c^n`$. Let $`H(a,b)`$ denote their weighted Helstrom error, which can be evaluated as

```math
H(a,b)=\frac{a+b-\sqrt{(a+b)^2-4ab c^{2n}}}{2}.
```

Suppose storage applies $`Z`$ with independent probability $`q\in[0,1/2]`$ and the identity otherwise. Define $`C_q(a,b)=\min\{a,b,q(a+b)\}`$. This is the weighted error if an observer is given the corrupted sign itself as a classical bit, because the optimal decision either uses it directly or always guesses the more likely sign. The actual weighted quantum risk $`H_q(a,b)`$ obeys

```math
\max\{C_q(a,b),H(a,b)\}\le H_q(a,b)\le C_q(a,b)+H(a,b).
```

The first lower bound follows because preparing $`|\phi_\pm\rangle`$ from the corrupted sign can only reduce the information. The second follows because dephasing is a channel applied to the ideal states.

For the upper bound, set $`\alpha=(1-q)a-qb`$ and $`\beta=(1-q)b-qa`$. The noisy weighted Helstrom difference is $`\alpha|\phi_+\rangle\langle\phi_+|-\beta|\phi_-\rangle\langle\phi_-|`$. If either coefficient is nonpositive, the difference has a fixed sign and the best decision uses only the prior. In this case $`H_q=C_q`$. Otherwise the trace-norm formula gives

```math
H_q(a,b)=q(a+b)+H(\alpha,\beta).
```

Here $`C_q=q(a+b)`$, $`\alpha\le a`$, and $`\beta\le b`$. The minimum of weighted testing risks is nondecreasing in each weight, giving the upper bound. These statements hold syndrome by syndrome, and the same bounds hold for total risks on summing over syndromes.

Writing $`C=c^n`$, $`m=a-b`$ and $`K=(a+b)\sqrt{1-C^2}`$ gives a useful finite-block version. The noisy weighted Helstrom difference has trace $`m`$ and Bloch-vector length $`\sqrt{m^2C^2+K^2(1-2q)^2}`$, so its trace norm is the larger of the absolute trace and that length. Convexity of $`x\mapsto\sqrt{m^2C^2+K^2 x^2}`$ at $`x=1`$ yields

```math
0\le H_q(a,b)-H(a,b)\le q\frac{K^2}{\sqrt{m^2C^2+K^2}} .
```

When both branch weights vanish, the contribution is zero. At the [four-flag point](early-readout.md), the syndrome pairs have lower Hamming weights $`0,1,2`$ with multiplicities $`1,4,3`$. The corresponding values of $`K^2/\sqrt{m^2C^2+K^2}`$ are bounded above by $`0.0254`$, $`0.0111`$ and $`0.0196`$. For each bound $`v`$, substitute the weights $`(a,b)=(81,1)/256`$, $`(27,3)/256`$ or $`(9,9)/256`$ and check the rational inequality $`K^4\lt v^2(m^2C^2+K^2)`$. The weighted sum is below $`0.13`$. For $`q\le1.9\times 10^{-5}`$, the total error increase is therefore below $`2.47\times 10^{-6}`$, smaller than the certified $`2.5\times 10^{-6}`$ gap to arbitrary early joint readout.

## Storage noise and the exponent

Take $`0\lt p\lt 1/2`$, $`0\lt c\lt 1`$ fixed, write $`\ell=\log((1-p)/p)`$ and use natural logarithms. Let

```math
D(t\|p)=t\log\frac{t}{p}+(1-t)\log\frac{1-t}{1-p}
```

be the binary relative entropy. For $`q_n=\exp(-\gamma n+o(n))`$ with finite $`\gamma\ge0`$ and $`q_n\le1/2`$, the exponent of the optimal noisy final readout is

```math
\min\left\{
-\log\!\left(2\sqrt{p(1-p)}c^2\right),\
\gamma+D\left(\max\left\{p,\frac{1-\gamma/\ell}{2}\right\}\,\middle\|\,p\right)
\right\}.
```

To derive the second entry, orient a compatible pair so its lower-weight string has Hamming weight $`nt\le n/2`$. For its probability $`a`$ and the complementary probability $`b`$, the ratio is $`b/a=\exp[-n(1-2t)\ell]`$. The exact sign-channel risk $`\min\{b,q_n(a+b)\}`$ lies between $`\min\{b,q_na\}`$ and twice that quantity. Summing Hamming types gives the exponent

```math
\min_{0\le t\le 1/2}\left[D(t\|p)+\max\left\{\gamma,(1-2t)\ell\right\}\right].
```

For $`(1-2t)\ell\ge\gamma`$, the objective equals $`D(1-t\|p)`$, which decreases with $`t`$ on this interval. On the other interval it equals $`\gamma+D(t\|p)`$, minimized at the larger of $`p`$ and the interval's left endpoint. Type multiplicities change the finite sum by subexponential factors for the purpose of this limit. Finally the maximum and sum risk bounds above imply that the noisy exponent is the smaller of the ideal and sign-channel exponents.

In particular, any fixed $`0\lt q\le1/2`$ retains the syndrome-only exponent $`D(1/2\|p)=-\log(2\sqrt{p(1-p)})`$. The ideal one-qubit exponent assumes phase noise falls sufficiently rapidly with block length, while the finite-block decoder can remain useful at nonzero dephasing.

## Phase flips during fusion

Consider the ideal two-input fusion followed by an independent memory $`Z`$ flip of probability $`\eta_i`$ at step $`i`$. New flags are noiseless in this model. Fusion outcomes are independent of the input signs, including signs affected by prior flips. The fusion outcome specifies whether the new retained sign comes from the old key or the incoming flag. Conditional on the fusion transcript, let $`q_i`$ be the probability that the retained sign after step $`i`$ differs from the one without noise. From a perfect initial flag, $`q_1=0`$, and

```math
q_i=\eta_i+(1-2\eta_i)\,q_{i-1}\,
\mathbf{1}\{\text{the fusion keeps the old key}\}.
```

When the new key comes from the incoming flag, earlier flips no longer affect the output sign. The recurrence accounts only for independent phase flips of the stored qubit after otherwise ideal operations.

One can choose the coupling in the fusion instrument to maximize this refresh probability. For the overlap $`d`$ of the old compressed flag and the incoming overlap $`c`$, put $`A_d=(1+d)/2`$, $`B_d=(1-d)/2`$ and define $`A_c,B_c`$ likewise. The even sector has normalized weight $`A_d A_c/(A_d A_c+B_d B_c)`$ on $`00`$. The odd sector has normalized weight $`A_d B_c/(A_d B_c+B_d A_c)`$ on $`01`$. These are the two outcomes that can be matched to keep the new key, along with the complementary match $`11`$ to $`10`$. Coupling the two binary marginals to maximize their matching probability makes the chance of keeping the old key equal to the absolute difference of those two normalized weights. Simplifying,

```math
\Pr(\text{old key})=\frac{c(1-d^2)}{1-d^2c^2}\le c .
```

Taking constant $`\eta_i=\eta\le1/2`$ gives $`\mathbb E[q_i]\le\eta/[1-c(1-2\eta)]`$. A decoder that keeps the transcript can compute $`q_i`$ and use the corresponding noisy Helstrom readout rather than using the average. The final storage bounds apply to each transcript. A fixed independent phase flip immediately before the final readout still imposes the fixed-noise exponent above.

For more general noise, let the implemented step, including its classical outcome, differ from the ideal step by at most $`\varepsilon_i`$ in diamond norm. The resulting logical failure probability differs from ideal by at most $`\tfrac12\sum_i\varepsilon_i`$. Replace the steps one at a time, use trace-distance contraction for the remaining quantum operations and classical feedback, and bound the change of a measurement probability by half the trace norm. This finite-block stability statement supplies an error budget for a realization. It makes no claim of fault tolerance under general circuit noise.
