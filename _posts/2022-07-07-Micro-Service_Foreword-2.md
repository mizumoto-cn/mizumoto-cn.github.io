---
layout: post
title: Foreword-2 - Service Discovery, Multi-cluster, and Multi-tenancy Part 1
subtitle: Health Check, and Service Discovery [Column - Go & Micro Services]
thumbnail-img: ""
share-img: /assets/img/path.jpg
tags: [Go, Micro-services]
---

[Last article](2022-06-26-Go-MicroServices-Forword-1.md) we talked about why shall we use **globally consistent** inter-service communication tools such as gRPC.

And now, after we discussed the definition of microservices, how shall we expose them to the public, etc. In addition to the exposure to the public, services also need to call and interact with each other, using the same communication protocol.

And that is "Health Check" and "Service Discovery".

### Health Check

`gRPC` provides a mechanism to check the health of a service.

Positive health checks can perceive the health status of a service by checking its heartbeat. When a service provider is not in a stable status, it will be marked as unhealthy and taken out of the balancing pool. It will be registered and put into the pool again when the service-registry receives its normal heartbeat signal again.

This can also be used in plug-in containers( k8s liveness and readiness)

> A typical kubernetes swift deployment example:
>
> - Kubernetes sends a terminate request to the discovery service
> - Kubernetes then sends a SIGTERM signal to the APP container, graceful quitting process shall be performed.
> - Clients, being informed by the service discovery, will be notified about the service being unavailable, and will quit in a given ttl timeout.(2 heartbeats, for example) Usually, they will qui
> - Kubernetes will force quit after timeout (10~60 seconds for most of the situations) (SIGKILL)

#### Graceful Startup&Shutdown

##### Graceful Startup

![img](/assets/img/micro-service-column/GracefulStart.svg)

- The service provider starts, and the Kubernetes startup script will check the health status of the service with a certain interval.
- Once the health status is healthy, the service registration script registers the service with the registry (rpc://ip:port).
- The consumers will regularly fetch/receive the service list from the registry.
- Consumers will send requests to the service after confirming it passes the health check.
  - and if a problem occurs with the health check, the service will be marked as unhealthy and removed from the registry list as well as the load.

##### Graceful Shutdown

![img](/assets/img/micro-service-column/GracefulShutdown.svg)

- There is an advantage to implementing it in the release deployment platform, as you don't have to implement the same logic for each application.
- It is also possible for an application to initiate a shutdown process after it has received a SIGTERM signal.
- Noted that there is an interval between registry deletion and consumer receiving the updated service list.
- registry deletion time out is usually 2 heartbeats.
- SIGKILL timeout is usually 10~60 seconds.

##### Graceful Startup&Shutdown in Gin

