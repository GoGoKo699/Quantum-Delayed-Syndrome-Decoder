# Error flags and the delayed syndrome

A repetition code protects a logical qubit against stochastic bit flips. Each physical error also leaves a flag in a separate qubit. The two possible flag states overlap, so a measurement of a flag can supply likelihood information without revealing its bit with certainty. The timing of that measurement matters because the stabilizer syndrome determines which candidate errors are relevant.

## Stochastic error instrument

At site $i$, let $x_i\in\{0,1\}$ indicate whether an $X$ error occurred. For independent errors of probability $p$ the channel at each site is

```math
\mathcal N_i(\rho)=\sum_{b=0}^1 p_b X^b\rho X^b
  \otimes |f^{(i)}_b\rangle\langle f^{(i)}_b|,
\qquad (p_0,p_1)=(1-p,p).
```

Equivalently, an orthogonal environment record can coherently control the Pauli and the flag preparation before being discarded. The decoder receives the flag only. We use known pure flags with overlaps $0<c_i<1$. A known choice of local basis and phases gives

```math
|f^{(i)}_b\rangle
  =\sqrt{\frac{1+c_i}{2}}\,|0\rangle
   +(-1)^b\sqrt{\frac{1-c_i}{2}}\,|1\rangle .
```

The streaming construction also applies to arbitrary known priors on error strings when the error channel is a classical mixture with conditionally product flags. Comparisons that require independent errors state that assumption explicitly.

## Side information and allowed recovery

The stabilizers $Z_iZ_{i+1}$ report the exact parity bits $s_i=x_i\oplus x_{i+1}$. The flags arrive and must be processed before these bits are available. Given $s$, the two compatible strings are a computable representative $r_s$ and its complement $\bar r_s$. Their corrections differ by $X^{\otimes n}$, which acts as the logical $X$.

The decoder can use any classical storage and a declared quantum register across the cut, then return a Pauli correction. It acts on the flag systems at the cut. The logical payload and other devices cannot be used as additional decoder memory. The benchmark with zero persistent qubits permits an arbitrary joint POVM on all flags before the cut. Its classical output can be postprocessed with the syndrome in any way. Giving this benchmark joint access makes it stronger than immediate single-flag detection. The benchmark that waits keeps all flags until the syndrome and then allows any measurement on them.

An incorrectly chosen string applies a logical $X$. For an arbitrary input qubit, including a qubit entangled with a reference, the corrected channel is a mixture of the identity and logical $X$. The coefficient of logical $X$ is the logical failure probability. It equals entanglement infidelity and half the diamond distance from the logical identity. The maximally entangled logical-reference state distinguishes the two Pauli branches exactly.

## Full-record optimum

Let $a=\Pr(x=r_s)$ and $b=\Pr(x=\bar r_s)$ be the unnormalized weights. The flag vectors have real overlap $d=\prod_i c_i$, since the candidates differ at every site. The Holevo–Helstrom bound yields the total optimum

```math
R_{\mathrm{wait}}=\frac12\sum_s
   \left[a+b-\sqrt{(a+b)^2-4ab\,d^2}\right].
```

A syndrome of zero probability contributes zero. The [streaming decoder](streaming-decoder.md) preserves the overlap and the prior in each syndrome branch. [Early readout](early-readout.md) tests whether a measurement with purely classical output can attain this expression. [Noise and timing](noise.md) track which gains survive imperfections in the flag path. [Linear syndromes](linear-syndromes.md) treat more than two compatible error strings.
