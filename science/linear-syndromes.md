# Delayed binary linear syndromes

Let the flag at site $`i`$ be

```math
|\psi_{x_i}\rangle=\sqrt{1-q_i}|0\rangle+(-1)^{x_i}\sqrt{q_i}|1\rangle,
\qquad q_i=\frac{1-c_i}{2}, \qquad 0\lt c_i\lt 1.
```

The unknown error string is $`x\in\mathbb F_2^n`$. The receiver consumes the flags one at a time and learns $`s=Hx`$ after the last flag, where $`H`$ is a known binary matrix. Put $`C=\ker H`$ and $`k=\dim C`$.

There is a single early instrument, independent of the syndrome and the error prior, that retains at most $`k`$ qubits plus a classical record. After $`s`$ is supplied, the receiver attains the full-record optimum for every prior and every decision loss defined on the error strings in that syndrome class. If the same instrument must preserve optimal exact-label decisions for every prior, $`k`$ qubits are necessary as soon as the target label takes at least two different values in one syndrome class. This lower bound applies to arbitrary joint early operations. For full error identification, priors supported on pairs already certify it.

## Track the characters of the kernel

Choose an $`n\times k`$ binary matrix $`G`$ whose columns form a basis of $`C`$. The $`i`$th row, written as a column, is $`h_i\in\mathbb F_2^k`$. Let $`V_i=\operatorname{span}(h_1,\ldots,h_i)`$ and $`k_i=\dim V_i`$, with $`V_0=\{0\}`$.

In the computational basis the product flag has amplitude $`\sqrt{p(z)}(-1)^{z\cdot x}`$ at $`z\in\mathbb F_2^n`$, where $`p(z)`$ is the probability of a string of independent bits with $`\Pr(z_i=1)=q_i`$. At fixed $`s`$, choose a representative $`r_s`$ with $`Hr_s=s`$. Write $`x=r_s+Gv`$. The sign at $`z`$ factors as

```math
(-1)^{z\cdot x}=(-1)^{z\cdot r_s}(-1)^{(G^{\mathsf T}z)\cdot v}.
```

All basis strings with the same $`G^{\mathsf T}z`$ thus carry the same character of $`v`$. Their other phases depend on the still-unknown $`r_s`$.

For the first $`i`$ flags define the character distribution

```math
P_i(a)=\Pr\left(\sum_{j=1}^i z_j h_j=a\right),
\qquad a\in V_i.
```

These probabilities are strictly positive on $`V_i`$. Start at $`P_0(0)=1`$ and set $`P_i(a)=(1-q_i)P_{i-1}(a)+q_i P_{i-1}(a+h_i)`$, extending $`P_{i-1}`$ by zero off $`V_{i-1}`$.

## The streaming instrument

After processing the first $`i`$ flags, the receiver retains the state

```math
|\chi_i(x)\rangle=
\sum_{a\in V_i}\sqrt{P_i(a)}\,(-1)^{m_a\cdot x_{1:i}}|a\rangle.
```

Here each mask $`m_a\in\mathbb F_2^i`$ is known from the classical record and satisfies $`\sum_{j=1}^i(m_a)_j h_j=a`$. At $`i=0`$ this is the state of a trivial register with the empty mask.

When flag $`i`$ arrives, a basis input $`z=(a',b)`$ consists of the old register label $`a'\in V_{i-1}`$ and new bit $`b\in\mathbb F_2`$. It maps to the character $`a=a'+b h_i`$. Its squared amplitude is

```math
w(z)=P_{i-1}(a')\big((1-q_i)^{1-b}q_i^b\big).
```

For each $`a\in V_i`$, let $`R_a(z)=w(z)/P_i(a)`$ on the group of inputs with character $`a`$. Each group contains one or two inputs. Its probabilities specify how the instrument should select a representative in that group.

Construct a single coupling of these selections. Use the same uniform number $`u\in[0,1)`$ for all groups. In a two-input group select the input with $`b=0`$ if $`u\lt R_a((a,0))`$, and select the input with $`b=1`$ otherwise. A one-input group selects its only input for every $`u`$. The distinct thresholds partition $`[0,1)`$ into at most $`|V_i|+1`$ nonempty intervals. Each interval $`t`$ has length $`\omega_t`$ and specifies one input $`z_t(a)`$ per group. It satisfies

```math
\sum_{t:z_t(a)=z}\omega_t=R_a(z).
```

The uniform number defines the coupling mathematically. To implement the coupling while preserving the character amplitudes, use the quantum instrument

```math
K_t=\sum_{a\in V_i}
  \sqrt{\frac{\omega_t}{R_a(z_t(a))}}\,|a\rangle\langle z_t(a)|.
```

