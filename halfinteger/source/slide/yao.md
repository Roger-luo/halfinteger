---
title: 幺
# subtitle: Roger's Fine Slide Generator
description: Extensible, Efficient Framework for Quantum Algorithm Design for Humans.
author: Roger

markdown:
  extensions:
  # more pymdownx extensions here:
  # https://facelessuser.github.io/pymdown-extensions/
    - pymdownx.magiclink
    - pymdownx.tasklist

reveal:
    theme: 'white'
    # full configuration see:
    # https://github.com/hakimel/reveal.js#configuration
    config:
        transition: 'fade'
...

---
background:
    image: ''
    color: black
...

[![幺](https://quantumbfs.github.io/Yao.jl/latest/assets/logo-light.svg){: style="margin: 0; border: none; box-shadow: none; background: none;" width=200 height=200}](https://github.com/QuantumBFS/Yao.jl)

#### **Extensible**{: style='color: #CD5C5C'} **Efficient**{: style='color: orange'} **Quantum Algorithm Design**{: style='color: #26d2a4'} for Humans.

---

[rogerluo.me](http://rogerluo.me)

![](/media/rogerluo-slide.png){: style="border: 0; box-shadow: none" height=500}

---

### Install Julia:

official compiler: [julialang.org/downloads](https://julialang.org/downloads/)

julia pro (annaconda for julia): [juliacomputing.com](https://juliacomputing.com/products/juliapro.html)

---

Install our package:

lastest:

```julia
julia> Pkg.clone("https://github.com/QuantumBFS/Yao.jl.git")
```

stable:

```julia
julia> Pkg.add("Yao")
```

---
note: "I will introduce the basics of quantum computing first, and then we will explore our recent package Yao."

background:
  image: "/media/qc-background.png"
  size: contain
  color: transparent
...

**Quantum Computing**

---
...

**Potential Applications for Near Term Small Quantum Computers**:

- Quantum Chemistry
- Quantum Co-Processor
- Secret Sharing
- Machine Learning

*Ref: [Technical Roadmap for Fault-Tolerant Quantum Computing](https://www.nqit.ox.ac.uk/sites/www.nqit.ox.ac.uk/files/2016-11/NQIT%20Technical%20Roadmap.pdf)*{: .fragment style="font-size: 16px"}

---
note: "perhaps the most promising application at the moment. Even after all the recent progress in classical algorithms for chemistry, some molecules exhibit what is known as 'strong correlation', which in practice means that conventional methods fail to yield reliable solutions for them in reasonable time. This is because available approximations normally rely on having very weak correlations. Some recent proof-of-concepts experiments have already been shown on a five"
...

**Quantum Chemistry**

![](/media/variational-quantum-eigensolver.png){: style="border: 0; box-shadow: none" height=400}

**O’Malley, P. J. J., et al. "Scalable quantum simulation of molecular energies." Physical Review X 6.3 (2016): 031007.**{: style="font-size: 16px"}

---
note: "small quantum co-processors can simulate a lager quantum computer, we can use the resources of a small quanutm computer with n qubits, to simulate (on a classical computer) a quantum computer with n+k qubits, with classical resources taht only scale exponentially with k rather than n+k. Besides, we can also simulate physical systems like a Hubbard model."
...

**Quantum Co-processor**

![](/media/trotter-step.png){: style="border: 0; box-shadow: none" height=400}

**Kreula, Juha M., et al. "Few-qubit quantum-classical simulation of strongly correlated lattice fermions." EPJ Quantum Technology 3.1 (2016): 11.**{: style="font-size: 16px"}

---
note: "Quantum devices can be used to accelerate machine learning tasks. But acceleration is not the only thing. Quantum based models may have
better representation power comparing to classical models."
...

**Machine Learning**

![](/media/xanadu-chips.png){: style="border: 0; box-shadow: none" height=400}

**Xandadu AI, Quantum Machine Learning 1.0**{: style="font-size: 16px"}

---
note: "e.g. It is proved by Xun Gao in his recent paper that their quantum generative model is exponentially more powerful comparing to represent probability distributions compared with classical generative models and has exponential speedup in training and inference at least for some instances under a reasonable assumption in computational complexity theory"
...

![](/media/QGM.png){: style="border: 0; box-shadow: none" height=400}

**Gao, Xun, Zhengyu Zhang, and Luming Duan. "An efficient quantum algorithm for generative machine learning." arXiv preprint arXiv:1711.02038 (2017).**{: style="font-size: 16px"}

---
note: "moreover, near term noisy quantum devices may be used for machine learning directly. Recently, a new modeled called Quantum Circuit Born Machine is proposed."
...

![](/media/QCBM.png){: style="border: 0; box-shadow: none" height=300}
![](/media/QCL.png){: style="border: 0; box-shadow: none" height=300}

**Liu, Jin-Guo, and Lei Wang. "Differentiable learning of quantum circuit Born machine." arXiv preprint arXiv:1804.04168 (2018).**{: style="font-size: 16px"}

**Mitarai, Kosuke, et al. "Quantum circuit learning." arXiv preprint arXiv:1803.00745 (2018).**{: style="font-size: 16px"}

---

**Quantum Computing is Approaching**

---
note: "Quantum computing is approaching in recent years."
...

![](/media/QC-is-near.JPG){: style="border: 0; box-shadow: none" height=500}

**Source: © By Thomas A. Campbell, Ph.D., FutureGrasp, LLC**{: style="font-size: 16px;"}

---
note: "this is the roadmap for quantum computing"
...

![roadmap](/media/roadmap-qc.jpg){: style="border: 0; box-shadow: none" height=500}

**J. Ignacio Cirac & H. Jeff Kimble. "Quantum optics, what next?" Nature Photonics volume 11, pages 18–20 (2017).**{: style="font-size: 16px"}

---
note: "Google/IBM/Intel is approach quantum advantage"
...

![Google](/media/google-chips.png){: style="border: 0; box-shadow: none" height=200}
![IBM](/media/IBM-CES.jpeg){: style="border: 0; box-shadow: none" height=200}

**Source: © By Nick Summers, engadget / Google AI lab**{: style="font-size: 16px;"}

---
note: "In near term future, the resources of quantum computing will still be limited, like the early stage, classical algorithm was designed
on papers. We have to design new quantum algorithms and explore when quantum computers is better with classical simulation. However, simulating
quantum computing on classical devices is hard due to its quantum nature. There are a lot of optimized classical algorithms for simulating a small
set of quantum circuits efficiently. Moreover, in the future, researchers may want to immigrate their classical simulated algorithms directly to quantum devices. However, we also hope researchers can focus on their own algorithms rather than backend details. Therefore, we need a framework that is highly extensible but easy to use. And here comes the Yao framework."
...

## What is 幺？

幺(Yao) is a **Extensible**, **Efficient** framework for quantum algorithm design.

---
note: "Let's explore the quantum computing with a few demos with Yao."
...

## What can 幺 do?


---
note: "I will now introduce some basics about quantum computing"
...

**Quantum Computing: Basics**

---
note: ""
...

**Review: Linear Algebra**

---

**Matrix Vector Multiplication**

$$
\begin{pmatrix}
a & b\\
c & d
\end{pmatrix}
\begin{pmatrix}
x \\
y
\end{pmatrix} =
\begin{pmatrix}
ax + by \\
cx + dy
\end{pmatrix}
$$

---

**Matrix Matrix Multiplication**

$$
\begin{pmatrix}
a & b\\
c & d
\end{pmatrix}\begin{pmatrix}
w & x\\
y & z
\end{pmatrix} = \begin{pmatrix}
aw + by & ax + bz\\
cw + dy & cx + dz
\end{pmatrix}
$$

---

**Identity Matrix**

$$
I\cdot \begin{pmatrix}
a\\
b\\
c\\
d
\end{pmatrix} = \begin{pmatrix}
1 & 0 & 0 & 0\\
0 & 1 & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 0 & 0 & 1\\
\end{pmatrix}\begin{pmatrix}
a\\
b\\
c\\
d
\end{pmatrix} = \begin{pmatrix}
a\\
b\\
c\\
d
\end{pmatrix}
$$

---

**Swap Matrix**

$$
\begin{pmatrix}
1 & 0 & 0 &0\\
0 & 0 & 1 &0\\
0 & 1 & 0 &0\\
0 & 0 & 0 &1
\end{pmatrix}\begin{pmatrix}
0\\
1\\
0\\
0
\end{pmatrix} = \begin{pmatrix}
0\\
0\\
1\\
0
\end{pmatrix}
$$

---
note: "tensor product of vectors"
...

$$
\begin{pmatrix}
x_0 \\
x_1
\end{pmatrix}\otimes\begin{pmatrix}
y_0 \\
y_1
\end{pmatrix} = \begin{pmatrix}
x_0 \begin{pmatrix}
y_0\\
y_1
\end{pmatrix} \\
x_1 \begin{pmatrix}
y_0\\
y_1
\end{pmatrix}
\end{pmatrix} = \begin{pmatrix}
x_0 y_0 \\
x_0 y_1 \\
x_1 y_0 \\
x_1 y_1
\end{pmatrix}
$$

---
note: "representing multiple classical bits"
...

$$
|00\rangle = \begin{pmatrix}
1\\
0
\end{pmatrix} \otimes \begin{pmatrix}
1\\
0
\end{pmatrix} = \begin{pmatrix}
1\\
0\\
0\\
0
\end{pmatrix}
$$

---

$$
|10\rangle = \begin{pmatrix}
0\\
1
\end{pmatrix} \otimes \begin{pmatrix}
1\\
0
\end{pmatrix} = \begin{pmatrix}
0\\
0\\
1\\
0
\end{pmatrix}
$$

---

$$
|01\rangle = ?
$$

---
note: "You can try what is the vector form of 1 with Yao."
...

**Try this**

```julia
register(bit"01") |> statevec
```

---
note: "The matrix form of classical bit operations is actually called the truth table."
...

| name     | function        | matrix                                      |
|:---------|:----------------|:--------------------------------------------|
| Identity | $f(x) = x$      | $\begin{pmatrix} 1 & 0\\0 & 1\end{pmatrix}$ |
| Negation | $f(x) = \neg x$ | $\begin{pmatrix} 0 & 1\\1 & 0\end{pmatrix}$ |
| Const-0  | $f(x) = 0$      | $\begin{pmatrix} 1 & 1\\0 & 0\end{pmatrix}$ |
| Const-1  | $f(x) = 1$      | $\begin{pmatrix} 0 & 0\\1 & 1\end{pmatrix}$ |

---

**Negation**

```julia
with!(X, register(bit"0")) |> statevec
```

---

**Operations on multiple Bits: CNOT**

$$
\begin{pmatrix}
1 & 0 & 0 & 0\\
0 & 1 & 0 & 0\\
0 & 0 & 0 & 1\\
0 & 0 & 1 & 0
\end{pmatrix}
$$

---

**Try**

```julia
g = control(2, [1, ], 2=>X)
```

```julia
with!(g, register(bit"10")) |> statevec

with!(g, register(bit"00")) |> statevec
```

---

## quantum bits

---
note: "In fact, what we used for classical bits are a special case of quantum bits. For the classical case,
the state vector is only a one-hot vector. However, in quantum case, this vector can be any normalized complex
valued vector, or the so-called a vector in Hilbert space. Or in quantum physics this is called a quantum state.
As you see, this generalized representation of the state of a bit can have a value that is not 0 or 1. In fact they
will have some possibility to have value 0 and 1, the possibility is the square norm of each element."
...

$$
\begin{pmatrix}
\frac{1}{\sqrt{2}}\\
\frac{1}{\sqrt{2}}
\end{pmatrix}\quad
\begin{pmatrix}
\frac{-1}{\sqrt{2}}\\
\frac{1}{\sqrt{2}}
\end{pmatrix}\quad
\begin{pmatrix}
im\\
0
\end{pmatrix}
$$

---
note: "It will collapse to one of the state if you measure it."
...

construct a quantum bit: $\frac{|0000\rangle + |1111\rangle}{\sqrt{2}}$

```julia
r = register(bit"0000") + register(bit"1111")
normalize!(r)
```

Then measure it:

```julia
measure(r, 5)
```

---
note: "such a single qubit can be described by a point on a sphere, since we have the constrain"
...

We have constrain:

$$
||a||^2 + ||b||^2 = 1 \Rightarrow \begin{pmatrix}
cos(\frac{\theta}{2})\\
e^{im\phi} sin(\frac{\theta}{2})
\end{pmatrix}
$$

![Bloch-sphere](/media/bloch-sphere.jpg){: style="border: 0; box-shadow: none" height=200}

---
note: "now we have quantum bits, which is called qubits, then how about a quantum gate. The Negation stays, however
since we are using a complex vector now, we will have some operations on other direction."
...

| name         | matrix                                         |
|:-------------|:-----------------------------------------------|
| Identity     | $\begin{pmatrix} 1 & 0\\0 & 1\end{pmatrix}$    |
| X (Negation) | $\begin{pmatrix} 0 & 1\\1 & 0\end{pmatrix}$    |
| Y            | $\begin{pmatrix} 0 & -im\\im & 0\end{pmatrix}$ |
| Z            | $\begin{pmatrix} 1 & 0\\0 & -1\end{pmatrix}$   |

---

**Try them see what happens**

```julia
r = register(bit"0000") + register(bit"0000")
normalize!(r)
apply!(r, X)
```

---
note: "now we know the basics of qubits and quantum gates. Let's explore what is a quantum circuit and algorithms with some demos."
...

### Demo 1: Preparing GHZ state

---

A GHZ state is a quantum state looks like:

$$
\frac{|0\cdots 0\rangle - |1\cdots 1\rangle}{\sqrt{2}}
$$

We will use a quantum circuit to prepare a GHZ state from $|0\cdots 0\rangle$

---

![GHZ-Circuit](https://quantumbfs.github.io/Yao.jl/latest/assets/figures/ghz4.png){: style="border: 0; box-shadow: none" height=500}

---
note: "kron block will use kronecker product to calculate multiple blocks vertical distributed in a quantum circuit"
...

![GHZ-Circuit](https://quantumbfs.github.io/Yao.jl/latest/assets/figures/ghz4.png){: style="border: 0; box-shadow: none" height=200}

```julia
circuit = chain(
    4,
    kron(i==1?i=>X:i=>H for i in 1:4),
    control([2, ], 1=>X),
    control([4, ], 3=>X),
    control([3, ], 1=>X),
    control([4, ], 3=>X),
    kron(i=>H for i in 1:4),
)
```

---
note: "you can use help mode in the REPL to check the documents, or just search it on the website."
...

```julia
help?> X

  X

  The Pauli-X gate acts on a single qubit. It is the quantum equivalent of the NOT gate
  for classical computers (with respect to the standard basis |0\rangle, |1\rangle). It
  is represented by the Pauli X matrix:

X = \begin{pmatrix}
0 & 1\\
1 & 0
\end{pmatrix}
```

---
note: "you can define a default register on CPU with register method, we support bit string literals."
...

Define initial state of a quantum register: $|0000\rangle$

```julia
julia> r = register(bit"0000")
```

---
note: "Then let's apply the circuit to the register, we provide two methods to make sure this operation is safe."
...

You can define how to apply several blocks inside a context with julia's **do** block:

```julia
# creates a new register
new = with(r) do r
  r |> kron(i==1?i=>X:i=>H for i in 1:4)
  r |> control([2, ], 1=>X) |> control([4, ], 3=>X)
  r |> control([3, ], 1=>X) |> control([4, ], 3=>X)
  r |> kron(i=>H for i in 1:4)
end

# apply blocks in-place
with!(r) do r
  r |> kron(i==1?i=>X:i=>H for i in 1:4)
  r |> control([2, ], 1=>X) |> control([4, ], 3=>X)
  r |> control([3, ], 1=>X) |> control([4, ], 3=>X)
  r |> kron(i=>H for i in 1:4)
end
```

---
note: "Or for convenient you can also simply input a block as the first argument"
...

Or use a wrapped quantum circuit.

```julia
# creates a new register
new = with(circuit, r)
# in-place
with!(circuit, r)
```

---
note: "let's measure the result for 1000 times to see what happens, the GHZ state will collapse to 0000 or 1111 when you measure it!"
...

```julia
using PyPlot
plt[:hist](measure(r, 1000))
```
![](/media/GHZ.png){: style="border: 0; box-shadow: none" height=400}

---
note: "In Yao, you can directly know what your program do from what you write, e.g previously, we use kronecker product
to calculate some Hadamard gates vertically. However, there are other ways to do this more efficiently, e.g"
...

```julia
kronecker = kron(4, 1=>X, H, H, H)
roller = roll(4, 1=>X, H, H, H)
```

```julia
julia> using BenchmarkTools

julia> @benchmark with!(roller, $(register(bit"0000")))
BenchmarkTools.Trial:
  memory estimate:  4.80 KiB
  allocs estimate:  55
  --------------
  minimum time:     2.328 μs (0.00% GC)
  median time:      2.428 μs (0.00% GC)
  mean time:        2.990 μs (12.86% GC)
  maximum time:     288.347 μs (94.90% GC)
  --------------
  samples:          10000
  evals/sample:     9
```

---
note: "In Yao, we provide various composite blocks like kron & roll to let you do whatever you want. And you can even easily
extend the whole block system to meet your own needs if you want."
...

```julia
julia> @benchmark with!(kronecker, $(register(bit"0000")))
BenchmarkTools.Trial:
  memory estimate:  18.55 KiB
  allocs estimate:  120
  --------------
  minimum time:     47.241 μs (0.00% GC)
  median time:      51.462 μs (0.00% GC)
  mean time:        56.150 μs (3.51% GC)
  maximum time:     2.768 ms (95.15% GC)
  --------------
  samples:          10000
  evals/sample:     1
```

---
note: "roll will rotate the tensor form of a quantum state and directly contract it with a quantum gate."
...

![](/media/roller.svg){: style="border: 0; box-shadow: none" height=300}

```julia
roller = roll(4, 1=>X, H, H, H)
```

---
note: "Quantum Circuit Born Machine is a recent progress on quantum machine learning, it treats quantum computing devices
as a new computation resources, and is able to be applied on near term noisy quantum computers. The training of a quantum
circuit born machine is similar to training a neural network, they both requires gradient and optimizers"
...

### Demo 2: Quantum Circuit Born Machine

---

Please open the notebook

```julia
julia> using IJulia

julia> notebook(joinpath(Pkg.dir("Yao"), "examples"))

```

---
note: "We provide hierarchical APIs that give developer freedom of extending Yao.

1. We extended the Julia's SparseArrays, which will be contributed to upper stream.
2. Thanks to Julia's multiple dispatch feature, we are able to optimize operator's
  performance with extensions, which means you can choose different optimization
  strategy by using different extensions.
3. We also provide some buildin optimization made by the Boost extension."
...

### Hierarchical APIs

![structre](https://quantumbfs.github.io/Yao.jl/latest/assets/figures/framework.png){: style="border: 0; box-shadow: none" height=450}

---
note: "we compare our performance to ProjectQ, a python effort that is able to simulate up to 45 qubits. With optimization
 done by the boost extension. We have much better performance on small circuit simulation and similar performance with large
 circuit simulation. The Q-X is ProjectQ and the Y-X is Yao."
...

![bench-xyz](https://quantumbfs.github.io/Yao.jl/latest/assets/benchmarks/xyz-bench.png){: style="border: 0; box-shadow: none" height=300}
![bench-rxyz](https://quantumbfs.github.io/Yao.jl/latest/assets/benchmarks/rot-bench.png){: style="border: 0; box-shadow: none" height=300}

---
note: "All of our optimized blocks gain better performance."
...

![bench-cxyz](https://quantumbfs.github.io/Yao.jl/latest/assets/benchmarks/cxyz-bench.png){: style="border: 0; box-shadow: none" height=300}
![bench-repeatxyz](https://quantumbfs.github.io/Yao.jl/latest/assets/benchmarks/repeatxyz-bench.png){: style="border: 0; box-shadow: none" height=300}

---
note: "Although un-optimized blocks does not as good as ProjectQ's for large number of qubits, but because of our hierarchical APIs and multiple
dispatch, fine-grained optimization can be easily done and dispatched to certain type of circuits without any overheads."
...

![bench-toffoli](https://quantumbfs.github.io/Yao.jl/latest/assets/benchmarks/toffoli-bench.png){: style="border: 0; box-shadow: none" height=300}
![bench-crot](https://quantumbfs.github.io/Yao.jl/latest/assets/benchmarks/crot-bench.png){: style="border: 0; box-shadow: none" height=300}


---
note: "Let's explore more about Yao's block system"
...

### Flexible Block System

---
note: "every component in a quantum circuit is a block. A block is like a quantum program, it is made up by one or more quantum operators. CompositeBlocks are blocks that contains other blocks. Primitive blocks are the immutable elements that will not contain any other blocks.
constant gates are blocks that binds to a constant in memory. It will not allocate any extra memory no matter how many constant gates you have.
In general, each different block type represents a different theoretical concepts or a different approach of simulation/calculation.
You can easily extending this block tree by defining your own block type.
"
...

![block tree](/media/block_tree.svg){: style="border: 0; box-shadow: none" height=700}

---
note: "Yao make use of Julia's multiple dispatch, extending a new block in the block tree can be extremely simple."
...

### Make use of Multiple Dispatch

---
note: "normally, a block's behavior can be defined with only by its matrix form. But sometimes, since we know how to apply it to
a quantum state directly. We can also define how it will applies."
...


1.the matrix form
{: .fragment}

2.how to apply on a quantum state
{: .fragment}

---
note: "for constant gates, we provide macros that will help you do the code generation.
  Try this command, it will automatically generate a new constant gate type for you. There is no difference
  between user defined constant blocks and builtin constant blocks"
...

```julia
julia> @const_gate MyConstGate = ComplexF64[0.5 0;-0.2 0.2]
```

```julia
function apply!(r::AbstractRegister, g::MyConstGate)
  # some better way to apply
  # this operator to quantum register
  r
end
```

---
note: "for primitive blocks, you have to define your own block type by subtyping PrimitiveBlock. And import methods
you will need to overload."
...

```julia
using Yao, Yao.Blocks # use 3rd hierarchy API: Blocks

import Yao.Blocks: mat, dispatch!, parameters # this is the mimimal methods you will need to overload

mutable struct NewPrimitive{T} <: PrimitiveBlock{1, T}
   theta::T
end
```

---
note: "Then define its matrix form."
...

```julia
mat(g::NewPrimitive{T}) where T = Complex{T}[sin(g.theta) 0; cos(g.theta) 0]
```

---
note: "Yao will use this matrix to do the simulation by default. However, if you know how to directly apply your block to a quantum register, you can also overload apply! to make your simulation become more efficient. But this is not required."
...

```julia
import Yao.Blocks: apply!
apply!(r::AbstractRegister, x::NewPrimitive) = # some efficient way to simulate this block
```

---
note: "Third If your block contains parameters, declare which member it is with dispatch! and how to get them by parameters"
...

```julia
dispatch!(g::NewPrimitive, theta) = (g.theta = theta; g)
parameters(x::NewPrimitive) = x.theta
```

---
note: "The prototype of dispatch! is simple, just directly write the parameters as your function argument. e.g if you have this type"
...

```julia
mutable struct MultiParam{N, T} <: PrimitiveBlock{N, Complex{T}}
  theta::T
  phi::T
end
```

just write

```julia
dispatch!(x::MultiParam, theta, phi) = (x.theta = theta; x.phi = phi; x)
```


---
note: ""
...

### Low abstraction

---
note: "our interface is low abstract, this will let you be aware of what you are doing. This is nice because explicit is always better
then implicit."
...

**Each block represents a different approach of calculation**

---

- `kron` -> **kronecker product**
- `roll` -> **reshape & roll dims**
- `repeat` -> **repeat a block on given lines**

---

### ROADMAPs

- More fine-tuned optimizations
- GPU support
- Special register states support: Stabilizers, MPS, etc.
- real quantum devices acceleration (like GPUs)

---

**Follow us on Github**: [Yao.jl](https://github.com/QuantumBFS/Yao.jl)
