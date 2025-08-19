  
Lambda calculus was introduced by Alonzo Church in the 1930s and is, essentially, a way of expressing computation through the use of functions we call Lambdas (yes, the same name you use for unnamed JavaScript functions). If a problem is computable then it means we can build an algorithm to solve it and thus it can be expressed through the use of Lambda Calculus, just like we could do with the use of [](https://en.wikipedia.org/wiki/Turing_machine).There are two broad kinds of lambda calculus: _untyped_ and _typed_. The untyped lambda calculus, discussed in this article, expresses an unrestricted computation. While it doesn’t find much use outside of computability theory, it’s necessary to understand it to meaningfully discuss the typed varieties.

1936 - Alan Turing invents every programming language that will ever be but is shanghaied by British Intelligence to be 007 before he can patent them.

1936 - Alonzo Church also invents every language that will ever be but does it better. His lambda calculus is ignored because it is insufficiently C-like. This criticism occurs in spite of the fact that C has not yet been invented.

Lambda calculus, initially envisioned as a formal logic system, was developed by [](https://en.wikipedia.org/wiki/Alonzo_Church) around the 1930s to explore the foundations of mathematics.

The initial formulation had a logical inconsistency known as the [](https://en.wikipedia.org/wiki/Kleene%E2%80%93Rosser_paradox) (Cantini, 2007). To sidestep this issue, Church isolated the part of lambda calculus relevant only to computation in 1936. This isolate is now known as the untyped lambda calculus

Later, in 1940, a typed version of lambda calculus based on Russel’s type theory was introduced. It has weaker expressive power, but it’s logically consistent.

In the mid-1960s, Peter Landin showed that lambda calculus models arbitrarily complex programming languages. Arguably, this insight kickstarted the research on functional programming languages.

## 

The pure untyped lambda calculus

The simplest, smallest type of lambda calculus is the pure untyped lambda calculus, so we’ll start with it.

Like any untyped lambda calculus, it is first and foremost a consistent system for rewriting expressions. And it’s called pure because it doesn’t have anything beyond what’s strictly necessary – it only contains functions and variables.

We can formally define the pure untyped lambda calculus in terms of _abstractions_ and _applications_.

### 

Abstractions

An abstraction, or a functional abstraction, is a parametric expression, that is to say, a function. Lambda calculus only defines univariate (single-variable) functions, but we can easily extend it to include multivariate functions too, as we’ll see later.

We introduce new abstractions using the λλ symbol. An abstraction consists of a _head_ and a _body_, separated by the dot (..) symbol. The head contains the λλ symbol and the argument name. The body is an arbitrary expression. For example, λx.xλx.x is an abstraction.

Lambda calculus derives its name from the λλ symbol used in this notation. Church has stated a couple times the symbol was chosen arbitrarily. However, there’s some evidence (Cardone, 2006) that the notation was derived from x^x^ used for class abstraction by Whitehead and Russell in Principia Mathematica, morphing first into ΛxΛx and later into λxλx.

Variables in the body of an abstraction that are parameters of said abstraction are called _bound variables_. Other variables are called _free variables_.

For example, consider the expression:

λy.(λz.x  y  z)  z.λy.(λz.xyz)z.

Variables y,y, zz in the body of the inner abstraction (x  y  z)(xyz) are bound in this expression. Variable xx is free everywhere. The last variable zz in the outer abstraction λy.…  zλy.…z is also free, because no abstraction binds (i.e. introduces) it before it is used. All bindings are local.

An expression without free variables is called a _closed term_ or a _combinator_.

For example, the expression λx.λy.λz.x  y  z.λx.λy.λz.xyz. is a combinator because xx, yy, and zz are bound in one of the outer (relative to their use) abstractions. However, the sub-expression λy.λz.x  y  zλy.λz.xyz _by itself_ is not.

The choice of bound variable names is arbitrary. Expressions that differ only in the names of bound variables are called _alpha-equivalent_. For example, λx.xλx.x and λy.yλy.y are alpha-equivalent, but λx.yλx.y and λy.zλy.z are not.

And, as usual in abstract mathematics, we can assign a name to an expression. Here we’ll be using the equals sign (==) for that. For example: id=λx.x.id=λx.x.

  
https://serokell.io/blog/untyped-lambda-calculus[](https://serokell.io/blog/untyped-lambda-calculus)dfd()https://serokell.io/blog/untyped-lambda-calculus[](https://serokell.io/blog/untyped-lambda-calculus)fd()()