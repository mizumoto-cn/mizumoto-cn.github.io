---
layout: page
title: Google Cloud Digital Leader Certification ABOUT
subtitle: GCP CDL notes by M." B.U.T.A"O.
---

## Before the Exam

- Practice on Examtopics
  - <https://www.examtopics.com/exams/google/cloud-digital-leader>
- [Flaw Sweeper](./CDL_FlawSweeper.md)
- [Flaw Sweeper - 2](./CDL_Flawsweeper2.md)
- [Flaw Sweeper - 3](./CDL_FlawSweeper3.md)

## Note

### Types of Cloud Computing

- Saas(Software as a Service)
  - e.g. Google Workspace/ Office 365...
  - Product provided and run by service provider
  - It just works and remains available
  - You don't need to worry about the infrastructure
- Paas(Platform as a Service)
  - e.g. Google App Engine
  - You can run your own code on the service provider's infrastructure
  - You don't need to worry about the infrastructure like provisioning, configuring or understanding the underlying hardware or OS
- IaaS(Infrastructure as a Service)
  - e.g. Google Cloud
  - Basic blocks of cloud computing, providing access to 
  - You can run your own code on the service provider's infrastructure
  - You need to worry about the IT staff, data centers and hardware

### Shared Responsibility Model

If you can configure or store it then you are responsible for it.

IaaS PaaS SaaS FaaS

#### IaaS

This means you are basically responsible for everything

- Compute Engine - Bare Metal 
  - > 裸机服务器是仅供一个消费者或租户使用的物理计算机服务器
  - Customer
    - Host OS Configuration
    - Hypervisor
  - Google
    - Physical Hardware

- Compute Engine - Virtual Machine
  - Customer
    - The Guest OS
    - Container Runtime
      - You can check the box on if you want a VM to have containerization, and that will make it Google's responsibility, but you can install it very much yourself which will make it your responsibility.
  - Google
    - Hypervisor, Physical Hardware

- Containers - GKE(Google Kubernetes Engine)
  - Customer
    - Container Configuration
    - Deployment of Containers
    - Storage
  - Google
    - OS, Hypervisor, Physical Hardware
  
#### PaaS

- Managed Platform - App Engine
  - Customer
    - Application Code
    - Environment Configuration
    - Deployment strategy
    - Configuration of services related to the application
  - Google
    - Server, OS, Networking, Storage, Security

#### SaaS

- Word Processor - Google Docs
  - Customer
    - Document content
    - Management of files
    - Configuration of sharing access control
  - Google
    - Server, OS, Networking, Storage, Security

#### FaaS

- Functions - Cloud Functions
  - Customer
    - Upload code
  - Google
    - Deployment, Container Runtime, Networking, Storage, Security, Physical Hardware(Almost everything)
- Serverless Container - Cloud Run

#### Dedicate Host - Sole-tenant Node

Sole-tenant Node: A node that is dedicated to a single customer, you are the only person on that physical machine.

#### Conclusion

| \ | Bare Metal | Dedicate Host | Virtual Machine | Container |  Function |
| ---------- | ---------- | ------------- | --------------- | --------- | --------- |
| Code | √ | √ | √ | √ | √ |
| App Container | √ | √ | √ | √ | x |
| Runtime | √ | √ | √ | x | x |
| OS | √ | √ | √ | x | x |
|Virtualization | √ | x | x | x | x |

### Cloud Computing Deployment Models

- Public Cloud
  - Everything built on the Cloud Provider's infrastructure, also known as Cloud-Native.
  - [ VM + DB sitting in a subnet ] sitting in a VPC provided by the Cloud Provider
- Private Cloud
  - Everything built on company's data centers, also known as On-Premise.
  - You may need something like OpenStack to manage the infrastructure and make it look like a cloud.