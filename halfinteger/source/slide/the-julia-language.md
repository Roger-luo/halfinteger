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

Roger Luo Research Assistant, IOP

http://rogerluo.me

|                     |                     |
|---------------------|---------------------|
| Interests           | Quantum Information |
|                     | Machine Learning    |
| Expertise           | Hu You              |

---
note: "since there will be links that I recommend, I suggest you open this presentation on your laptop before we started"
...

You can find all related material at

http://num.v2nobel.com/talks/9/

---

I highly recommend you read the documents here:

http://rogerluo.me/TutorialForPhysicists.jl/

And install this tutorial in your Julia by

```julia
julia> Pkg.clone("https://github.com/Roger-luo/TutorialForPhysicists.jl.git")
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
---
note: "Direct construction of Expr objects with value arguments is powerful, but Expr constructors can be tedious compared to \"normal\" Julia syntax. As an alternative, Julia allows \"splicing\" or interpolation of literals or expressions into quoted expressions. Interpolation is indicated by the $ prefix."
...

### Interpolation

---

```julia-repl
julia> a = 1;

julia> ex = :($a + b)
:(1 + b)
```

---

### Evaluation

---

```julia-repl
julia> a = 1; b = 2;

julia> eval(:(a + b))
3
```

---
note: "Macros provide a method to include generated code in the final body of a program. A macro maps a tuple of arguments to a returned expression, and the resulting expression is compiled directly rather than requiring a runtime eval() call. Macro arguments may include expressions, literal values, and symbols."
...

### Macros

A brief structure of Julia's execution process

```julia
prog |> readstring |> parse |> macros |> eval 
```

---
note: "try this simple macro, to see what happens. The macro will catch expressions parsed by Julia compiler and the returns of the macro will be evaluated."
...

```julia
macro showexpr(expr)
    println(expr)
end
```

---
note: "A very special macro is @generated, which allows you to define so-called generated functions. Let's try it by example"
...

### Generated Functions

---
note: "generated functions must be pure functions and it will generates expressions according to the input, and in the runtime, the program will just run through the expressions, which reduces the overheads."
...

**calculate a number from its trinary representation**

```julia-repl
@generated function tri2int(x::NTuple{N, Int}) where N
    # you can only access x as a type inside
    ex = :(x[1])
    for i = 2:N
        base = 3^(i-1)
        ex = :($ex + x[$i] * $base)
    end
    return ex
end
```

---

### Why not Python, Numba, PyPy but Julia?

---

**Julia's Performance is not magic, the language design is**

---
note: "consider a python class, python's class is so dynamic and convenient that
all the methods and members can be dynamically attached to the parent
class `object`"
...

```python
class Foo(object):

    STATIC_MEMBER

    def method1(self):
        pass

    def method2(self):
        pass
```

---
note: "It is hard for the compiler to know all its states until the object is used and will be hard to optimized, therefore numba only optimize a subset of the language and projects like pyston, pypy never acheive a nice performance."
...

```ipython
In [1]: foo = Foo()

In [2]: foo.a = 2

In [3]: foo.a
Out[3]: 2
```

---
note: "while in python we have to use things like cython"
...

Julia itself is even C compatible (more like AOT language than Python)

```julia
Base.@ccallable function hello(n::Int)::Int
    for i = 1:n
        println("hello world")
    end
    return 0
end
```

---

**Julia's metaprogramming is much more stronger than most of the popular languages in numerical computing community, e.g Python, C/C++ and etc.**

---
note: "With strong meteprogramming, libraries with DSL (domain specific language) like [iTensor](http://itensor.org/) can be easy to implement and tasks like code generation can be extremely easy. Although, it is not totally fair that itensor and taco contains some other functionalities, but itensor is over 20k loc, but TensorOperation.jl is only 2k loc and can handle most functionalities of iTensor with Julia builtin functions."
...

iTensor tensor contraction:

```c++
Index a("a",2), 
      b("b",2), 
      c("c",2);
ITensor Z(a,b), 
        X(c,b);

Z.set(a(1),b(1),+1.0);
Z.set(a(2),b(2),-1.0);

X.set(b(1),c(2),+1.0);
X.set(b(2),c(1),+1.0);

//the * operator finds and
//contracts common index 'b'
//regardless of index order:

