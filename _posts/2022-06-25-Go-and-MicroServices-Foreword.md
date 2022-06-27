---
layout: post
title: Foreword-0 - A brief overview of Micro-services
subtitle: Column - Go & Micro Services
thumbnail-img: ""
share-img: /assets/img/path.jpg
tags: [Go, Micro-services]
---

[Special Column: Go & Micro Services](go_index.md)

> So, before we start, let's ask ourselves a few questions. It's ok if you cannot answer it now, but I hope that we can have a clear answer later when we finish this set of articles.

1. Why are there micro-services?
2. What is a micro-service?
3. What are the pros and cons of micro-services?
4. How do we build a micro-service?
5. How do we expose a micro-service to the outside world?
6. How do we split our micro-service into smaller parts?
7. How to ensure that our micro-service is secure?

### Q1. Why are there micro-services?

<!-- markdownlint-disable MD032 MD004 -->

* Back about ten years ago, most of the internet applications were built in a way we call `monolithic architecture`, causing lots of problems.
  + Applications are too complicated for any single developer to understand.
  + Applications are not modular and difficult to make expandable. Reliability is also not guaranteed in some way.
  + Too heavy for agile development and deployment.

So smart engineers decided to separate the applications into smaller parts, according to services and functions. That is the origin of micro-services.

### Q2. What is a micro-service?

* Let's start with the opinion "SOA"(Service-Oriented Architecture)
  + By splitting the application into services, we can make the services smaller, easy to test and maintain, and easier to deploy or extend.
  + **Atomic**. Single responsibility principle. One service should only do one thing.
  + **Prototype first principle**. We should start with a prototype, defining the APIs as soon as possible.
  + **Portability is more important than efficiency**. It's rather important to have a portable interaction protocol(s) between the services.
- Micro-services can be considered a practice of the SOA. Micro-serves are also service-oriented architectures.
- What is a micro=service?
  + A micro-service is a small, self-contained unit of an application. **Built around one specific business functionality**. Light-weight communication protocol(s) used between the services. Allowing automatic deployment, and different programming languages or data storage methods can be used.

### Q3. What are the pros and cons of micro-services?

* pros:
  - easy to develop, test, deploy, maintain, and extend.
  - **atomic**. Single responsibility principle. One service should only do one thing and it shall not be split into other services.
  - **independent**. Each service is an independent process and shall stay stateless. Making it easy to get combined with containerization, fits `Kubernetes` well.
  - **isolated development**. The development of each service should be independent, avoiding mutual influences between services. Also making it possible to allocate different resources to each service according to its needs.
  - **Decentralized Governance**. Each service is independent and can be deployed anywhere.
    + **Data decentralization**. Each service can store its data in its own database, cache and other facilities. Of course, it can also communicate with other services or share a common database.
    + **Governance decentralization**. Each service can be managed by its own team.
    + **Technical decentralization**. Each service can be written in its own language as long as it is compatible with the other services. But also note that too divergent technology stacks can cause problems in management.