For fixed $`t`$, distinct groups use distinct input basis labels and have orthogonal outputs. Thus $`K_t^\dagger K_t`$ is diagonal. For each input $`z`$ its diagonal entries sum to one by the marginal identity, proving $`\sum_t K_t^\dagger K_t=I`$ on the input register. Applying $`K_t`$ gives amplitude magnitudes $`\sqrt{\omega_t P_i(a)}`$. If $`z_t(a)=(a',b)`$, the new mask for $`a`$ is the old mask for $`a'`$ followed by $`b`$. The outcome distribution is exactly $`\omega_t`$ for every $`x`$ and for every previous record. The normalized output has the required form for the next step.

If $`h_i`$ is independent of the previous rows, each group has one member and the step is a basis relabeling with no meter outcome. If $`h_i=0`$, the flag contains no information about $`v`$. The receiver can discard it and append zero to every mask. The same formula covers the other rank-preserving steps.

## Use the syndrome to finish the measurement

After the cut, compute $`r_s`$ and multiply each basis state $`|a\rangle`$ by $`(-1)^{m_a\cdot r_s}`$. The corrected state is independent of the meter record:

```math
|\phi_v\rangle=\sum_{a\in V_n}\sqrt{P_n(a)}\,(-1)^{a\cdot v}|a\rangle.
```

For any two members $`x=r_s+Gv`$ and $`x'=r_s+Gv'`$ of the syndrome class, orthogonality of the character basis gives

```math
\langle\phi_v|\phi_{v'}\rangle
=\sum_{a\in V_n}P_n(a)(-1)^{a\cdot(v+v')}
=\prod_{i:(G(v+v'))_i=1}c_i
=\left\langle\bigotimes_i\psi_{x_i}\,\middle|\,\bigotimes_i\psi_{x'_i}\right\rangle.
```

The middle equality uses independence of the bits $`z_i`$ and $`1-2q_i=c_i`$. Equality of Gram matrices gives an isometry from the compressed states to the span of the full flag states in that class. Pull back any full-record decision POVM along this isometry. This preserves its entire conditional decision distribution. Since $`V_n=\mathbb F_2^k`$ and every $`P_n(a)\gt 0`$, the columns of the character matrix weighted by $`\sqrt{P_n(a)}`$ are linearly independent, so this span has dimension $`2^k`$.

For stochastic $`X`$ errors in a CSS code with the stated flag and syndrome interface, the same isometry preserves the optimum among flag-based decisions on the logical $`X`$ class. That task groups error strings by their stabilizer equivalence within the known syndrome class. Pulling back the full-string experiment preserves those coarser decisions and their risk.

## Resource accounting

| Resource | Upper bound in the ideal model |
| --- | --- |
| Persistent quantum register | $`k_i`$ qubits after flag $`i`$, hence at most $`k`$ |
| Streaming steps | $`n`$ consumed flags, with exactly $`k`$ rank-increasing relabelings and at most $`n-k`$ nontrivial fusions |
| Classical record across the cut | At most $`\sum_{i:k_i=k_{i-1}}(k_i+1)\le(n-k)(k+1)`$ bits when retaining interval indices |
| Temporary quantum width | At most $`2k+1`$ qubits including the incoming flag and the meter. A rank-preserving step at rank $`k_i`$ uses at most $`k_i`$ fresh ancilla qubits |

The width follows by implementing the isometry $`|z\rangle\mapsto\sum_t K_t|z\rangle|t\rangle`$ and measuring the meter. At constant rank $`k_i`$ there are $`k_i+1`$ input qubits including the new flag. The output uses $`k_i`$ qubits plus a meter of at most $`k_i+1`$ qubits. A unitary extension uses the same physical workspace for inputs and outputs. A rank increase needs only the old register and the flag.

The receiver can keep an explicit table of masks using up to $`n2^k`$ bits. With interval indices, reconstruct each final mask after $`s`$ arrives. Start at its final character and walk backward through the chosen intervals. At step $`i`$, read the selected $`b`$, add $`b(r_s)_i`$ to the phase parity, and update the character to $`a+b h_i`$. The masks themselves never control a fusion. For fast lookup, the static description for one step can store the sorted thresholds, the rank of each group's threshold and the character labels. This requires $`O(2^{k_i})`$ table entries per step, in addition to the code description and known overlap parameters. The distribution recursion and threshold sorting require at most $`O(n(k+1)2^k)`$ real-arithmetic operations given the character labels and constant-time access to their indices.

The bounds count coherent width and meter records. They assume access to ideal controlled rotations from the known parameters. The finite gate count, gate approximation error, and implementation cost of the final conditional POVM depend on the control model and the decoding task. The construction can be used at small $`k`$ while a general final POVM still acts on a $`2^k`$-dimensional space.

## Why fewer than $`k`$ qubits cannot preserve every prior

Fix a syndrome class and let $`S`$ be the span of its product flag states. Any two distinct flag states $`|f\rangle`$ and $`|g\rangle`$ in this class are linearly independent and satisfy $`0\lt |\langle f|g\rangle|\lt 1`$. Fix the early instrument. Write its Kraus operators as $`K_{b,j}`$ from the flag space to a register of dimension $`d`$, with $`b`$ the retained classical outcome and $`j`$ an unobserved index. The optimal decision after the cut may condition on $`b`$ and the prior.

