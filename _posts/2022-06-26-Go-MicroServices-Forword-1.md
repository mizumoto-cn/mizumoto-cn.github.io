---
layout: post
title: Foreword-1 - Service Discovery, Multi-cluster, and Multi-tenancy
subtitle: Column - Go & Micro Services
thumbnail-img: ""
share-img: /assets/img/path.jpg
tags: [Go, Micro-services]
---

In the [previous article](2022-06-25-Go-and-MicroServices-Foreword.md), we talked about the definition of microservices, their pros and cons, how shall we expose them to the public, etc. In addition to the exposure to the public, services also need to call and interact with each other.

What protocols shall we use between different services? How do we implement service discovery, how can we ensure smooth release and restart of services, how to solve the test environment problems? These questions are all waiting to be answered.

### Inter-service communication tool: gRPC

<!-- markdownlint-disable MD032 MD004 -->

* Why gRPC?
  - **gRPC is language neutral**, it can be used with any language.
  - **gRPC is light-weight and has high performance**. Supports `Json` and `Protocol Buffer` as data serializer, generates data structures, server-side interfaces and client-side Stubs in a given language via proto-3 tools.
  - **Pluggable**
  - **Interface define language** -- Services defined according to the files, and code itself serves as documentation.
  - On mobile endpoints: gRPC is built on **standard http 2.0 protocol**, supports **bidirectional streaming, header compression, TCP multiplexing, and other features like server-side push**. These features makes gRPC more power-efficient and more net-traffic saving on mobile devices.
  - **Services rather than objects, messages rather than references**: Coarse-grained messaging interaction design philosophy.
  - **Protocol payload independent**: Different services may use different protocols, like `JSON`/`XML`/`Thrift` and `Protocol Buffer`.
  - Streaming: streaming APIs.
  - **Blocking and non-blocking**: support both blocking synchronous and asynchronous message sequences between clients and servers.
  - **Metadata exchange**: common cross-cutting concerns, such as authentication or tracking, rely on data exchange.
  - **Standardized status codes**: clients respond to errors returned by the APIs in a limited way.
* **Why shouldn't simply use `restful`**?
  - SDKs must be rewritten for each client, complex and error-prone.
  - Documentations required for each SDK, hard to maintain, especially during updates.
  - Performance not so good. `Json` is not aa good a choice as `protobuf`.
  - Based on http 1.1, which is a single connection, not multiplexing, wasteful in intranet environments.
  - **`restful` is a loose protocol**, it has no strict standards, making different developers/teams come out with different codes, very error-prone.

> See [mizumoto-cn/TRPcG](https://github.com/mizumoto-cn/TRPcG) for my example of gRPC/Protobuf-based RPC framework. Supporting customized serializer including `Json`, `Protobuf`, etc..

> Some of my thoughts:
> 
> Standardization first, performance optimization second.
> 
> How can we determine if a link discovery is a topological ring?
> > Good authority determinations can help you to determine if a link discovery is a topological ring.

### Health Check, graceful deployment, and graceful shutdown