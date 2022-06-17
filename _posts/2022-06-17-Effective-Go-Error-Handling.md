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

```golang
type error interface {
    Error() string
}
```

> So basically, an error is anything that implements the Error() method, which returns an error message as a string. It’s that simple!

Go中的error类型是通过一个包含Error()方法的简单接口实现的。所以可以简单认为，任何实现了Error()方法，能通过字符串返回一个错误信息的东西都能算是error。就这么简单。

### Constructing Errors || 构建错误

> Errors can be constructed on the fly using Go’s built-in errors or fmt packages. For example, the following function uses the errors package to return a new error with a static error message:

```golang
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

错误可以以nil的形式返回，事实上，nil是Go中错误的默认值，或者说 "零"。这一点很重要，因为检查err != nil是确定是否遇到错误的惯用方法（取代你在其他编程语言中可能熟悉的try/catch语句）。

错误通常作为函数的最后一个参数返回。例如在我们上面的例子中，我们依次返回一个int和一个错误。

当我们返回一个错误时，函数返回的其他参数通常会返回其默认的 空值。一个函数如果返回一个非零的错误，那么返回的其他参数就没有意义了。

最后，错误信息通常以小写字母书写，并且不以标点符号结束。但也有例外，例如包括一个专有名词，一个以大写字母开头的函数名称，等等。

### Defining Expected Errors || 定义预期的错误

> Another important technique in Go is defining expected Errors so they can be checked for explicitly in other parts of the code. This becomes useful when you need to execute a different branch of code if a certain kind of error is encountered.

定义预期错误相当重要，这样就可以在代码的其他部分明确地检查这些错误。当你需要做出在遇到某种错误时执行不同的代码分支的决定时，这就很有用。

#### Defining Sentinel Errors || 定义哨兵错误

> Building on the Divide function from earlier, we can improve the error signaling by pre-defining a “Sentinel” error. Calling functions can explicitly check for this error using errors.Is:

```golang
package main

import (
    "errors"
    "fmt"
)

var ErrDivideByZero = errors.New("divide by zero")

func Divide(a, b int) (int, error) {
    if b == 0 {
        return 0, ErrDivideByZero
    }
    return a / b, nil
}

func main() {
    a, b := 10, 0
    result, err := Divide(a, b)
    if err != nil {
        switch {
        case errors.Is(err, ErrDivideByZero):
            fmt.Println("divide by zero error")
        default:
            fmt.Printf("unexpected division error: %s\n", err)
        }
        return
    }

    fmt.Printf("%d / %d = %d\n", a, b, result)
}
```
在前面的Divide函数的基础上，我们可以通过预先定义一个 "哨兵 "错误来改善错误信号。调用函数可以使用`errors.Is()`来明确地检查这个错误。

#### Defining Custom Error Types || 定义自定义错误类型

> Many error-handling use cases can be covered using the strategy above, however, there can be times when you might want a little more functionality. Perhaps you want an error to carry additional data fields, or maybe the error’s message should populate itself with dynamic values when it’s printed.
>
> You can do that in Go by implementing custom errors type.
>
> Below is a slight rework of the previous example. Notice the new type DivisionError, which implements the Error interface. We can make use of errors.As to check and convert from a standard error to our more specific DivisionError.

```golang
package main

import (
    "errors"
    "fmt"
)

type DivisionError struct {
    IntA int
    IntB int
    Msg  string
}

func (e *DivisionError) Error() string { 
    return e.Msg
}

func Divide(a, b int) (int, error) {
    if b == 0 {
        return 0, &DivisionError{
            Msg: fmt.Sprintf("cannot divide '%d' by zero", a),
            IntA: a, IntB: b,
        }
    }
    return a / b, nil
}

