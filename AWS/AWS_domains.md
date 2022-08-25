---
layout: page
title: AWS SAA-C02 - Domains
subtitle: AWS notes by M." B.U.T.A"O.
tags: [AWS]
---

## Domains

### Design Resilient Architecture 30%

- reliable and resilient storage
  - EFS // TODO
  - EBS // TODO
  - S3 // TODO
- design decoupling mechanisms
  - SQS //TODO
  - load balancer
  - elastic IP: decouple IP addresses from the server
- multi-tier architecture solutions
- high availability and/or fault-tolerant solutions:
  - user can access service under any circumstances; can allow certain performance degradation
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

##### HA Architecture Example

![HA example](pic/HA_example.png)

##### HA Bastion Hosts

- Option1: separate hosts in different AZs; use a network load balancer with static IP address and health checks to ensure that the host is up
  - layer 4 load balancer needed, so it cannot be an application load balancer // TODO
  
![HA Bastion Host Option 1](pic/HA_bastion_1.png)

- OPtion2: one host in a single AZ behind an Auto Scaling Group with health checks and a fixed EIP,
  - if the host fails, the health check will fail and the auto-scaling group will automatically provision a new EC2 instance.
  - not 100 percent fault-tolerant, but can be used as a backup; will take some time to recover from a failure
  - **lowest cost option**

![HA Bastion Host Option 2](pic/HA_bastion_2.png)

> 总体来说，理解为`BFF层`与`Service层`即可
> 无论4层负载均衡还是Auto Scaling Group策略，与health check一起都属于BFF层
> BFF->Service(Public SN)->DB(Private SN)

> 这里这么说只是为了帮助理解，BFF层的存在意义是进行鉴权、安全、限流、数据转换与组装等与业务无关的逻辑等业务无关逻辑的处理

### Define Performant Solutions 28%

> Performant means that the service is fast and reliable

- performant storage and databases
  - EBS: different types of storage classes //TODO
  - S3: host static files (instead of keeping them in the EC2 instance)
  - RDS vs. MongoDB vs. Redshift
    - replicas
- caching
- design solutions for elasticity and scalability

#### HPC: High Performance Computing

- data transfer: See [Jayendra's Blog](https://jayendrapatil.com/aws-data-transfer-services/) // TODO
  - Snowball Snowmobile // TODO
  - DataSync // TODO
  - Direct Connect
- cache
  - CloudFront // TODO
  - API Gateway
  - ElastiCache - Memcached and Redis
  - DynamoDB Accelerator (DAX) // TODO
- compute and network
  - EC2 instances(GPU, CPU optimized)
  - [EC2 fleets](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet.html) (e.g. spot fleets)
  - placement groups (cluster placement groups for low latency)
  - enhanced networking (e.g. ENA, VF, EFA) // TODO
- storage
  - instance-attached storage 
    - EBS
    - instance-store volumes
  - network storage
    - S3 : Distributed Object-based Storage; not a file system
    - EFS: scale IOPS based on total size, or use provisioned IOPS //TODO
    - FSx or Lustre: HPC-optimized distributed file system; millions of IOPS; backed by S3
  - orchestration and automation 服务调度编排与自动化
    - AWS Batch: run many batch computation jobs
    - AWS ParallelCLuster

### Specify Secure Applications and Architectures 24%

- secure application tier
- secure data
  - in transit
    - SSL
    - VPN
    - Snowball // TODO
  - at rest
    - data on S3 is private by default and need credentials to access
- networking infrastructure for VPC
  - subnets
  - security groups and NACLs (network access control lists)
  - IGW (internet gateway); NAT gateway/instance
  - bastion hosts
- shared responsibility model
  - AWS responsibility: AZ, region, edge locations, EC2 // TODO edge locations are the locations where the service is deployed.(?)
- principle of least privilege*

### Design Cost-optimized Architecture 18%

- storage
- compute
- serverless architecture
- CloudFront // TODO
  - no charge for data transfer between CloudFront and S3
- key principles
  - pay as you need
  - pay less when reserved
  - pay less per unit when use more

### Define Operationally Excellent Architectures 0%

- prepare operate update
- perform operations with code
- annotate documentation
- make frequent, small, reversible changes
- refine operations procedures frequently
- anticipate failure // 预见错误
- related services
  - AWS config //TODO
  - CloudFormation //TODO
  - VPC flow logs //TODO
  - CloudTrail //TODO
  - CloudWatch //TODO
  - AWS Trusted Advisor //TODO
  