* cons:
  - **complex dependencies between services**. There might be hundreds of services, and each service needs to communicate with other services.
    + can be solved by using full link tracking tools like `OpenTracing`.
  - **Micro-services are born to be distributed**. So RPC or other message queue protocols(like Kafka) are necessary. **Making it necessary to write code to deal with local failures** like `slow delivery` or `unreachable services`.
    + e.g Service call traffic can be amplified easily, especially when there is a `for` call. If service A calls service B in a `for` loop, for like 10 times, then B calls C in a loop for ten times, there will be a 100 times traffic to C.
    + **common solutions**: Coarse-grained(粗粒度的) inter-process communication (batch interface, batch requests, avoiding n+1 problem), and other facilities like isolation, timeout protection, load protection,  circuit breaker, current limiting, downgrading, retry, load balancing, and so on.
  - **Distributed transaction problems**. Cross-service transaction management is not easy, as there are independent databases in most of the services.
    + **common solutions**: TCC (try confirm cancel), two-phase commit, etc.
    + You can refer to [Xiaomi's `distributed transaction`](https://xiaomi-info.github.io/2020/01/02/distributed-transaction/) for more real-world solution examples.
  - **Complicated testing**. As there are too many dependencies. It's hard to tell whether it's due to abnormal behavior or simply because of the dependencies.
    + **common solutions**: Independent testing. I'll add another solution later in the coming articles.
  - Dependency between service modules may cause update problems.
    + **Always maintain the compatibility of interfaces**. Changes in services may destroy the compatibility of service contracts, causing compatibility damage to service consumers.
    + **Be conservative when sending and be open when receiving (data)**.  This is called the "Bostar's Law": necessary messages shall be sent with minimal size, and when it comes to receiving, the message shall be received with the tolerance of the maximum redundant data. >>> compatibility.
  - High requirements of infrastructures.
    + If you aren't a huge company, just simply put everything onto the **cloud**.
    + Otherwise, you need to implement automation tools, log collection, monitoring, alarm, CI/CD, Kubernetes, etc.

### Q4. How do we build a micro-service?

> The `composition` of multiple micro-services completes a complete `usecase`.

* kit: A basic library/framework
* service: business code + kit dependency + 3rd-party dependency
* light-weight communication: rpc + message queue

### Q5. How do we expose a micro-service to the outside world?

![API gateway & micro-services](/assets/img/micro-service-column/APIgateway&microservices.png)

API gateway: routing, authorization, rate limiting, circuit breaker, load balancing, etc. Basically, the API gateway handles horizontal functions which are not business-related.

BFF(Backend for Frontend): This is a layer that mainly does the data assembly, and provides unified and user-friendly API interfaces to the client/web/mobile etc. BFF can be separated into multiple parts according to the needs or importance of the APIs.

BFF advantages:
- light-weight interaction: streamlining and aggregation of protocols.
- diverse services: data cropping and aggregation, providing client endpoints with customized APIs.
- dynamic upgrades: upgrade performs smoothly with the existing system. Upgrades only affect the services, not changing the protocols.
- improves communication efficiency. Forming a collaborative model of mobile business and gateway teams.

#### Traffic Link

* Mobile/Web/... -> API gateway -> BFF -> Micro-services
* Noted that CDNs and layer4/7 load balancers are not included.
> Nodejs SSR for pure web BFFs usually.

#### Why is micro-service not exposed directly to the outside world?

+ Directly exposing services will make it hard for the front-end developers. It also means poor compatibility and low communication efficiency.
+ It will also make it impossible for the backend developers to expand or update the services.

#### Why does there have to be an outmost API gateway?

Making upgrading business unrelated functions, such as current limiting easy.

### Q6. How do we split our micro-service into smaller parts?

* When it's not quite clear what the business is all about, we can split the service according to "department functions", such as account, finance, etc.
  - note that functions should be divided into closed loops. Don't separate the same function into different departments.
* After the system is stabilized, we can split the services according to DDD context bounds.
* If a user scenario can be solved in a closed-loop, then it shall be a single service.
* It can also be divided according to the frequency of the use case.
* It can also be divided according to the read and write access of the data.
  - CQRS: Command Query Responsibility Separation. CQRS separates the services into two parts: command and query. "Command" is the service that handles the business logic, and "query" is the service that performs queries to the database. The command side handles creation, update and delete requests and issues events when data changes. The query side handles queries by executing queries against one or more materialized views that are kept up to date by subscribing to a stream of events issued on data changes.

### Q7. How to ensure that our micro-service is secure?

![micro-service security](/assets/img/micro-service-column/APIgateway&microservices.png)

#### API Gateway

e.g. This layer does the authentication and authentication of the user. Generate a jwt token for the intranet and pass it along with the uid.

#### BFF

Check the jwt token to get the uid and user info and add it into the context. e.g. metadata in RPC, header in HTTP, etc.

#### Micro-services (Intranet)

* Identification:
  + e.g., gRPC uses certificates to identify the users.
* Authorization:
  + via RBAC (`Role-Based policies Access Control`) e.g. configuration center issues

In intranet,
* Full Trust: Assumes that intranet services are secure from each other and do nothing authentication.
* Half Trust: Authentication is required between intranet services, but not all of them need to be encrypted.
* Zero Trust: The intranet is insecure, similar to a public network, and all requests need to be encrypted after authentication to prevent sniffing.
  + [Embrace proactive security with Zero Trust](https://www.microsoft.com/en-us/security/business/zero-trust)

---

> For more of this special column, click [Go & Micro-services](/go_index.md).
