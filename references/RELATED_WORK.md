# Related work

The decoder concerns classical Pauli bit flips accompanied by pure, partly informative quantum flags. The side information is an exact delayed syndrome. The cost of interest is coherent width across that cut, with classical storage and postprocessing available.

## Discrimination with later information

Ballester, Wehner and Winter formulated state discrimination when extra information arrives after a measurement or after a quantum-memory bound applies. Carmeli, Heinosaari and Toigo showed that early and late guessing probabilities coincide exactly when suitable optimal measurements for the subensembles are jointly measurable. A stabilizer syndrome is a concrete choice of subensemble in this framework. The [four-flag certificate](../science/early-readout.md) supplies an incompatibility calculation and a finite error bound within the repetition-code model. [Ballester, Wehner and Winter, IEEE Trans. Inf. Theory 54, 4183 (2008)](https://arxiv.org/abs/quant-ph/0608014) · [Carmeli, Heinosaari and Toigo, Phys. Rev. A 98, 012126 (2018)](https://doi.org/10.1103/PhysRevA.98.012126)

Acín and coauthors attain the binary collective optimum using adaptive individual measurements when the two hypotheses are known. With a repetition syndrome supplied before readout, local relabeling makes the two hypotheses known. In the early-readout comparison the local policy must be chosen before that relabeling is known. [Acín et al., Phys. Rev. A 71, 032338 (2005)](https://doi.org/10.1103/PhysRevA.71.032338)

## Quantum belief propagation and compression

Renes’s pure-state variable-node convolution combines two states with the same known input label and multiplies their overlaps. The check node processes an unknown parity as a mixture. Piveteau and Renes generalize optimal pure-state decoding on suitable graphs. Their recent subspace-decoding primitive groups Fourier coordinates by a linear image and conditionally uncomputes nuisance registers for a specified subspace decoding problem. These results supply close constructions and an efficient decoding framework. [Renes, New J. Phys. 19, 072001 (2017), Eqs. (4)–(8)](https://arxiv.org/abs/1607.04833) · [Piveteau and Renes, Quantum 6, 784 (2022)](https://doi.org/10.22331/q-2022-08-23-784) · [Piveteau and Renes, arXiv:2509.19441v1 (2025), Def. 3.2 and Lemma 3.1](https://arxiv.org/html/2509.19441v1)

Here the error label lies in an affine syndrome class that is still unknown at the cut. Conditioning a pure-state fusion on equality of its two inputs would require the missing parity. In the simplest case of two equally noisy flags, grouping the Fourier coordinates by parity and measuring one raw nuisance coordinate leaves a sign encoded with the single-flag overlap. The [coupling instrument](../science/streaming-decoder.md) chooses an outcome whose law is independent of the input and keeps the product overlap for both possible parity classes. The [linear extension](../science/linear-syndromes.md) provides a common instrument before any affine representative is available.

Koashi and Imoto characterize operations that preserve a family of states. In [the memory converse](../science/linear-syndromes.md), exact preservation of binary and triple-prior decision experiments implies a scaled isometry on the pure-state span, which yields the requisite coherent dimension. [Koashi and Imoto, Phys. Rev. A 66, 022318 (2002)](https://doi.org/10.1103/PhysRevA.66.022318)

## Flags for error correction

Flagged weight optimization uses already classical flag values to improve decoder likelihoods. Soft-information repetition-code experiments also use analog measurement records as classical input. These applications motivate asking whether any information is lost when a flag is first converted to a classical value. The present model isolates that readout question with pure state flags and a delayed, otherwise perfect syndrome. [Takada and Fujii, PRX Quantum 5, 030352 (2024)](https://doi.org/10.1103/PRXQuantum.5.030352) · [Hanisch, Hetényi and Wootton, APS Open Sci. 1, 000019 (2026)](https://doi.org/10.1103/y9fh-4x6n)

The [bibliography](references.bib) also lists the textbook supporting the [learning route](../learning/WATROUS_BRIDGE.md).
