---
title: Julia语言
# subtitle: Roger's Fine Slide Generator
description: 一种科学计算的新尝试
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

![julia-logo](/media/julia-logo.svg){: style="border: 0; box-shadow: none"}

**一种科学计算的新尝试**

---

**Available at [rogerluo.me](http://rogerluo.me)**

---

note: "Most people will talk about Julia's performance, I will talk about it today but I will also explain when you won't want to use Julia and when you should use it."
...

## Benchmark

---

**Tensor Contraction**

![](/media/contract.png){: style="border: 0; box-shadow: none" height=450 width=450}

---

**Python (3.5 on IPython 6.3.1)** 326 ms (C implementation in numpy)

```python
import numpy as np

def propagate(LHS, X, Y):
    P = np.einsum('ijk, ipq', LHS, X)
    Q = np.einsum('jkqp, jvrq', P, Y)
    R = np.einsum('kprv, kvm', Q, X)
    return R
```

```ipython
LHS = np.random.randn(200, 10, 200)
X = np.random.randn(200, 2, 200)
Y = np.random.randn(10, 2, 10, 2)

%timeit propagate(LHS, X, Y)
```

---

**Python (3.5 on IPython 6.3.1)** 45.1 ms (numpy.tensordot in numpy)

```python
def propagate(LHS, X, Y):
    P = np.tensordot(LHS, X, axes=([0, ], [0, ]))
    Q = np.tensordot(P, Y, axes=([0, 2], [0, 1]))
    R = np.tensordot(Q, X, axes=([0, 3], [0, 1]))
    return R
```

```ipython
LHS = np.random.randn(200, 10, 200)
X = np.random.randn(200, 2, 200)
Y = np.random.randn(10, 2, 10, 2)

%timeit propagate(LHS, X, Y)
```

---

**Julia (0.6 with OpenBLAS)** 24.593 ms (pure Julia implementation)

```julia
using TensorOperations
using BenchmarkTools

function propagate(LHS, X, Y)
    @tensor R[6,7,8] := LHS[1,2,3]*X[1,4,6]*Y[2,5,7,4]*X[3,5,8]
end

BLAS.set_num_threads(1)
LHS = randn(200, 10, 200); X = randn(200, 2, 200); Y = randn(10, 2, 10, 2);

@benchmark propagate(LHS, X, Y)
```

---

<div>
    <a href="https://plot.ly/~Roger-luo/9/?share_key=Lf91Q3vXngwR4BCCAxVHa2" target="_blank" title="Plot 9" style="display: block; text-align: center;"><img src="https://plot.ly/~Roger-luo/9.png?share_key=Lf91Q3vXngwR4BCCAxVHa2" alt="Plot 9" style="max-width: 100%; max-height: 20%; width: 900px;height: 600px"  width="900" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="Roger-luo:9" sharekey-plotly="Lf91Q3vXngwR4BCCAxVHa2" src="https://plot.ly/embed.js" async></script>
</div>

---

From IBM community: [link](https://www.ibm.com/developerworks/community/blogs/jfp/entry/A_Comparison_Of_C_Julia_Python_Numba_Cython_Scipy_and_BLAS_on_LU_Factorization?lang=en)

**A Comparison of C Julia Numba and Cython on LU Factorization**

---

![numba](/media/runtimes_103.png){: style="border: 0; box-shadow: none"}

---

![cython](/media/runtimes_202.png){: style="border: 0; box-shadow: none"}

---

![numpy](/media/runtimes_203.png){: style="border: 0; box-shadow: none"}

---

![scipy](/media/runtimes_204.png){: style="border: 0; box-shadow: none"}

---

![julia](/media/runtimes_205.png){: style="border: 0; box-shadow: none"}

---
note: "similar to C and Cython for large scale, but faster for small scale (better SIMD and other compiler optimization)"
...

![julia-cython](/media/runtimes_210.png){: style="border: 0; box-shadow: none"}

---

Comparition to QuTIP

[benchmark](https://qojulia.org/benchmarks)

---

[A Comparision between Differential Equation Solvers](http://www.stochasticlifestyle.com/comparison-differential-equation-solver-suites-matlab-r-julia-python-c-fortran/)

---

![compare](https://i1.wp.com/www.stochasticlifestyle.com/wp-content/uploads/2017/11/de_solver_software_comparsion-1.png){: style="border: 0; box-shadow: none"}

---

## Why use Julia wrapper?

[Why use the Julia Tensorflow](https://github.com/malmaud/TensorFlow.jl/blob/master/docs/src/why_julia.md)

---

## Some Selected Features

---

- Multiple Dispatch
{: .fragment .current-visible}
- Dynamic Type System
{: .fragment .current-visible}
- Good Performance, approaching statically-compiled languages like C
{: .fragment .current-visible}
- Lisp-like macros and other metaprogramming facilities
{: .fragment .current-visible}
- Call Python functions: use the PyCall package
{: .fragment .current-visible}

---

- Call C functions directly: no wrappers or special APIs
{: .fragment .current-visible}
- Designed for parallelism and distributed computation
{: .fragment .current-visible}
- Automatic generation of efficient, specialized code for different argument types
{: .fragment .current-visible}
- elegant and extensible conversions and promotions for numeric and other types
{: .fragment .current-visible}
- Efficient support for Unicode, including but not limited to UTF-8
{: .fragment .current-visible}
- MIT licensed: free and open source
{: .fragment .current-visible}

---
background:
    image: ''
    color: black
...

[![幺](https://quantumbfs.github.io/Yao.jl/latest/assets/logo-light.svg){: style="margin: 0; border: none; box-shadow: none; background: none;" width=200 height=200}](https://github.com/QuantumBFS/Yao.jl)

#### **Extensible**{: style='color: #CD5C5C'} **Efficient**{: style='color: orange'} **Quantum Algorithm Design**{: style='color: #26d2a4'} for Humans.

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

- Quantum Circuit Born Machine
- Quantum GAN
- Quantum Circuit Compression

---

![](https://quantumbfs.github.io/Yao.jl/latest/assets/figures/framework.png){: style="border: 0; box-shadow: none"}

---
note: "every component in a quantum circuit is a block. A block is like a quantum program, it is made up by one or more quantum operators. CompositeBlocks are blocks that contains other blocks. Primitive blocks are the immutable elements that will not contain any other blocks.
constant gates are blocks that binds to a constant in memory. It will not allocate any extra memory no matter how many constant gates you have.
In general, each different block type represents a different theoretical concepts or a different approach of simulation/calculation.
You can easily extending this block tree by defining your own block type.
"
...

![block tree](/media/block_tree.svg){: style="border: 0; box-shadow: none" height=700}

---
note: "we compare our performance to ProjectQ, a python effort that is able to simulate up to 45 qubits. With optimization
 done by the boost extension. We have much better performance on small circuit simulation and similar performance with large
 circuit simulation. The Q-X is ProjectQ and the Y-X is Yao."
...

![bench-xyz](https://quantumbfs.github.io/Yao.jl/latest/assets/benchmarks/xyz-bench.png){: style="border: 0; box-shadow: none" height=300}
![bench-rxyz](https://quantumbfs.github.io/Yao.jl/latest/assets/benchmarks/rot-bench.png){: style="border: 0; box-shadow: none" height=300}

---
note: "Julia中文社区由Julia社区中的中文用户发起，成立于2015年。主要的活动包括Julia语言的meetup，中文文档翻译等，以帮助Julia语言在
中国本地传播。我们会在这个月的29号举办2018年的meetup活动，这次将会有包括Julia语言的发明人之一Viral博士等的演讲，敬请期待。"
...

Julia中文社区：[juliacn.com](http:juliacn.com)

---

谢谢
