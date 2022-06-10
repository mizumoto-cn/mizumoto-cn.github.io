---
layout: post
title: `IDisposable` Interface in C#
subtitle: 
cover-img: /assets/img/path.jpg
thumbnail-img: /assets/img/thumb.png
share-img: /assets/img/path.jpg
tags: [C#]
---

## C#中的`IDisposable`接口

首先，我们应该明确的一点是：`IDisposable`是C#用于释放非托管资源的一种接口。

[MSDN - IDisposable Interface (System)](https://docs.microsoft.com/en-us/dotnet/api/system.idisposable?redirectedfrom=MSDN&view=netframework-4.8)
> The primary use of this interface is to release unmanaged resources. 

这句话重点在于<u>release</u>和<u>unmanaged</u>两点。
IDispose接口最初而最重要的定位便是管理不受CLR控制的资源。

---

#### `Dispose()`方法并非析构函数

 在很多实现中`IDisposable`接口被一定程度上滥用了。<br />
值得注意的,`Dispose()`方法并不能说就等同于C语言中的`free()`。<br />
由于托管资源的回收由GC处理，在大多数时候时候立刻调用`Dispose()`方法将 引用
赋值设为`null`并不能即时回收内存。

在C++中，析构函数(Destructor)是这样定义的一类函数

> a destructor (dtor) is a method which is automatically invoked 
> when the object is destroyed.

C++等语言的析构函数并不像C#一样对`Dispose()`方法有这样或者那样的限制。
因为析构函数并不具有“传染性”。C\+\+本身并没有垃圾回收机制，所有的
Cleanup工作都需要析构函数去完成。<br />

但是在C#中，托管资源的Cleanup工作由GC去完成，`IDisposable`接口只应被用于
非托管资源 的释放。

C#的类型分为普通类型和非普通类型，非普通类型包含普通的类型自身和非托管资源。
那么，如果类的某个字段或属性是非普通类型，那么这个类型也应该是非普通类型，
也应实现IDisposable接口。

这造成了`IDisposable`接口的**传染性**。

>根据微软的编程规范，对于所有实现了`IDisposable`接口的对象，
都必须显式调用所有这些对象的`Dispose()`方法进行释放，而不能依赖GC进行回收。
在复杂情形下，这使得`Dispose()`方法调用的时机变得难以判断。就像C语言中过早地
`free()` 一块内存一样，可能会导致严重而蹊跷的内存错误。

而微软在许多常用库中对于`IDisposable`接口的滥用无疑助涨了这一点。

<p align="right">Mizumoto<br />
Wuhan, Hubei, China<br />04 - 19 - 2020</p>

[Back to HomePage](https://blog.mizumoto.ml)
