# From Watrous to decoding with a late syndrome

An encoded qubit can suffer several patterns of physical bit flips. The repetition-code checks tell the decoder which adjacent error bits disagree, leaving two possible patterns. A quantum flag from each site provides partial evidence about its error bit. The central design problem is deciding what to keep from the flags while the checks are still on their way.

The educational anchor is **John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018**. Use the section numbering of the author's prepublication manuscript dated January 2018. [Author's book page](https://cs.uwaterloo.ca/~watrous/TQI/) · [Manuscript contents](https://cs.uwaterloo.ca/~watrous/TQI/TQI.frontmatter.pdf)

Watrous supplies the principles of instruments and discrimination. The parity model, the fusion operation that precedes the syndrome, and the limit on early classical readout are developed in this project. Use the [30-milestone map](MILESTONES.md) for the full route and the [model](../science/model.md) for the exact assumptions.

## Read the relevant sections

| Milestones | Source | What to take into the project |
|---|---|---|
| M01, M05–M06 | [Chapter 2, §2.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | A state vector describes a pure flag. A tensor product describes the flags given a fixed error pattern. Taking a mixture over error patterns is a separate operation. |
| M08, M13–M17 | [Chapter 2, §§2.2.1–2.2.2 and 2.3.1–2.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | The Kraus completeness identity certifies that the fusion instrument is a physical channel. A measurement can keep an outcome label and a conditional quantum state. |
| M07, M09–M10, M18–M24 | [Chapter 3, §3.1.1, Theorem 3.4](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) | The weighted state difference defines the optimal binary decision. Its trace norm gives the optimum and its signed eigenspaces specify a measurement. |
| M25–M27 | [Chapter 3, §§3.2.1 and 3.2.3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) | The root fidelity of two pure states is their absolute overlap. Converting a flag to a classical outcome can only increase fidelity. Trace-norm distinguishability bounds the effect of perturbing the stored states. |
| M28–M29 | [Chapter 3, §3.1.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) | A binary linear syndrome can leave more than two candidates. The task is then discrimination of a finite ensemble, with the posterior priors set by that syndrome. |

## Translate the notation

| Watrous | This project | Role |
|---|---|---|
| $\rho_0,\rho_1$ | $\lvert\psi_{r_s}\rangle\langle\psi_{r_s}\rvert$ and $\lvert\psi_{\bar r_s}\rangle\langle\psi_{\bar r_s}\rvert$ | The full flag states for the two candidate patterns after the syndrome. |
| $\lambda,1-\lambda$ | $a/(a+b), b/(a+b)$ | Conditional priors computed from the original probabilities $a,b$ of the two patterns. |
| $\mu(y)$ | $E_y=K_y^\dagger K_y$ | The positive effect that fixes a branch's probability. The operator $K_y$ also specifies what quantum state remains. |
| $F(\rho_0,\rho_1)$ | $d=\prod_i c_i$ | The absolute overlap of the two full pure flags in a repetition-code syndrome class. The squared overlap is $d^2$. |
| $X$ as a weighted state difference in Theorem 3.4 | $D=a\rho_0-b\rho_1$ | The difference that determines the readout. In the project model, the Pauli $X$ instead denotes a physical bit flip. |

For positive $a,b$, the contribution of one syndrome class to the **total** logical error is

```math
e(a,b;d)=\frac{a+b-\sqrt{(a+b)^2-4abd^2}}{2}.
```

The theorem in Watrous normalizes the two priors. Multiplying its error formula by $a+b$ gives this expression, which can be added across disjoint syndrome classes. The square root is the trace norm of $D$ on the span of the two state vectors. On that span, $D$ has trace $a-b$ and determinant $-ab(1-d^2)$, so the eigenvalues have opposite signs whenever $0<d<1$. Measuring their signed eigenspaces gives the optimum. [Model](../science/model.md) · [Streaming decoder](../science/streaming-decoder.md)

## Work through two flags

Take two independent physical error bits of probability $1/4$, and let the two flags have overlaps $c_1=3/5$ and $c_2=1/2$. In the flag basis, the squared amplitudes of the two-qubit product flag are

| Basis string $z$ | $00$ | $01$ | $10$ | $11$ |
|---|---:|---:|---:|---:|
| Squared amplitude | $3/5$ | $1/5$ | $3/20$ | $1/20$ |
| Parity | Even | Odd | Odd | Even |

An error pattern $x$ changes the signs of these amplitudes by $(-1)^{x\cdot z}$, leaving their squares fixed. The total even and odd weights are $A=13/20$ and $B=7/20$. Use a branch that selects one even coordinate and one odd coordinate. A valid joint choice draws each coordinate according to its normalized weight within its sector. For example, the branch $(00,01)$ has probability $(12/13)(4/7)=48/91$, for every pattern $x$. Its output is, up to a global phase,

```math
\sqrt{13/20}\lvert 0\rangle+(-1)^{x_2}\sqrt{7/20}\lvert 1\rangle.
```

The two squared amplitudes stay fixed across all branches. Other branches can carry $x_1$ in the sign instead. Keep the index of the sign bit and discard the rest of the outcome label. For either sign bit, changing the error string to its complement reverses the relative sign. The two output states have overlap $A-B=3/10$, exactly the overlap $c_1c_2$ of the two full records in either syndrome class.

Now let the syndrome $x_1\oplus x_2$ arrive. If it is zero, the candidates $00$ and $11$ have probabilities $9/16$ and $1/16$. If it is one, $01$ and $10$ each have probability $3/16$. The same fusion instrument serves both classes, and the syndrome selects which prior and sign convention to use. In this example the two terms give an overall logical error of about $0.0137406$. The error is the same as for a decoder that held both flags and measured them after reading the syndrome. [Fusion and recursive overlap](../science/streaming-decoder.md)

## Follow the proof beyond two flags

The two-flag operation accepts a flag already compressed from several sites. Every step multiplies the overlap by that of the new flag and keeps a known coordinate of the unknown error pattern in its relative phase. One qubit and one index therefore suffice for the repetition decoder. This uses known pure flag states and exact late syndrome information. [Streaming decoder](../science/streaming-decoder.md)

To test whether the qubit is necessary, consider a record that is fully measured before the syndrome. Every possible late rule is a classical postprocessing of a single early measurement. The optimal binary decisions for two selected syndromes in the four-flag instance give a test of whether such a common measurement exists. This test depends on the relative eigenvectors across syndromes and on their priors. [Early readout comparison](../science/early-readout.md)

The [noise analysis](../science/noise.md) changes the retained states and bounds the corresponding change in logical risk. The [binary linear extension](../science/linear-syndromes.md) changes the set of possible patterns after the syndrome. It tracks a character of the kernel of the syndrome map in place of the two even/odd sectors. For a kernel of dimension $k$, the resulting instrument uses $k$ retained qubits. That width is necessary for exact full-error identification when one instrument has to preserve the optimum for every prior.