For two different positive prior ratios $`\lambda`$ and $`\mu`$, the optimal full-record binary tests are specified by the positive and negative eigenvectors of $`\lambda|f\rangle\langle f|-|g\rangle\langle g|`$ and $`\mu|f\rangle\langle f|-|g\rangle\langle g|`$. Each has one strictly positive and one strictly negative eigenvalue on $`S_{fg}=\operatorname{span}(f,g)`$. Their eigenprojectors fail to commute because the two weighted differences have a nonzero commutator on $`S_{fg}`$.

For either prior, let $`e_+,e_-`$ be the two sign eigenvectors and let $`0\le M_b\le I`$ be the effect for the positive decision after $`b`$. Optimality forces the pulled-back effect to have expectation one on $`e_+`$ and zero on $`e_-`$. The upper and lower bounds on $`M_b`$ then imply

```math
M_b K_{b,j}e_+=K_{b,j}e_+,
\qquad M_b K_{b,j}e_-=0
```

for every $`b,j`$. The images of $`e_+`$ and $`e_-`$ belong to orthogonal eigenspaces of the same Hermitian effect. Therefore the compression of $`K_{b,j}^\dagger K_{b,j}`$ to $`S_{fg}`$ is diagonal in the sign basis of this prior. Repeat for the second prior. A Hermitian operator on a two-dimensional space that is diagonal in both of these noncommuting bases is scalar.

For full error identification this scalar is the same for every pair in the syndrome class. Pairs sharing $`f`$ give the same value $`\|K_{b,j}f\|^2`$, and all pairs are linked through shared endpoints. Thus every matrix element of $`K_{b,j}^\dagger K_{b,j}`$ between class vectors equals the same scalar times their inner product. The class vectors span $`S`$, so $`K_{b,j}`$ restricts to a scaled isometry on $`S`$. Trace preservation guarantees a nonzero scale for at least one Kraus term. Hence $`d\ge\dim S=2^k`$. The conclusion is immediate when $`k=0`$.

For a coarser target label, apply the pair argument first to error strings with different labels. This still gives a common scale for fixed $`b,j`$, because every pair of strings with the same label is linked through any string with a different label. Consider two distinct full flag states $`f_1,f_2`$ with the same label, and a state $`g`$ from a different label. In their three-dimensional span, let $`A`$ be the compression of $`K_{b,j}^\dagger K_{b,j}`$ minus the common scale times the identity. In the spanning basis $`(f_1,f_2,g)`$, the only potentially nonzero matrix elements of $`A`$ are $`\langle f_1|A|f_2\rangle`$ and its conjugate. If this element is nonzero, $`A`$ has rank two and its kernel is exactly the span of $`g`$.

Now use a prior supported equally on the three strings. The two-label decision has Helstrom difference proportional to

```math
|f_1\rangle\langle f_1|+|f_2\rangle\langle f_2|-|g\rangle\langle g|.
```

It has two positive eigenvalues and one negative eigenvalue on the triple span, by congruence with the diagonal sign matrix in the independent spanning basis. Its negative eigenvector $`e_-`$ has nonzero inner product with $`g`$, because the positive projectors alone have a nonnegative expectation. It is linearly independent from $`g`$, since applying the difference operator to $`g`$ gives nonzero components along $`f_1`$ and $`f_2`$ in the spanning basis. The same deterministic-sign argument gives $`A e_-=\alpha e_-`$ for some $`\alpha`$. Taking the inner product with $`g`$ gives $`\alpha=0`$ because $`A g=0`$. This contradicts the one-dimensional kernel whenever $`\langle f_1|A|f_2\rangle\ne 0`$. The same-label matrix element must vanish, completing the scaled-isometry proof for any nonconstant target label.

A continuous classical record obeys the same argument almost everywhere. In finite input and output dimensions its instrument has a positive Choi-matrix density with respect to the finite scalar measure given by the trace of its Choi measure. Use a measurable Kraus decomposition of that density. Zero integrals of the nonnegative decision errors give the deterministic-sign identities almost everywhere. The proof uses finitely many testing priors, which admit one common full-measure set, and trace preservation again gives a nonzero scale.

The sharpness condition uses one fixed early instrument across all priors. A decoder optimized for one prior need only preserve the corresponding optimal tests.

## Relation to prior compression methods

Piveteau and Renes group basis strings by linear images and uncompute conditional amplitudes in a specified subspace-decoding problem. The instrument above also groups by a linear image. Its coupled selections keep one representative from each group in every branch, allowing all affine phases to be restored once the syndrome arrives. See Definition 3.2 and Lemma 3.1 of [Efficient and optimal quantum state discrimination via quantum belief propagation](https://arxiv.org/html/2509.19441v1).

Koashi and Imoto describe compression of state families under a preservation requirement. The two-prior argument here starts from preservation of the binary decision values in each pair and derives the scaled-isometry condition on the full pure-state span. See [Operations that do not disturb partially known quantum states](https://doi.org/10.1103/PhysRevA.66.022318).
