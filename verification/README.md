# Reproduce the finite checks

From the repository root, run the following command with Python 3.10 or newer. The script uses only the standard library.

```sh
python verification/run_all.py
```

The script verifies completeness of the fusion instrument, the label-independent branch probabilities, and the phase carried by each branch. It then enumerates fusion histories and compares their aggregate minimum logical error with the error computed from the full product flags. The examples include unequal overlaps, correlated priors, an error string with zero prior, and a balanced case where an early collective measurement attains the optimum.

The four-flag benchmark uses independent bit-flip probability $p=1/4$ and single-flag overlap $c=0.99$.

| Quantity | Result |
|---|---:|
| Optimum using one retained qubit | $0.122599192080$ |
| Error of a feasible zero-memory policy | $0.126935131109$ |
| Absolute cross-Gram norm for the two witness syndromes | $1.101099216498$ |
| Certified excess error of every zero-memory policy | Greater than $2.5\times 10^{-6}$ |
| Final phase-flip probability covered by the strict separation | Up to $1.9\times 10^{-5}$ |

The zero-memory policy in the table fuses the flags and measures the final qubit in the $X$ basis before the syndrome arrives. Its error is an upper bound on the optimum with zero retained qubits. The script computes the cross-Gram norm independently from the flag amplitudes. It also checks the rational inequalities that certify the [early-readout lower bound](../science/early-readout.md) and the [phase-noise threshold](../science/noise.md).