func main() {
    a, b := 10, 0
    result, err := Divide(a, b)
    if err != nil {
        var divErr *DivisionError
        switch {
        case errors.As(err, &divErr):
            fmt.Printf("%d / %d is not mathematically valid: %s\n",
              divErr.IntA, divErr.IntB, divErr.Error())
        default:
            fmt.Printf("unexpected division error: %s\n", err)
        }
        return
    }

    fmt.Printf("%d / %d = %d\n", a, b, result)
}
```

许多错误处理的用例都可以用上面的哨兵策略来覆盖。然而，有时你可能需要更多的上下文信息。也许你想让一个错误携带额外的数据字段，或者错误的信息在被打印时应该自带一个动态的数值。

你可以通过实现自定义错误类型在Go中做到这一点。

下面是对前一个例子的轻微改编。注意新的`DivisionError`类型，它实现了`Error()`接口。我们可以利用`errors.As()`来检查并赋值，即从标准错误转换到我们更具体的`DivisionError`。

- 译者注： 仍然推荐使用`ErrErrorName`的形式命名错误类型

> Note: when necessary, you can also customize the behavior of the `errors.Is()` and `errors.As()`. See this [Go.dev blog](https://go.dev/blog/go1.13-errors) for an example.
>
> Another note: `errors.Is()` was added in Go 1.13 and is preferable over checking `err == ....` More on that below.

注意：必要时，你也可以自定义 `errors.Is` 和 `errors.As` 的行为。参见Go.dev博客中的[例子](https://go.dev/blog/go1.13-errors)。

另一个注意点：`error.Is`是在Go 1.13中添加的特性。正确使用这个函数会优于`err == ...`。下面有关于这个问题的更多内容。

- 译者注：普通想来，fmt.Errorf()会破坏相等性，因而`err ==`无法正确判断错误的类型。
  
### Wrapping Errors || 包装错误

> In these examples so far, the errors have been created, returned, and handled with a single function call. In other words, the stack of functions involved in “bubbling” up the error is only a single level deep.
>
> Often in real-world programs, there can be many more functions involved - from the function where the error is produced, to where it is eventually handled, and any number of additional functions in-between.
>
> In Go 1.13, several new error APIs were introduced, including errors.Wrap and errors.Unwrap, which are useful in applying additional context to an error as it “bubbles up”, as well as checking for particular error types, regardless of how many times the error has been wrapped.
>
> > A bit of history: Before Go 1.13 was released in 2019, the standard library didn’t contain many APIs for working with errors - it was basically just `errors.New` and `fmt.Errorf`. As such, you may encounter legacy Go programs in the wild that do not implement some of the newer error APIs. Many legacy programs also used 3rd-party error libraries such as `pkg/errors`. Eventually, a formal proposal was documented in 2018, which suggested many of the features we see today in Go 1.13+.

在到目前为止的这些例子中，错误是通过调用一个函数来创建、返回和处理的。换句话说，参与 "冒泡"错误的函数堆栈只有一个层次的深度。

在现实世界的程序中，往往会有更多的函数参与其中--从产生错误的函数，到最终处理错误的函数，以及中间的任何数量的附加函数。

在Go 1.13中，引入了几个新的错误API，包括`errors.Wrap`和`errors.Unwrap`，它们在错误 "冒泡"时对其附加额外的上下文信息。它们还能检查错误是否是特定的错误类型，无论这些错误被包装了多少次。

-> 看看历史。在2019年发布Go 1.13之前，标准库并不包含许多用于处理错误的API--基本上只有 `errors.New` 和 `fmt.Errorf`。因此，你可能会在野生环境中遇到遗留的，没能采用新的错误API实现的Go程序。许多遗留程序还使用第三方错误库，如pkg/errors。最终，在2018年Go语言通过了一个正式提案，其中提出了许多我们今天在Go 1.13+中看到的功能。

### The Old Way (Before Go 1.13) || 旧时代的方法（Go 1.13之前）

> It’s easy to see just how useful the new error APIs are in Go 1.13+ by looking at some examples where the old API was limiting.
>
> Let’s consider a simple program that manages a database of users. In this program, we’ll have a few functions involved in the lifecycle of a database error.
>
> For simplicity’s sake, let’s replace what would be a real database with an entirely “fake” database that we import from "example.com/fake/users/db".
>
> Let’s also assume that this fake database already contains some functions for finding and updating user records. And that the user records are defined to be a struct that looks something like:

通过看一些旧的API有局限性的例子，很容易看出Go 1.13+中新的错误API有多么有用。

让我们用一个管理用户数据库的简单程序作例子吧。在示例程序中，将有几个函数参与到数据库错误处理的生命周期中。

为了简单起见，让我们从 "example.com/fake/users/db "导入用一个完全 "假 "的数据库来代替真正的数据库。

我们假设这个假数据库已经包含了一些查找和更新用户记录的函数。而且用户记录被定义为一个结构，看起来像这样：

```golang
package db

