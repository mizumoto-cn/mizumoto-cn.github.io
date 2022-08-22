---
layout: page
title: AWS SAA-C02 - Domains
subtitle: AWS notes by M." B.U.T.A"O.
---

## Domains

### Design Resilient Architecture

- reliable and resilient storage
  - EFS // TODO
  - EBS // TODO
  - S3 // TODO
- design decoupling mechanisms
  - SQS //TODO
  - load balancer
  - elastic IP: decouple IP address from server
- multi-tier architecture solutions
- high availability and/or fault tolerant solutions:
  - user can access service under ant circumstances; can allow certain performance degradation
  - fault tolerance: user does not experience any issue; more strict requirements
  - RTO vs. RPO
    - Recovery Time Objective: **time** to recover from a failure without causing significant performance degradation
    - Recovery Performance Objective: the **amount of data** that can be lost before significant performance degradation occurs

#### HA: Highly Available architecture

- Always design for failure
- use multiple AZs and regions wherever you can
- multi-AZ vs. read replicas for RDS // TODO
- scaling out vs. scaling up
  - scaling out: use auto-scaling groups(add instances)
  - scaling up: increase resources inside EC2 instance (e.g. increase CPU, memory, storage)beware of the cost element
- different S3 storage classes

