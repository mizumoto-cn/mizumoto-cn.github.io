---
type: post
title: Side Article(0) - Elegant Error Handling in Go (Part 0)
subtitle: Column - Go & Micro Services
thumbnail-img: ""
share-img: /assets/img/path.jpg
tags: [Go, Micro-services]
---

### Foreword

Earlier this month, I've translated an article introducing different error handling strategies in Go. [Effective Go Error Handling](./2022-06-17-Effective-Go-Error-Handling.md).

But as we often encounter in our daily programming, we sometimes write tons of `log`s and `if err != nil` statements. Sometimes being stupid can solve the problem, but sometimes stupid efforts do not necessarily pay off.

So let's begin.

<!-- markdownlint-disable MD010 MD034 -->

### Panic & Recover

Though we do not recommend you to use `panic` initially, it is sometimes necessary to be taken into consideration.

#### When can you panic?

Panic usually means that the program is about to crash unless you handle it properly. For example, you may use `panic` under these circumstances:

1. A service on which the program has string rely is not available.
2. The configuration is not correct when starting the service.

Otherwise, unless an unrecoverable error occurs, you shall not use `panic` directly.

#### When can you recover?

1. When you enter a program. For example, you may use `recover` to prevent the program from crashing when you use some of the `gin`'s middleware.
2. Try to avoid using wild goroutines
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

We can use `pkg/errors` in single programs, but remember that it is not a good idea to use it in public libraries.

#### About the error type

1. An `error` should be the last return type of a function. When `err` is not nil, the other return types shall be ignored. We shall not expect anything else the function returns. There may be some data in the return values but we shall discard them as we cannot prove its correctness.

#### About code layout and control flow

The normal logic code shall be a straight line, while the error handling code shall be a block after the `if err != nil` statement.

> Which I usually refer to as "if-err oriented programming".

And throw the error back using `errors.New()` or `errors.Errorf()`.

If the error comes from another function, simply return it, or use `errors.WithMessage()` to wrap the error if you need more context.

```golang
if err != nil {
    return errors.WithMessage(err, "context info")
}
```

If the error comes from a 3-rd party library, use `errors.Wrap()` to wrap the error if you need more context.
    - Note that you just need to wrap the error once when it occurs. Do not wrap it again elsewhere.
    - In some situations you may choose to discard the error after judging, e.g. database-related errors in the `repository` layer. Returning business error codes is a better idea. Avoid changing superstructure codes when changing the `ORM` library or partitioning microservices.
    - Also if you are writing a reused library, please don't use `errors.Wrap()` as it may cause duplicate error messages.

#### About logging

Never ever log everywhere. Logs shall only be printed once at the beginning of the process using the `%+v` format.

#### Error equivalence & type assertion

Use `errors.Is()` to check if two errors are the same.

```golang
if errors.Is(err, io.EOF) {...}
```

Use `errors.As()` to check the error type.

```golang
err := A()

var errA errorA
if errors.As(err, &errA){
	// ...
}
```

#### Other details

- Always try to ensure you printed enough error information to help you locate problems. For example, the parameter information is usually printed in request logs.
- As for business errors, it's recommended to set up an isolated error dictionary containing the specified error codes and print them in the log file as a separate field.
- Always print a log when an error gets discarded.
- When errors occur continuously at a same point, don't print error logs repeatedly. Just print the detailed error message once, and then calculate the number of times errors occur and print it in the log file.
- Use a same schema for same cases. For example, as for parameter errors, don't return a 404 here and a 200 there.
- When handling errors, remember to deal with the resource assigned. Manage them in the `defer` statement, such as file handles, database connections, etc.

### Panic or Error?

#### Panic cannot be used everywhere

`panic` is a fatal error in Go and will cause the program to crash. Of course, you can catch `panic`s using `recover` but there can be lots of problems.
    - using `recover` will cause performance issues.
    - prone to abnormal exits.
    - Uncontrollable. If you throw out `panic` to the outside caller and the caller doesn't catch it, the program will crash. We cannot control the caller.

Thus we shall use `panic` only in real emergencies like stack overflow/index out of range/unrecoverable environment errors etc.

#### Why errors instead

- Easy to use.
- Plan for failure, not success.
- No hidden control flow, no hidden side effects.
- Totally controllable.
- Errors are values.

### `errors.New()` returns a pointer?

The `errorString` structure in the `errors` library implements the `error` interface, but why does it return a pointer to a structure when `New()` an `error`?

```golang
// New returns an error that formats as the given text.
// Each call to New returns a distinct error value even if the text is identical.
func New(text string) error {
	return &errorString{text}
}

// errorString is a trivial implementation of error.
type errorString struct {
	s string
}

func (e *errorString) Error() string {
	return e.s
}
```

The only difference between our custom one and the standard library one is that the self-built one returns a **value** rather than a **pointer**.

We can see in the comparison of the `main` function that our custom `errorString` will return `true` when comparing as long as the corresponding **strings are the same**, but the standard library package will not.

This is because when comparing two `struct`s to see if they are the same, it will compare whether the **fields** in the two `struct`s are the same and return true if they are, but when comparing pointers it will determine whether the **addresses** of the two pointers are the same.

#### And `true` when strings are the same will cause trouble

If I have two packages that define two `error`s, they are actually two identical strings, and when other libraries call them for comparison, they may go into different branches due to different writing orders resulting in some odd problems.

