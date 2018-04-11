---
title : The Julia Language
description: A Fresh Approach to Numerical Computing
author : Roger Luo

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

**A Fresh New Approach to Numerical Computing**

---

**About Me**

Roger Luo (罗秀哲) Research Assistant, IOP


|                     |                     |
|---------------------|---------------------|
| Interests           | Quantum Information |
|                     | Machine Learning    |
| Expertise           | Hu You              |

---
note: "since there will be links that I recommend, I suggest you open this presentation on your laptop before we started"
...

You can access this presentation at

```
http://104.224.129.42/slides/the-julia-language
```

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

## Let's learn it from examples

---

### REPL

Julia has an awesome REPL, just type `julia` in your terminal

```shell
shell> julia
```

---

```
               _
   _       _ _(_)_     |  A fresh approach to technical computing
  (_)     | (_) (_)    |  Documentation: https://docs.julialang.org
   _ _   _| |_  __ _   |  Type "?help" for help.
  | | | | | | |/ _` |  |
  | | |_| | | | (_| |  |  Version 0.6.3-pre.0 (2017-12-18 07:11 UTC)
 _/ |\__'_|_|_|\__'_|  |  Commit 93168a6 (106 days old release-0.6)
|__/                   |  x86_64-linux-gnu

julia>
```

---

### CLI Compiler

Like **GCC**, **Python** and other compilers, you can run julia scripts by
its CLI interface

```shell
shell> julia script.jl
```

---

### **Demo:**{: style='color: #CD5C5C'} Hello World

```julia
println("hello world!")
```

```shell
shell> julia hello.jl
hello world!
```

---
note: "julia has abundant builtin types, even including arbitrary precision numerical types"
...

### Builtin Numerical Types

- `Int8` to `Int128`
{: .fragment .current-visible}
- `Float16` to `Float64`
{: .fragment .current-visible}
- `BigInt` and `BigFloat` (Arbitrary Precision)
{: .fragment .current-visible}

---
note: "a function is defined using the key word function and end, we use :: to declare the variable type, or you can just let julia itself find out the type."
...

### **Demo:**{: style='color: #CD5C5C'} Sum up two numbers

Julia has abundant builtin types, including:

```julia
function mysum(a::Int, b)
    return a + b
end
```

---
note: "We can use `@code_typed` to look julia's type inference"
...

```julia-repl
julia> @code_typed mysum(1, 2)
CodeInfo(:(begin 
        return (Base.add_int)(a, b)::Int64
    end))=>Int64
```

---
note: "Julia has an amazing type system, I will introduce them by writing our own Complex type"
...

### Type System

---
note: "Except abundant builtin types, we can defined our own composite types."
...

```julia
struct Complex128
    real::Float64
    imag::Float64
end
```

---
note: "You can use its default constructor, and note the parameters have an order"
...

```julia
julia> Complex128(1, 2)
```

---
note: "However there are many complex types in different precision, we will use the parameter type"
...

```julia
struct Complex{T}
    real::T
    imag::T
end
```

---
note: You can specify the type parameter by filling its constructor
...

```julia
julia> Complex{Float64}(1.0, 2.0)
Complex{Float64}(1.0, 2.0)
```

---

But actually julia can infer the parameters itself if possible

```julia
julia> Complex(1.0, 2.0)
Complex{Float64}(1.0, 2.0)
```

---
note: "However, we need to limit the type parameter to numerical numbers for safety"
...

This does not make sense for numerics:

```julia
Complex{String}("a", "b")
```

---
note: "All numbers are subtypes of Number in Julia, we will declare our Complex type as an subtype of Number, which means the parameter of the type can only be subtype of Number, and the Complex type itself is an subtype of Number. Number is something called abstract type, which we will introduce later."
...

```julia
struct Complex{T <: Number} <: Number
    real::T
    imag::T
end
```

The operatorr `<:` means subtype, you can also use it to test the relation between types.
{: .fragment}

```julia-repl
julia> Complex <: Number
true
```

---
note: "try it out! And you will receive an error."
...


```julia-repl
julia> Complex{String}
ERROR: TypeError: Complex: in T, expected T<:Number, got Type{String}
```

---
note: "this is the basics of composite types, and we will introduce multiple dispath along with abstract types and parameter types"
...

## **Multiple Dispatch**{: style='color: #CD5C5C'}
## and Julia's 
## **Abstractions**{: style='color: #0066ff'}

---
note: "abstract types are something slightly similar to virtual class, it does not contain anything as its member and can not be constructed."
...

#### Abstract Types

We could define some abstract type hierarchies.

```julia
# The zoo society
abstract type Animal end
abstract type AbstractBird <: Animal end
abstract type AbstractCat <: Animal end
```

---
note: "we will first define some default methods"
...

```
# All subtype of Animal should have a name
name(animal::Animal) = animal.name
gender(animal::Animal) = "unknown"

# We can know about each animal if it can fly
# By requiring this function (or property)
# Most animals won't fly
flyable(animal::Animal) = false
# Most birds can
flyable(bird::AbstractBird) = true
```

---
note: "and we can define new composite type as subtype of an abstract type"
...

```julia
# Kitty is a special Cat
struct Kitty <: AbstractCat
    weight::Float64
end
```

define a constructor with default values

```julia
# Kitty is 0.3kg when she was born
Kitty() = Kitty(0.3)
```

---
note: "subtyping a composite type is invalid"
...

```julia
struct KittyKitty <: Kitty
end
```

---

The ability of dispatching functions according to **runtime type signatures**{: style='color: #CD5C5C'}
is called multiple dispatch.

---
note: "we will define some property for Kitty and Julia will dispatch these methods to methods with input type Kitty when you call it with type Kitty"
...

```julia
# comment this method to see what will happen
# Kitty's name
name(me::Kitty) = "Kitty"
# Kitty's gender
gender(me::Kitty) = "female"
```

---
note: "Julia's Multiple Dispatch will not only affects single type signatures, all kinds of type can be registered as method signature can be used for dispatch"
...

```
# play is a kind of relationship inside the society of animals
# Most animal won't play with others
play(a::Animal, b::Animal) = "$(name(a)) won't play with $(name(b))"
play(a::Animal, b::Animal, c::Animal) = "$(name(a)), $(name(b)), $(name(c)) won't play together"

# Kohen will play with Kitty
# comment this to see what will happen
play(bird::Kohen, cat::Kitty) = "$(name(bird)) will play with $(name(cat))"
play(cat::Kitty, bird::Kohen) = "$(name(cat)) won't play with $(name(bird))"
```

---
note: "There is also parametric types"
...

### Parametric Types

---
note: "There are some bears in the zoo, but bears can be characterized by colors"
...

```julia
# Bear can have different colors
abstract type AbstractBearColor end
abstract type Green <: AbstractBearColor end
abstract type White <: AbstractBearColor end
abstract type Brown <: AbstractBearColor end
abstract type AbstractBear{T <: AbstractBearColor} <: Animal end
```

---
note: "Multiple dispatch will also work on parameters"
...

```julia
# we could define some general interface to All KINDS OF bears
# and use multiple dispatch to specify methods to certain
# type with certain type parameters (signature)
# the word where declares type parameters
color(::Type{AbstractBear{T}}) where T = "We don't have $T Bear"
# you can specify type parameters' parent type if you want
# Union will create a type union, behaves like an abstract type
# in type inference, but it cannot be subtyped
color(::Type{AbstractBear{T}}) where {T <: Union{Brown, White}} = T
color(bear::AbstractBear) where T = color(typeof(bear))
```

---
note: "multiple dispatch can work on different number of arguments"
...

```
# Abram is a Brown bear
struct Abram <: AbstractBear{Brown}
end

name(bear::Abram) = "Abram"

# Dima is a White bear
struct Dima <: AbstractBear{White}
end

name(bear::Dima) = "Dima"

play(a::Abram, b::Dima, c::Kohen) = "Abram, Dima and Kohen often play together"
```

---

**Make your hands dirty**

---
note: "try this"
...

**What is the color of Dima?**

```julia-repl
julia> color(Dima())
```

---
note: "Now we have a complex type, but its default construct does not support real numbers, we will use multiple dispatch to correct this"
...

##### How to fix this?

```julia-repl
julia> Complex(1.0)
ERROR: LoadError: MethodError: Cannot `convert` an object of type Float64 to an object of type Complex
```

---

Try more about multiple dispatch with `zoo.jl` script.

```shell
shell> julia zoo.jl
```

---

### **Mutable**{: style='color: #CD5C5C'} **Types**{: style='color: #6666ff'}
### and
### **Immutable**{: style='color: #CD5C5C'} **Types**{: style='color: #6666ff'}

---
note: "mutable objects are allocated on the heap and have stable memory address, immutable objects may not. To decide whether to make a type mutable ask whether two instances with the same field values would be considered identical, or if they might need to change independently over time."
...

Two essential properties of immutability in Julia:

- An object with an immutable type is passed around (both in assignment statements and in function calls) by copying, whereas a mutable type is passed around by reference.
- It is not permitted to modify the fields of a composite immutable type.

---
note: "since immutables may be allocated on stack and its state can be determined in runtime, it may also have better performance."
...

```
# name can be changed
mutable struct MutablePerson
    name::String
end

# name cannot be changed
struct Person
    name::String
end
```

---
note: Now we know about multiple dispath, and we have our complex type
...

### Inner Constructor

---
note: Inner constructor
...

```julia
struct Complex{T <: Number} <: Number
    real::T
    imag::T

    function Complex(real::T, imag::T) where T
        new(real, imag)
    end
end
```

---
note: Inner constructor is useful when you need to enforce some invariants
...

```julia
julia> struct Even
           e::Int
       end

julia> Even(2)
Even(2)
```

And to reject old numbers

```julia
Even(x) = iseven(x) ? Even(x) : throw(ArgumentError("x=$x is odd))
```

---

This won't work, because it has the signature
```julia
Even(x::Any)
```

But the default constructor has

```julia
Even(x::Int)
```

Julia will call the default constructor first because of multiple dispatch. 

---

We will use the inner constructor instead

```julia-repl
julia> struct Even
          e::Int
          Even(e::Int) = iseven(e) ? new(e) : throw(ArgumentError("e=$e is odd"))
       end
```
---
note: "Julia is an impure functional programming language, the impure means Julia won't require you to write everything in pure functions. And it actually accepts other programming styles"
...

## Functional Programming in Julia

---
note: "In Julia, programs are considered more like functions operating on data, rather than mutable objects interacting with each other like Python and Java. Julia is not a truely functional programming language and it only offers you some features for functional programming that may ease your efforts. However, since some advanced metaprogramming and feature requires some knowledge about functional programming indeed, I will introduce a little bit of it."
...

**Pure Function**

Pure functions are functions that do not have side-effects and impure functions may change the global state.

```julia
x = 2
# impure
function f()
    x = 3
end

# pure
f(x) = x
```

---
note: "like pure functional programming language, Julia works with immutable data structures by default. However, you might find that there are some comments say that there is no immutable or mutables, remember to check the time, Julia offers immutable types in more recent versions"
...

```julia
# immutable type by default
struct Foo
    name::String
end

foo = Foo("Me")
foo.name = "You" # this will cause an error
```

---
note: "but on the other hand, like some other languages (rust and clojure), Julia do not offer tail call optimization. Tail call optimization has pros and cons, I mention this just to clarify that Julia is not a functional programming language, it is only a multi-paradiagm language with functional programming features."
...

```julia
function foo()
    foo()
end
```

This will cause stack overflow.

---
note: "in fact, Julia itself is written by a tone of lisp"
...

This one is functional and is used for Julia's parser at the moment.

[femtolisp](https://github.com/JeffBezanson/femtolisp)

---
note: "back to functional programming, it has pros and cons, practical benefits could be the following, OOP has some disadvantage that we may care about, OOP objects usually depends on some global state and is hard to optimize because there could be undesirable behavior such as race conditions. Functional programming will help you avoid any shared state or side-effects, which eliminates bugs caused by multiple functions competing for the same resources. computation that make use of pure functions will be very easy to scale on clusters"
...

- Laziness
- Cacheable results
- No order dependencies
- Easy to parallelize

---
note: "an example of race condition could be that when you trying writing values with multiple process into a single file, the final output depends on the order randomly and it may not be the result you want. And also shared states like locks will cause deadlock, when process 1 holds resource 2 but want resource 1 and process 2 holds resource 1 and want resource 2, it will do nothing."
...

![deadlock](https://upload.wikimedia.org/wikipedia/commons/2/28/Process_deadlock.svg)

---
note: "but functional programming may cause poor readability because resulting code is often more abstract, more terse and less concrete. And moreover, it is not suitable for some data types, and therefore, I won't recommend you to fully use it for practical numerical programming in physics"
...

- `Arrays` or `Vectors`, because they have amortised constant time O(1) insert at the end and have constant time lookup, make it mutable would be a better choice
- `Hashmaps` or `Hashset` similar

---
note: "however, the use of functional programming will look nice in some situations, using high order functions like map, reduce, etc. will help you ease the efforts."
...

```
map(sin, rand(100, 100)) # sin is a pure function
```

equivalent to

```
sin.(rand(100, 100)) # similar with MATLAB
```

---
note: "the return keyword, like Haskell and lisp, all the Julia's expression will return the evaluation result of the expression, but you can also add return keyword when you are using other paradiagm"
...


```julia
# get 3
begin
    3
end
```

```julia
function foo()
    3
end
```

---
note: "The strongest legacy of Lisp in the Julia language is its metaprogramming support. Like Lisp, Julia represents its own code as a data structure of the language itself. Since code is represented by objects that can be created and manipulated from within the language, it is possible for a program to transform and generate its own code. This allows sophisticated code generation without extra build steps, and also allows true Lisp-style macros operating at the level of abstract syntax trees."
...

## Metaprogramming

---

## Program Representation

Every Julia program starts life as a string:

```julia-repl
julia> prog = "1 + 1"
"1 + 1"
```

---

next it will be parsed to an Julia type Expr:

```julia-repl
julia> ex1 = parse(prog)
:(1 + 1)

julia> typeof(ex1)
Expr
```

---

`Expr` objects contain two parts:

- a Symbol identifying the kind of expression. A symbol is an interned string identifier.

```julia-repl
julia> ex1.head
:call
```

---

- the expression arguments, which may be symbols, other expressions, or literal values:

```
julia> ex1.args
3-element Array{Any,1}:
  :+
 1
 1
```

---

**The key point here is that Julia code is internally represented as a data structure that is accessible from the language itself.**

---
note: "The second syntactic purpose of the : character is to create expression objects without using the explicit Expr constructor. This is referred to as quoting."
...

### Quoting

---
note: "The : character, followed by paired parentheses around a single statement of Julia code, produces an Expr object based on the enclosed code. Here is example of the short form used to quote an arithmetic expression:"
...

```julia-repl
julia> ex = :(a+b*c+1)
:(a + b * c + 1)
```

```julia
ex = quote
    x = 1
    y = 2
    x + y
end
```
