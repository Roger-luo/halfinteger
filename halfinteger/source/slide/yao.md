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

![幺](/media/logo-light.svg){: style="margin: 0; border: none; box-shadow: none; background: none;" width=200 height=200}

#### **Extensible**{: style='color: #CD5C5C'}, **Efficient**{: style='color: orange'} Framework for **Quantum Algorithm Design**{: style='color: #26d2a4'} for Humans.

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
- Approximate optimizers
- Quantum simulators
- Adaptive algorithms on noisy circuits (e.g machine learning)

---
note: ""
...

## What is 幺？

幺(Yao) is a **Extensible**, **Efficient** framework for quantum algorithm design for humans.


---
note: "Let's explore the quantum computing with a few demos with Yao."
...

## What can 幺 do?