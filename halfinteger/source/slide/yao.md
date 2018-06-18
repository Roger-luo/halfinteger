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

![幺](https://rawgit.com/QuantumBFS/Yao.jl/master/docs/src/assets/logo-light.svg){: style="margin: 0; border: none; box-shadow: none; background: none;" width=200 height=200}

#### **Extensible**{: style='color: #CD5C5C'}, **Efficient**{: style='color: orange'} Framework for **Quantum Algorithm Design**{: style='color: #26d2a4'} for Humans.

---

**Available @** [rogerluo.me](http://rogerluo.me) -> click slides

or type

```
http://104.224.129.42/slides/
```

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
note: "classical computers have been doing great, however there are still problems that is hard for them. These problems includes:

1. optimization
2. chemistry & physics

In order to accelerate the computation of solving those problems, scientists have proposed various computing machines
and quantum computer is one of those promising approaches. Then, what is quantum computing?"
...

- optimization

---
note: "Let's imagine if you are managing a dinner tonight, and you have twenty attendees and four tables. Some attendees will start arguing
if they are arranged on the same table, and some attendees want to sit on the same table, and so on. They could have a lot requirements.
And you have to make them satisfied. Is there a solution that satisfies all the attendees? This is called the Satisfiability Problem"
...

![SAT](/media/attendees.jpg){: style="border: 0; box-shadow: none" height=450}

**How to satisfy them?**

---

![SAT](/media/Sat_reduced_to_Clique_from_Sipser.svg){: style="border: 0; box-shadow: none" height=450 width=450}

**Source: © Wikipedia**{: style="font-size: 16px;"}

---
note: "modern chemistry & physics usually has to learning materials that made of multiple particles, it can be really hard to simulate
those particles precisely sometimes."
...

- problems in chemistry & physics

---

![protein](/media/protein.jpg){: style="border: 0; box-shadow: none" height=450}

**Source: © eLife Sciences Publications Ltd**{: style="font-size: 16px; line-height: 0.4;"}
*Amino acid pairs that have co-evolved together (linked by yellow lines) give a useful hint to protein modellers, as the pairs end up close in the folded structure*{: style="font-size: 16px;"}

---
note: "Quantum computers are a new kind of computation resource that make use of quantum effects."
...

## **What is quantum computing**{: style='color: #09add1'}

---
note: "It may help us solve a set of problem with less complexity. e.g it can solve RSAs."
...

- It can factor numbers with exponential speed up comparing to classical computers (the Shor algorithm)
- I can search an unordered list in $O(\sqrt{n})$ time (Grover's algorithm, 1996)
- It can calculate 3SAT with less complexity
    - ($O(1.15^n)$, [Schöning's Algorithm](http://homepages.cwi.nl/~rdewolf/schoning99.pdf))
    {: style="font-size: 25px"}
    - [Record-Breaking Algorithms for SAT](https://digitalcommons.utep.edu/cgi/viewcontent.cgi?referer=&httpsredir=1&article=1256&context=cs_techrep)
    {: style="font-size: 25px"}
    - [Improved Randomized Algorithms for 3-SAT](http://dx.doi.org/10.1007/978-3-642-17517-6_9) ($O(1.32113^n)$ classical comparison)
    {: style="font-size: 25px"}
    - etc.
    {: style="font-size: 25px"}

---
note: "It can simulate physical systems involves quantum effects like proteins, particles, etc."
...

> let the computer itself be built of quantum mechanical elements which obey quantum mechanical laws.

*Feynman, 1982, Int. J. Theor. Phys. 21, 467–488.*{: style="font-size: 20px"}

[Using Quantum Computers for Quantum Simulation](http://www.mdpi.com/1099-4300/12/11/2268/pdf){: .fragment style="font-size: 20px"}

---
note: "A potential quantum (near) future"
...

Intermediate quantum computing regime:

- Error mitigation
- Testable advantage
- Approximate optimizers, Quantum machine learning
- Quantum simulators

---
note: "In near term future, the resources of quantum computing will still be limited, like the early stage, classical algorithm was designed
on papers. We have to design new quantum algorithms and explore when quantum computers is better with classical simulation. However, simulating
quantum computing on classical devices is hard due to its quantum nature. There are a lot of optimized classical algorithms for simulating a small
set of quantum circuits efficiently. Moreover, in the future, researchers may want to immigrate their classical simulated algorithms directly to quantum devices. However, we also hope researchers can focus on their own algorithms rather than backend details. Therefore, we need a framework that is highly extensible but easy to use. And here comes the Yao framework."
...

## What is 幺？

幺(Yao) is a **Extensible**, **Efficient** framework for quantum algorithm design for humans.

---
note: "We provide hierarchical APIs that give developer freedom of extending Yao.

1. We extended the Julia's SparseArrays, which will be contributed to upper stream.
2. Thanks to Julia's multiple dispatch feature, we are able to optimize operator's
  performance with extensions, which means you can choose different optimization
  strategy by using different extensions.
3. We also provide some buildin optimization made by the Boost extension."
...

### Hierarchical APIs

![structre](https://rawgit.com/QuantumBFS/Yao.jl/master/docs/src/assets/figures/framework.png){: style="border: 0; box-shadow: none" height=450}

---
note: "we compare our performance to ProjectQ, a python effort that is able to simulate up to 45 qubits. With optimization
 done by the boost extension. We have much better performance on small circuit simulation and similar performance with large
 circuit simulation. The Q-X is ProjectQ and the Y-X is Yao."
...

![bench-xyz](https://rawgit.com/QuantumBFS/Yao.jl/master/docs/src/assets/benchmarks/xyz-bench.png){: style="border: 0; box-shadow: none" height=450}

---
note: "All of our optimized blocks gain better performance."
...

![bench-cxyz](https://rawgit.com/QuantumBFS/Yao.jl/master/docs/src/assets/benchmarks/cxyz-bench.png){: style="border: 0; box-shadow: none" height=300}
![bench-repeatxyz](https://rawgit.com/QuantumBFS/Yao.jl/master/docs/src/assets/benchmarks/repeatxyz-bench.png){: style="border: 0; box-shadow: none" height=300}

---
note: "Although un-optimized blocks does not as good as ProjectQ's for large number of qubits, but because of our hierarchical APIs and multiple
dispatch, fine-grained optimization can be easily done and dispatched to certain type of circuits without any overheads."
...

![bench-toffoli](https://rawgit.com/QuantumBFS/Yao.jl/master/docs/src/assets/benchmarks/toffoli-bench.png){: style="border: 0; box-shadow: none" height=300}
![bench-crot](https://rawgit.com/QuantumBFS/Yao.jl/master/docs/src/assets/benchmarks/crot-bench.png){: style="border: 0; box-shadow: none" height=300}

---
note: "Let's explore the quantum computing with a few demos with Yao."
...

## What can 幺 do?

---

### Demo 1: Preparing GHZ state

---

A GHZ state is a quantum state looks like:

$$
\frac{|0\cdots 0\rangle + |1\cdots 1\rangle}{\sqrt{2}}
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
