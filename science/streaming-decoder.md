# A streaming decoder with one qubit of memory

The decoder fuses each new flag into a one-qubit accumulator. It retains a classical index that identifies the error bit encoded in the accumulator's phase. The index can change during fusion, while the state overlap multiplies at every step. The syndrome later relates the selected bit to the required logical correction.

## Two flags in, one flag out

Write the two pure input flags in the amplitude basis used in the [model](model.md). For two unknown sign bits $x,y$, the coefficient of a two-bit basis vector $z=(z_1,z_2)$ is $a_z(-1)^{xz_1+yz_2}$, with $a_z>0$ independent of the signs. Define the even and odd sets $E=\{00,11\}$ and $O=\{01,10\}$ and their masses $A=\sum_{u\in E}a_u^2$ and $B=\sum_{v\in O}a_v^2$. Both masses are positive. If the incoming overlaps are $d$ and $c$, then $A+B=1$ and $A-B=dc$.

Choose any fixed coupling $w_{uv}$ whose even marginal is $a_u^2/A$ and odd marginal is $a_v^2/B$. Independent sampling of the two marginals is one explicit choice. Each coupling entry specifies an outcome with Kraus operator

```math
K_{uv}=\sqrt{w_{uv}}\left(
    \frac{\sqrt A}{a_u}|0\rangle\langle u|
   +\frac{\sqrt B}{a_v}|1\rangle\langle v|\right).
```

The cross terms in $K_{uv}^\dagger K_{uv}$ vanish because the output labels are orthogonal. Summing its even diagonal entry over $v$ gives one, and summing its odd entry over $u$ gives one. Thus this is a trace-preserving instrument with a classical outcome and a one-qubit output.

An outcome $(u,v)$ has probability $w_{uv}$ for every input sign pair. After removing a global phase, it leaves

```math
\sqrt A\,|0\rangle
   +(-1)^{(x,y)\cdot(u\oplus v)}\sqrt B\,|1\rangle.
```

The string $u\oplus v$ has odd parity. On two bits this selects exactly one input coordinate. The outcome thus tells the decoder which input sign the new flag carries without giving away that sign. The two possible outputs have overlap $A-B=dc$.

## Streaming, then correcting

1. Set the accumulator to the first flag and set the retained index to one.
2. Fuse with each subsequent flag. Update the retained index when the selected coordinate is the new flag. Its overlap is the product of the overlaps processed so far.
3. Receive the syndrome $s$. Compute the bit of $r_s$ at the retained index. Use it to identify which accumulator state corresponds to $r_s$.
4. Apply the binary Holevo–Helstrom measurement with the known conditional priors and return the indicated Pauli correction.

The classical fusion outcome law is independent of the entire error string, so conditioning on the retained index leaves the priors intact. Each original candidate pair and its compressed pair have the same Gram matrix after a known phase convention. Equivalently, there is an isometry between the two candidate spans after the syndrome is known. Therefore the last measurement achieves exactly the full-record optimum for every possible prior, rather than only preserving the average optimum for a specific distribution.

## Resources and implementation

The decoder consumes $n$ flags through $n-1$ fusions and holds one qubit across the syndrome cut. Only one classical coordinate index is retained, requiring $\lceil\log_2 n\rceil$ bits. A known schedule supplies the overlaps, which can also be computed by multiplying online. The four possible fusion outcomes fit in two meter bits. A finite-dimensional implementation uses the isometry $\sum_{uv}|uv\rangle K_{uv}$ from two input qubits into three qubits, followed by measuring two meter qubits. A unitary dilation therefore needs one fresh auxiliary qubit in addition to the incoming flag and accumulator. No two fusion gates have to be live at once. This is an ideal circuit model with calibrated overlaps and controls.

Keeping all $n$ flags is a matched benchmark for logical failure. Forcing a fully classical record before the syndrome is a separate benchmark. Its loss for a four-site biased example is established by an [explicit incompatibility certificate](early-readout.md).
