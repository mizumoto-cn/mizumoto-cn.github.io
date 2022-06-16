---
layout: post
title: Effective Error Handling in Golang
subtitle: Some translation
cover-img: /assets/img/path.jpg
thumbnail-img: ""
share-img: /assets/img/path.jpg
tags: [Go]
---

> find the raw document at <https://earthly.dev/blog/golang-errors/>
> Originally written by Brandon Schurman

So, let's begin. Go error handling is a lot more than iferr-oriented programming.

>Error handling in Go is a little different than other mainstream programming languages like Java, JavaScript, or Python. Go’s built-in errors don’t contain stack traces, nor do they support conventional `try/catch` methods to handle them. Instead, errors in Go are just values returned by functions, and they can be treated in much the same way as any other datatype - leading to a surprisingly lightweight and simple design.

Go中的错误处理与其他主流编程语言，如Java、JavaScript或Python，所采用的方式有些不同。Go 的内置错误不包含堆栈跟踪，也不支持传统的 try/catch 方法来处理它们。相反，Go中的错误只是由函数返回的值，它们的处理方式与其他数据类型基本相同--从而形成了令人惊讶的轻量级错误处理机制。

>In this article, I’ll demonstrate the basics of handling errors in Go, as well as some simple strategies you can follow in your code to ensure your program is robust and easy to debug.

在这篇文章中，Brandon Schurman将向你展示Go语言中错误处理的基础知识，以及一些简单的策略。遵循这些策略可以帮助你确保你的代码具有相当的鲁棒性（是健壮的），并易于调试。

### The Error Type || error是什么

> The error type in Go is implemented as the following interface:

```Golang
type error interface {
    Error() string
}
```

> So basically, an error is anything that implements the Error() method, which returns an error message as a string. It’s that simple!

Go中的error类型是通过一个包含Error()方法的简单接口实现的。所以可以简单认为，任何实现了Error()方法，能通过字符串返回一个错误信息的东西都能算是error。就这么简单。

### Constructing Errors || 构建错误

> Errors can be constructed on the fly using Go’s built-in errors or fmt packages. For example, the following function uses the errors package to return a new error with a static error message:

```Golang
package main

import "errors"

func DoSomething() error {
    return errors.New("something didn't work")
}
```

错误可以使用Go的内置错误包或fmt包来即时构建。例如，上面的函数使用 errors 包来返回一个带有静态错误信息的新错误。

> Similarly, the fmt package can be used to add dynamic data to the error, such as an int, string, or another error. For example:

```golang
package main

import "fmt"

func Divide(a, b int) (int, error) {
    if b == 0 {
        return 0, fmt.Errorf("can't divide '%d' by zero", a)
    }
    return a / b, nil
}
```

> Note that fmt.Errorf will prove extremely useful when used to wrap another error with the %w format verb - but I’ll get into more detail on that further down in the article.

同样，fmt包可以用来给错误添加动态数据，比如一个int、字符串或其他错误。例如上面的代码。Errorf在用%(w)格式包装其它错误的时候非常有用，但是他也有着自己的问题，这将在文章后面详细说明。

> There are a few other important things to note in the example above.
>
> - Errors can be returned as nil, and in fact, it’s the default, or “zero”, value of on error in Go. This is important since checking if err != nil is the idiomatic way to determine if an error was encountered (replacing the try/catch statements you may be familiar with in other programming languages).
>
> - Errors are typically returned as the last argument in a function. Hence in our example above, we return an int and an error, in that order.
>
> - When we do return an error, the other arguments returned by the function are typically returned as their default “zero” value. A user of a function may expect that if a non-nil error is returned, then the other arguments returned are not relevant.
>
> - Lastly, error messages are usually written in lower-case and don’t end in punctuation. Exceptions can be made though, for example when including a proper noun, a function name that begins with a capital letter, etc.

在上面的例子中，还有一些重要的事情需要注意。

错误可以以nil的形式返回，事实上，它是Go中错误的默认值，或者说 "零"。这一点很重要，因为检查err != nil是确定是否遇到错误的惯用方法（取代你在其他编程语言中可能熟悉的try/catch语句）。

错误通常作为函数的最后一个参数返回。因此在我们上面的例子中，我们依次返回一个int和一个错误。

当我们返回一个错误时，函数返回的其他参数通常会返回其默认的 "零 "值。一个函数的用户可能期望，如果返回一个非零的错误，那么返回的其他参数就没有意义了。

最后，错误信息通常以小写字母书写，并且不以标点符号结束。但也有例外，例如包括一个专有名词，一个以大写字母开头的函数名称，等等。

TBC ...
