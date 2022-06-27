---
layout: post
title: Int array equals to `any` array, or not?
subtitle: The Equivalence between Interface and Non-interface Variables
cover-img: /assets/img/path.jpg
thumbnail-img: ""
share-img: /assets/img/path.jpg
tags: [Go]
---

So let's start with the code below:

```golang
package main

func main() {
    var wubba [100]int
    var lubba any = [...]int{99:0}
    dubdub := wubba == lubba
    println(dubdub)
}
```

What will the output be?

A. `true` B. `false` C. `panic` D. `Compile error`

The answer will be A, `true`.

This may be a little bit counter-intuitive, but it's the correct answer. Let's dive into it.

### `any` is an alias of `interface{}`

You can even use `gofmt -w -r 'interface{} -> any' ./...` to convert all `interface{}` to `any` in your .go code files.

> As a bit of a digression, at this moment everyone is in the painful stage of mixing `interface{}` with `any`, as go1 needs to be compatible with earlier versions.

So the question turns into the equivalence of `interface` and `non-interface type T`.

### The equivalence of `interface` and `non-interface type T`

> The equality operators == and != apply to operands that are comparable. 
> ...
> A value x of non-interface type X and a value t of interface type T are comparable when values of type X are comparable and X implements T. They are equal if t's dynamic type is identical to X and t's dynamic value is equal to x.

<!-- markdownlint-disable MD004 MD033 -->

<p align="right">Quoted from <a href="https://go.dev/ref/spec#Operators">[go.dev/ref/spec]</a></p>

We all know how arrays are equal to each other, so the question turns into

```golang
println(interface{}(0) == int(0))
```

obviously this will print `true`.
