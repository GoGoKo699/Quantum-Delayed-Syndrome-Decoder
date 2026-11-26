# Quantum Delayed Syndrome Decoder

**How many qubits of error information should a decoder keep while it waits for the syndrome?** For a repetition code with nonorthogonal qubit flags, one. A streaming instrument fuses the flags as they arrive. After the syndrome, the retained qubit and a classical index give the same minimum logical error as a collective measurement that waits with all the flags.

In a four-site example with independent bit flips of probability $`1/4`$ and flag overlap $`0.99`$, any joint measurement that keeps only classical information before the syndrome has logical error more than $`2.5\times10^{-6}`$ above the delayed optimum. The ideal full-record and streaming error is approximately $`0.1225991921`$. The certified streaming advantage survives an independent final phase flip of probability up to $`1.9\times10^{-5}`$.

| Question | Result |
| --- | --- |
| What is sufficient for an arbitrary-length repetition block? | One persistent qubit, a classical index and one fusion per flag after the first |
| Can a purely classical record match it? | It cannot attain the ideal optimum in the biased four-flag example. At equal priors a collective early measurement can attain the optimum. |
| What changes for a binary linear syndrome $`Hx=s`$? | $`k=\dim\ker H`$ coherent qubits preserve every conditional decision. They are necessary for a fixed early instrument that must work for all priors on a syndrome class with a nonconstant decision label. |

## Read the science

- [Model and exact recovery objective](science/model.md) defines the flag channel, the syndrome cut and the full-record benchmark.
- [Streaming decoder](science/streaming-decoder.md) gives the two-flag fusion instrument and its physical workspace.
- [Early readout](science/early-readout.md) proves the finite joint-measurement gap and the exponent for adaptive single-flag measurements.
- [Noise](science/noise.md) gives finite and asymptotic results for phase flips in the accumulator and a separate bound on arbitrary gate deviations.
- [Linear syndromes](science/linear-syndromes.md) extends the construction and proves the memory lower bound for all-prior sufficiency.

The finite results assume known pure flag states, a classical distribution of Pauli bit flips and an exact, delayed syndrome. The full zero-memory collective error exponent and the minimum memory for a single fixed prior with several logical labels remain open. The [related work](references/RELATED_WORK.md) explains the connections to state discrimination, quantum belief propagation and decoder flags.

## Learn the project

John Watrous’s *The Theory of Quantum Information* (2018) is the educational anchor. The [Watrous bridge](learning/WATROUS_BRIDGE.md) links the textbook measurements and channels to the decoder. The [30 milestones](learning/MILESTONES.md) lead from the two-state test to the linear-syndrome construction. The [LLM guide](llms.txt) points to exact scientific and educational routes.

## Reproduce the finite checks

From the repository root, run:

```bash
python3 verification/run_all.py
```

The checks use only the Python standard library. They verify the fusion probabilities and overlaps, reproduce the four-flag witness and certify the stated finite dephasing tolerance. The [verification guide](verification/README.md) gives the expected results and their scope.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