ITensor R = Z * X;

Print( R.real(a(2),c(1)) ); 
//output: R.real(a(1),c(2)) = -1
```

---
note: "TACO has a very elegant and high efficiency C++ implementation of tensor constractions. But passing indexes to the compiler is still not elegant enough because the lack of builtin metaprogramming feature in C++, you can only hack it by classes and templates"
...

[taco](https://github.com/tensor-compiler/taco) tensor contraction

```c++
// Create formats
Format csr({Dense,Sparse});
Format csf({Sparse,Sparse,Sparse});
Format  sv({Sparse});

// Create tensors
Tensor<double> A({2,3},   csr);
Tensor<double> B({2,3,4}, csf);
Tensor<double> c({4},     sv);

// Insert data into B and c
B.insert({0,0,0}, 1.0);
B.insert({1,2,0}, 2.0);
B.insert({1,3,1}, 3.0);
c.insert({0}, 4.0);
c.insert({1}, 5.0);

// Pack inserted data as described by the formats
B.pack();
c.pack();

// Form a tensor-vector multiplication expression
IndexVar i, j, k;
A(i,j) = B(i,j,k) * c(k);

// Compile the expression
A.compile();

// Assemble A's indices and numerically compute the result
A.assemble();
A.compute();
```

---
note: "with the builtin metaprogramming, implementing this is much easier and simpler, and of course, much safer, because the language itself will help you figure out what you want to do."
...

A brief look at the [TensorOperations.jl](https://github.com/Jutho/TensorOperations.jl) tensor contraction

```julia
using TensorOperations
alpha=randn()
A=randn(5,5,5,5,5,5)
B=randn(5,5,5)
C=randn(5,5,5)
D=zeros(5,5,5)
@tensor begin
    D[a,b,c] = A[a,e,f,c,f,g]*B[g,b,e] + alpha*C[c,a,b]
    E[a,b,c] := A[a,e,f,c,f,g]*B[g,b,e] + alpha*C[c,a,b]
end
```

---
note: "to understand the power of Julia's metaprogramming, it would be better to write something. I will help you to write a very simple kronecker expression parser here with only 3 hundred of lines here and although this requires some basic knowledge of writing parsers, but don't panic, just try it out!"
...


### Let's write a Kronecker Expression Parser

---

**Julia is the only dynamical language that can do GPGPU natively**

*Effective Extensible Programming: Unleashing __Julia__ on __GPUs__: arxiv 11712.03112*{: .fragment}

---
note: "This makes Julia's GPU interface extremely generic and elegant"
...

**define CuArray like CPU**
```julia
xs = cu(rand(5, 5))
ys = cu[1, 2, 3]
xs_cpu = collect(xs)
```

---

**Broadcasting Operations**

Exactly the same with CPU

```julia
zs .= xs.^2 .+ ys .* 2
```

---

**Write Your Own CUDA kernel**

```julia
using CuArrays, CUDAnative

xs, ys, zs = CuArray(rand(1024)), CuArray(rand(1024)), CuArray(zeros(1024))

function kernel_vadd(out, a, b)
  i = (blockIdx().x-1) * blockDim().x + threadIdx().x
  out[i] = a[i] + b[i]
  return
end

@cuda (1, length(xs)) kernel_vadd(zs, xs, ys)

@assert zs == xs + ys
```

---

More details here: [Generic GPU Kernels](http://mikeinnes.github.io/2017/08/24/cudanative.html)

---
note: "Julia is a great language that it allows you to write things like Python, but if you care about the performance, here are some tips"
...

## Performance Tips

---
note: "there are quite a lot performance tips in the documentation, but remember one thing is that there is no silver bullet, the less you cares about, the cost will be paid from other sides."
...

*The more you tell the compiler, the faster your program could be*

---

use BenchmarkTools to measure your performance (similar to python's `timeit`)

```julia-repl
julia> Pkg.add("BenchmarkTools")

julia> @benchmark rand(1000, 1000)
```

---

- Avoid global variables
{: .fragment}

- Provide as much information as possible in compile time.
{: .fragment}

e.g `StaticArray` is faster than native `Array` for small size arrays.
{: .fragment}

---
note: "abstract types contains less detailed information about the memory, avoid using it can improve performance"
...

- Avoid containers with abstract type parameters

```julia
a = Real[] # should use Float64[] here
if (f = rand()) < .8
    push!(a, f)