type User struct {
  ID       string
  Username string
  Age      int
}

func FindUser(username string) (*User, error) { /* ... */ }
func SetUserAge(user *User, age int) error { /* ... */ }
```

> Here’s our example program:

这里是我们的示例代码：

```golang
package main

import (
    "errors"
    "fmt"

    "example.com/fake/users/db"
)

func FindUser(username string) (*db.User, error) {
    return db.Find(username)
}

func SetUserAge(u *db.User, age int) error {
    return db.SetAge(u, age)
}

func FindAndSetUserAge(username string, age int) error {
  var user *User
  var err error

  user, err = FindUser(username)
  if err != nil {
      return err
  }

  if err = SetUserAge(user, age); err != nil {
      return err
  }

  return nil
}

func main() {
    if err := FindAndSetUserAge("bob@example.com", 21); err != nil {
        fmt.Println("failed finding or updating user: %s", err)
        return
    }

    fmt.Println("successfully updated user's age")
}
```

> Now, what happens if one of our database operations fails with some `malformed request` error?
>
> The error check in the `main` function should catch that and print something like this:

现在，如果我们的一个数据库操作因为一些"畸形请求错误"而失败，会发生什么？

主函数中的错误检查应该捕捉到这一点，并打印出类似这样的东西:

`failed finding or updating user: malformed request`

> But which of the two database operations produced the error? Unfortunately, we don’t have enough information in our error log to know if it came from FindUser or SetUserAge.
> >
> Go 1.13 adds a simple way to add that information.

但这两个数据库操作中的哪一个产生了错误？不幸的是，我们的错误日志中没有足够的信息来知道它是来自`FindUser`还是`SetUserAge`。

Go 1.13增加了一个简单的方法来添加这些信息。

#### Errors Are Better Wrapped || 错误们被更好地包装起来

> The snippet below is refactored so that is uses fmt.Errorf with a %w verb to “wrap” errors as they “bubble up” through the other function calls. This adds the context needed so that it’s possible to deduce which of those database operations failed in the previous example.

下面的代码段经过重构，使用带有%w动词的fmt.Errorf来 "包裹 "错误，因为它们通过其他函数调用 "冒泡"。这增加了所需的上下文，从而有可能推断出在前面的例子中哪些数据库操作失败。

```golang
package main

import (
    "errors"
    "fmt"

    "example.com/fake/users/db"
)

func FindUser(username string) (*db.User, error) {
    u, err := db.Find(username)
    if err != nil {
        return nil, fmt.Errorf("FindUser: failed executing db query: %w", err)
    }
    return u, nil
}

func SetUserAge(u *db.User, age int) error {
    if err := db.SetAge(u, age); err != nil {
      return fmt.Errorf("SetUserAge: failed executing db update: %w", err)
    }
}

func FindAndSetUserAge(username string, age int) error {
  var user *User
  var err error

  user, err = FindUser(username)
  if err != nil {
      return fmt.Errorf("FindAndSetUserAge: %w", err)
  }

  if err = SetUserAge(user, age); err != nil {
      return fmt.Errorf("FindAndSetUserAge: %w", err)
  }

  return nil
}

func main() {
    if err := FindAndSetUserAge("bob@example.com", 21); err != nil {
        fmt.Println("failed finding or updating user: %s", err)
        return
    }

    fmt.Println("successfully updated user's age")
}
```

TBC...