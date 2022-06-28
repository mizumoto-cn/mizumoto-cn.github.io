---
type: post
title: Elegant Error Handling in Go
subtitle: Column - Go & Micro Services
thumbnail-img: ""
share-img: /assets/img/path.jpg
tags: [Go, Micro-services]
---

### Foreword

Earlier this month, I've translated an article introducing different error handling strategies in Go. [Effective Go Error Handling](./2022-06-17-Effective-Go-Error-Handling.md).

But as we often encounter in our daily programming, we sometimes write tons of `log`s and `if err != nil` statements. Sometimes being stupid can solve the problem, but sometimes stupid efforts do not necessarily pay off.

So let's begin.

### Panic & Recover

Though we do not recommend you to use `panic` initially, it is sometimes necessary to be taken into consideration.

#### When can you panic?

Panic usually means that the program is about to crash unless you handle it properly. Foe example, you may use `panic` under these circumstances:

1. A service on which the program has string rely is not available.
2. The configuration is apparently not correct when starting the service.

Otherwise, unless unrecoverable error occurs, you shall not use `panic` directly.

#### When can you recover?

1. When you enter a program. For example, you may use `recover` to prevent the program from crashing when you use some of the `gin`'s middleware.
2. Try avoid using wild goroutines
   i. If async tasks are requested, you shall use async `worker`s, and deal with the problem with the message queue. Avoid creating too many `goroutine`s.
   ii. Use a universal `Go()` function to create a goroutine. In which you can use `recover` to handle the error, avoid wild goroutines causing the program `panic` to crash.

The code below is a simple example.

```golang
func Go(f func()) {
    go func() {
        defer func() {
            if err := recover(); err != nil {
                log.Println(err)
            }
        }()

        f()
    }()
}
```

### Error

So now let's go back to the `error`.

#### About `github.com/pkg/errors`

We can use pkg/errors in single programs, but remember that it is not a good idea to use it in public libraries.

#### About the `error` type

1. `error` should be the last return type of a function. When `err` is not nil, the other return types shall be ignored. We shall not expect anything else the function returns.

To be continued...