end
```

---
note: "with similar reason, avoid fields with abstract type"
...

It would be hard to know the exactly type information for a type of `Any`

```julia
struct MyAmbiguousType
    a::AbstractFloat
end
```

---

this would be better

```julia
struct MyAmbiguousType{T <: AbstractFloat}
    a::T
end
```

---
note: "It is often convenient to work with data structures that may contain values of any type (arrays of type Array{Any}). But, if you're using one of these structures and happen to know the type of an element, it helps to share this knowledge with the compiler"
...

Annotate values taken from untyped locations

```julia
function foo(a::Array{Any,1})
    x = a[1]::Int32
    b = x+1
    ...
end
```

---

More about performance tips, please ref the official documentation.

---
note: "Then you may ask what kind of problem are you working on with this language"
...

### What we are working on?

---

### The Quantum Many-body Toolkit
*Name is still not decided yet, better suggestion is welcome*{: style="font-size: 20pt"}

---
note: "What is our motivation in physics? In fact, from last year, we found that there is no mature package from the software engineering aspect in the field of quantum physics. And most of physicists' codes are too fragmented, without contiguous integration and very unsafe to use and share. And even they are lack of readability. There was some libraries that is similar to ours indeed, like ALPS, but ALPS is not very active at the moment and its C++ repository is like a mess."
...

**Motivation**

- Tiny Numerical Tools like the kronecker expression parser could be **too fragmented** for a single package, but we can collect them together with **unified interface**.
{: .fragment}
- Some Python package is not **efficient enough** but requires a long time for developing its C++ backend
{: .fragment}

---

- Some C/C++ library is efficient but lack of a **user friendly** interface to help researcher focus on their research
{: .fragment}
- Most Physicists do not have **professional experience** for writing **high performance** computing program with C/C++. But in quantum physics, especially quantum many-body physics, both program efficiency and development efficiency are crucial.
{: .fragment}

---
note: "Why do we choose Julia? In fact, I wrote this package's prototype in Python with enhancement from C++ by pybind11. However, one day I found pure Julia implementation of the traversion of lattice has similar performance with my Python implementation. But I paid a week for implementing everything in C++ and bind it to python, and only one day for writing a Julia implementation."
...

What Julia offers us:

**Enough Efficiency** It can approach **C/C++** implementation on speed in simple situation and may offer much better

---
note: "Last year, I was developing a famous deep learning framework called PyTorch made by Facebook from its C backend. It is an awesome framework indeed. However, when you try to implement differentiable functions in its C backend, it requires thousands of lines. But I found that with Julia's metaprogramming, I can implement them in a few hundred of lines by code generation. And they have almost the same benchmark on CPU."
...

You can acheive **High abstractions** with **low overhead** with metaprogramming by **code generation** in Julia.

---
note: "As our demo today, the kronecker expression parser is also a functionality of the package. It make use of metaprogramming feature to provide more user friendly interface"
...

**More user-friendly interface** can be implemented through Julia's metaprogramming

---
note: "Julia can call C/C++ functions directly from header files, which allows us to optimize whatever we want in C/C++ without writing any glue code"
...

**Awesome Foreign Function Interface (FFI)**

Call the function `clock` from `libc.so`
```julia
t = ccall((:clock, "libc"), Int32, ())
```

Create a C function with Julia
```
function mycompare(a::T, b::T) where T
    return convert(Cint, a < b ? -1 : a > b ? +1 : 0)::Cint
end
cfunction(mycompare, Cint, (Ref{Cdouble}, Ref{Cdouble}))
```

---
note: "Julia team cares about scientists, because it is designed for science. While Python may have to care about web servers, education, gamings and etc. And moreover it is approaching its first release version 1.0. Only issues related to an iterator optimization has not been solved."
...

Julia cares about science. It is approaching 1.0 within 10 issues.

---
note: "Although, our first tagged version is not released yet, you can check our documents for what is functional at the moment and try it out. We are always welcome for comments of this package development, and please give an issue in the repository. We will accept Pull Requests after the first tagged version which will be in a few weeks"
...

Star our package's documentation at [rogerluo.me/QMTK.jl](http://rogerluo.me/QMTK.jl/)