```golang
type errorString struct {
	text string
}

func (e errorString) Error() string {
	return e.text
}

// New 创建一个自定义错误
func New(s string) error {
	return errorString{text: s}
}

var errorString1 = New("test a")
var err1 = errors.New("test b")

func main() {
	if errorString1 == New("test a") {
		fmt.Println("err string a") // 会输出
	}

	if err1 == errors.New("test b") {
		fmt.Println("err b") // 不会输出
	}
}
```

### Error types
 
#### Sentinel errors

`io` library for example:

```golang
// EOF is the error returned by Read when no more input is available.
// Functions should return EOF only to signal a graceful end of input.
// If the EOF occurs unexpectedly in a structured data stream,
// the appropriate error is either ErrUnexpectedEOF or some other error
// giving more detail.
var EOF = errors.New("EOF")

// ErrUnexpectedEOF means that EOF was encountered in the
// middle of reading a fixed-size block or data structure.
var ErrUnexpectedEOF = errors.New("unexpected EOF")

// ErrNoProgress is returned by some clients of an io.Reader when
// many calls to Read have failed to return any data or error,
// usually the sign of a broken io.Reader implementation.
var ErrNoProgress = errors.New("multiple Read calls return no data or error")
```

When we try to judge them we use `errors.Is()`:

```golang
if errors.Is(err, io.EOF) {...}
```

The only problem is exposing error types as APIs to the outside world, causing problems when refactoring.

Also sentinel errors do not carry much context information.

#### error types

```golang
type MyStruct struct {
	s string
    name string
    path string
}



// 使用的时候
func f() {
    switch err.(type) {
        case *MyStruct:
        // ...
        case others:
        // ...
    }
}
```

More context than sentinel errors can be carried, but also exposes the error type to the outside world. `os.PathError` is an example.

#### Opaque errors

The most important feature is that only the error is returned, exposing the error determination interface, not the type, which can reduce the exposure of the APIs, the subsequent processing will be more flexible. Generally used in public libraries.

```golang
type temporary interface {
	Temporary() bool
}

func IsTemporary(err error) bool {
	te, ok := err.(temporary)
	return ok && te.Temporary()
}
```

Instead of asserting that the error  is of a particular type or value, we can assert that the error implements a particular behaviour.

### Optimizing error handling

How to use less iferr blocks?

#### bufio.scan

Comparing the processing of the two functions below, we can see that `count2` uses `sc.Scan` without any `if err` judgement, which greatly simplifies the code.
This is because there is a lot of processing done in `sc.Scan`, and many similar functions that need to be read in a loop can be considered to be wrapped and processed like this. When the external package is called, it is very clean.

```golang
// 统计文件行数
func count(r io.Reader) (int, error) {
	var (
		br    = bufio.NewReader(r)
		lines int
		err   error
	)

	for {
		// 读取到换行符就说明是一行
		_, err = br.ReadString('\n')
		lines++
		if err != nil {
			break
		}
	}

	// 当错误是 EOF 的时候说明文件读取完毕了
	if err != io.EOF {
		return 0, err
	}

	return lines, err
}

func count2(r io.Reader) (int, error) {
	var (
		sc    = bufio.NewScanner(r)
		lines int
	)

	for sc.Scan() {
		lines++
	}

	return lines, sc.Err()
}
```

#### error writer

Let's see an example from go blog <https://blog.golang.org/errors-are-values> :

```golang
_, err = fd.Write(p0[a:b])
if err != nil {
    return err
}
_, err = fd.Write(p1[c:d])
if err != nil {
    return err
}
_, err = fd.Write(p2[e:f])
if err != nil {
    return err
}
// and so on
```

errWriter

```golang
type errWriter struct {
    w   io.Writer
    err error
}

func (ew *errWriter) write(buf []byte) {
    if ew.err != nil {
        return
    }
    _, ew.err = ew.w.Write(buf)
}

// 使用时
ew := &errWriter{w: fd}
ew.write(p0[a:b])
ew.write(p1[c:d])
ew.write(p2[e:f])
// and so on
if ew.err != nil {
    return ew.err
}
```

Also occurs in `bufio.Writer`. The duplicate logic is encapsulated and the error is staged, so that we only need to judge the error at the end.

### `errors.Is()` and `errors.As()`

```golang
func Is(err, target error) bool {
	if target == nil {
		return err == target
	}
	// 通过反射判读 target 是否可以被比较
	isComparable := reflectlite.TypeOf(target).Comparable()
	for {
        // 循环判断是否相等
		if isComparable && err == target {
			return true
		}
        // 判断是否实现了 is 接口，如果有实现就直接判断
		if x, ok := err.(interface{ Is(error) bool }); ok && x.Is(target) {
			return true
		}

		// 去判断是否实现了 unwrap 的接口，如果实现了就进行 unwrap
		if err = Unwrap(err); err == nil {
			return false
		}
	}
}

// unwrap 进行比较，只要有一个相同就返回，如果一直到底都不行就返回 false
func As(err error, target interface{}) bool {
	if target == nil {
		panic("errors: target cannot be nil")
	}
	val := reflectlite.ValueOf(target)
	typ := val.Type()
	if typ.Kind() != reflectlite.Ptr || val.IsNil() {
		panic("errors: target must be a non-nil pointer")
	}
	if e := typ.Elem(); e.Kind() != reflectlite.Interface && !e.Implements(errorType) {
		panic("errors: *target must be interface or implement error")
	}
	targetType := typ.Elem()
	for err != nil {
		if reflectlite.TypeOf(err).AssignableTo(targetType) {
			val.Elem().Set(reflectlite.ValueOf(err))
			return true
		}
		if x, ok := err.(interface{ As(interface{}) bool }); ok && x.As(target) {
			return true
		}
		err = Unwrap(err)
	}
	return false
}
```
