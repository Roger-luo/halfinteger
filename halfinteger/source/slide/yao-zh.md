---
title: 幺
# subtitle: Roger's Fine Slide Generator
description: 简单好用的量子算法设计框架.
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

#### **高效**{: style='color: orange'}好用**可扩展**{: style='color: #CD5C5C'} 的**量子算法设计框架**{: style='color: #26d2a4'}

---

[rogerluo.me](http://rogerluo.me)

![](/media/rogerluo-slide.png){: style="border: 0; box-shadow: none" height=500}

---

###  安装Julia:

官方编译器: [julialang.org/downloads](https://julialang.org/downloads/)

julia pro (Julia的annaconda): [juliacomputing.com](https://juliacomputing.com/products/juliapro.html)

---

安装我们的框架:

最新版（lastest）:

```julia
julia> Pkg.clone("https://github.com/QuantumBFS/Yao.jl.git")
```

稳定版（stable）:

```julia
julia> Pkg.add("Yao")
```

---
note: "首先我会简要介绍一下量子计算，然后我们会用幺来探索一些量子算法。"

background:
  image: "/media/qc-background.png"
  size: contain
  color: transparent
...

**量子计算**

---
...

**近期小型量子计算机的潜在应用**:

- 量子化学
- 量子协处理器
- 机器学习

*参见: [Technical Roadmap for Fault-Tolerant Quantum Computing](https://www.nqit.ox.ac.uk/sites/www.nqit.ox.ac.uk/files/2016-11/NQIT%20Technical%20Roadmap.pdf)*{: .fragment style="font-size: 16px"}

---
note: "量子化学也许是目前量子计算最有前景的应用，即便我们已经有了丰富的经典量子化学算法，然而对于一些被称作强关联的分子，传统方法往往无法有效计算出它们的解。这是因为很多经典的近似都有着弱关联的假设。而近期已经有一些概念实验已经在一个有5个比特的量子计算机上展示了量子模拟的威力。这篇文章使用了一个量子线路中的变分参数来学习分子的基态。"
...

**Quantum Chemistry**

![](/media/variational-quantum-eigensolver.png){: style="border: 0; box-shadow: none" height=400}

**O’Malley, P. J. J., et al. "Scalable quantum simulation of molecular energies." Physical Review X 6.3 (2016): 031007.**{: style="font-size: 16px"}

---
note: "小型量子计算机可以作为协处理器完成模拟大型量子计算机的功能。实际上已经被证明我们可以用n个比特的小型量子计算机来模拟n+k个比特的量子计算机，其所需的经典计算资源仅仅随着k发生指数增长。 Besides, we can also simulate physical systems like a Hubbard model."
...

**量子协处理器**

![](/media/trotter-step.png){: style="border: 0; box-shadow: none" height=400}

**Kreula, Juha M., et al. "Few-qubit quantum-classical simulation of strongly correlated lattice fermions." EPJ Quantum Technology 3.1 (2016): 11.**{: style="font-size: 16px"}

---
note: "量子计算机还可以被用来加速机器学习任务。此外出了加速，量子计算机作为一种新的计算资源，也能够让我们使用更强大的模型。"
...

**机器学习**

![](/media/xanadu-chips.png){: style="border: 0; box-shadow: none" height=400}

**Xandadu AI, Quantum Machine Learning 1.0**{: style="font-size: 16px"}

---
note: "例如郜勋在最近一篇文章中证明了量子生成模型比经典生成模型有更好的表达能力。"
...

![](/media/QGM.png){: style="border: 0; box-shadow: none" height=400}

**Gao, Xun, Zhengyu Zhang, and Luming Duan. "An efficient quantum algorithm for generative machine learning." arXiv preprint arXiv:1711.02038 (2017).**{: style="font-size: 16px"}

---
note: "此外，短期内出现的无法纠错的量子计算机实际上也许更加适合做机器学习任务，最近刘金国和王磊提出了一种叫做量子线路波恩机的模型。它能够直接被短期内的小型量子计算机实现。"
...

![](/media/QCBM.png){: style="border: 0; box-shadow: none" height=300}
![](/media/QCL.png){: style="border: 0; box-shadow: none" height=300}

**Liu, Jin-Guo, and Lei Wang. "Differentiable learning of quantum circuit Born machine." arXiv preprint arXiv:1804.04168 (2018).**{: style="font-size: 16px"}

**Mitarai, Kosuke, et al. "Quantum circuit learning." arXiv preprint arXiv:1803.00745 (2018).**{: style="font-size: 16px"}

---

**量子计算就要来了**

---
note: "量子计算机的比特数目一直在提高，而最近IBM，Google，Intel都宣布了40个比特以上的机型."
...

![](/media/QC-is-near.JPG){: style="border: 0; box-shadow: none" height=500}

**Source: © By Thomas A. Campbell, Ph.D., FutureGrasp, LLC**{: style="font-size: 16px;"}

---
note: "这是一个量子计算机发展的规划图"
...

![roadmap](/media/roadmap-qc.jpg){: style="border: 0; box-shadow: none" height=500}

**J. Ignacio Cirac & H. Jeff Kimble. "Quantum optics, what next?" Nature Photonics volume 11, pages 18–20 (2017).**{: style="font-size: 16px"}

---
note: "Google/IBM/Intel正在实现量子优势，或者说是量子霸权。这是Google和IBM所展出的接近量子优势的机器。"
...

![Google](/media/google-chips.png){: style="border: 0; box-shadow: none" height=200}
![IBM](/media/IBM-CES.jpeg){: style="border: 0; box-shadow: none" height=200}

**Source: © By Nick Summers, engadget / Google AI lab**{: style="font-size: 16px;"}

---
note: "在不远的将来，量子计算资源依然受限，正如早起的经典算法都是在纸上设计的一样，在很长的一段时间里我也需要使用经典计算机来辅助我们设计量子算法。然而在经典计算机上模拟量子算法往往是非常困难的，由于量子系统的空间会指数增长，我们需要在技术上小心处理各种技术问题。并且实际上有一些类型的量子线路是可以进行高效模拟的，而作为量子信息理论的研究人员，我们并不希望时常去关注这些与核心内容无关的技术细节，而我们又希望我们可以根据自己的研究需要修改一些算法细节。此外，由于目前我们还不清楚量子编程的具体形式，一个高效的量子算法设计框架也能够帮助我们探索如何给量子计算机编程。综上，我们需要一个高性能，高扩展性，而又好用的框架，所以我们开发了幺。幺这个字来自于幺正矩阵，或者你也可以认为它来自于麻将。"
...

## 幺是什么？

幺(Yao)是一个**可扩展**的**高性能**量子算法设计框架

---
note: "那么我们首先来通过幺介绍简要介绍一下量子计算。"
...

## 幺可以用来做什么？


---
note: "下面我们来通过幺熟悉一些量子计算的基础"
...

**量子计算基础**

---
note: ""
...

**回顾：线性代数**

---

**矩阵向量的乘积**

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

**矩阵和矩阵的乘法**

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

**单位矩阵**

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

**置换矩阵**

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
note: "向量的张量乘"
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
note: "用向量来表示多个经典比特"
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
note: "让我们在幺中尝试一下经典比特的向量形式是什么"
...

**Try this**

```julia
register(bit"01") |> statevec
```

---
note: "经典比特操作的矩阵形式，它也被称为真值表。"
...

| 名称     | 函数            | 矩阵                                        |
|:---------|:----------------|:--------------------------------------------|
| Identity | $f(x) = x$      | $\begin{pmatrix} 1 & 0\\0 & 1\end{pmatrix}$ |
| Negation | $f(x) = \neg x$ | $\begin{pmatrix} 0 & 1\\1 & 0\end{pmatrix}$ |
| Const-0  | $f(x) = 0$      | $\begin{pmatrix} 1 & 1\\0 & 0\end{pmatrix}$ |
| Const-1  | $f(x) = 1$      | $\begin{pmatrix} 0 & 0\\1 & 1\end{pmatrix}$ |

---

**求反**

```julia
with!(X, register(bit"0")) |> statevec
```

---

**多比特的操作：控制非门**

$$
\begin{pmatrix}
1 & 0 & 0 & 0\\
0 & 1 & 0 & 0\\
0 & 0 & 0 & 1\\
0 & 0 & 1 & 0
\end{pmatrix}
$$

---

**试试这个**

```julia
g = control(2, [1, ], 2=>X)
```

```julia
with!(g, register(bit"10")) |> statevec

with!(g, register(bit"00")) |> statevec
```

---

## 量子比特

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
note: "当你测量它的时候它就会塌缩到其中之一上去。"
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
