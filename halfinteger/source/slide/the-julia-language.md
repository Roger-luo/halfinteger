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

** Make your hands dirty **

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
note: ""
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

