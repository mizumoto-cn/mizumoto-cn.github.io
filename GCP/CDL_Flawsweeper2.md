---
layout: page
title: Google Cloud Digital Leader Certification Flaw Sweeper 2
subtitle: GCP CDL notes by M." B.U.T.A"O.
---

## Billing

BigQuery Flex Slots for cyclical workloads that require extra capacity, or for workloads that need to process a lot of data in a short time, and so would be less expensive to run using reserved slots for a short time.

-------------------------

## Migration

### Regulations

* Moving to Google Cloud is not an all or nothing option.  Certain workloads can continue to remain on-premise while the predominant chunk moves to Google Cloud. Customers can take advantage of Google Cloud and communicate with the on-premise systems as and when required. For communication they can even have high-bandwidth access through hybrid networking options.

* Regulations have to be strictly followed.  They are not guidelines or optional. 

* Not moving to Google would be a competitive disadvantage and risk.  This is not a strategically useful decision.

* Changes to regulations might take a long time.  This company will continue to be at a competitive disadvantage until then.

### Types of Migrations

There are three major types of migrations:
- Lift and shift
- Improve and move
- Remove and replace (sometimes called rip and replace)
In the following sections, each type of migration is defined with examples of when to use each type.

**Lift and shift**

如果工作负载可在目标环境中按原样运行，或者完全没有或几乎没有更改工作负载的业务需求，那么直接原样迁移是理想的选择。由于重构量最小，因此此类迁移所耗时间最少。是最容易执行的是最快的。直接原样迁移产生的是在目标环境中运行的非云原生工作负载。这些工作负载没有充分利用云平台功能

**Improve and move**

在迁移工作负载时实现负载的现代化。“改进并迁移”所需的时间比直接原样迁移的长，因为必须对它们进行重构才能迁移应用。您需要将所耗费的额外时间和精力都评估计入应用生命周期的一部分。
“改进并迁移”还需要您掌握新的技能。

**Remove and replace**

在“移除并替换”迁移中，您将停用现有应用，完全重新设计并将其重写为云原生应用。够充分利用横向可伸缩性、高度代管式服务和高可用性等 Google Cloud 功能。因为您从头开始重写该应用，所以也消除了现有旧版应用的技术债务。

但是，“移除并替换”迁移可能比直接原样迁移或“改进并迁移”花费的时间都长。此外，由于需要重写应用，所以此类迁移不适合现成的应用。您需要将重新设计和重写应用所耗的额外时间和精力都评估计入应用生命周期的一部分。执行“移除并替换”迁移还需要新技能。您需要使用新的工具链来预配和配置新环境，并在该环境中部署应用。

#### 例题

1. A customer having a lease on their current datacenter for another 3 years wants to migrate to GCP after the lease expires. Their current applications are very old, some part of it is current, while some use older technical approaches. What type of migration should they use?

- Improve and move

2. A customer wants to migrate their applications to Google Cloud. The workloads have to be moved quickly. The current datacenter runs the applications on regular VMs, but they need to scale horizontally in the future to accommodate growing workloads. Which migration strategy would you recommend for them?

- Lift and shift. The applications don't require any specific hardware and therefore can be easily migrated.

### Simple Services to Migrate First

### Migrating VM Images

Migrate for Compute Engine gives you miinimal cut over time. Imaging a system and restoring it and a fresh install will both have significantly higher downtime. Artifiact Registry is not for storing compute OS images.

### Wait until you know the type of processor you need C/G/TPU

Different processors are suitable for different kinds of workloads. You don't usually jump between different hardware types. Though it is possible in a few cases and it can also be programmed to do so, it is better to start off with a suitable processor for a specific kind of workload.

### Getting an inventory of the local VMs (like 1000 VMs)

An automated VM discovery tool is the best option. Cloud Asset Inventory runs within Google Cloud only. All other options will give you suboptimal results - VM lists that potenially outdated or irrelevant. The hardware vendor won't have information about VMs that are running. 

-------------------------

## Security

### When Public Service Got Bot DDoSed

* Bots attacking the application is the most likely scenario in this case.  Using WAAP is the right protection plan: Anti-DDoS, anti-bot, WAF, and API protection help you protect against new and existing threats while helping you keep your apps and APIs compliant and continuously available.

* IAP would restrict it to known internal users.  Since this is a public app allowing other forms of registration, IAP cannot be used.

* Cloud Armor provides DDoS protection for applications.  It can also "Filter your incoming traffic based on IPv4 and IPv6 addresses or CIDRs. Enforce geography-based access controls to allow or deny traffic based on source geo using Google’s geoIP mapping."

* Firewall rules are for traffic which is already within the VPC.  We want to stop this spurious traffic even earlier.

* Cloud NAT does not provide DDoS protection.

### worries that somebody would make a misconfiguration or compliance violation thus exposing the company to data and privacy loss.

* Security Command Center is the right tool for this use case.  It can check resources for security issues and notify you with when issues are found.

* DDoS protection is the not the key issue here.  The problem is misconfigurations leading to exploitation.

* DLP is for removing sensitive information from data.  This doesn't protect again IT misconfigurations.

* Cloud Identity Aware proxy supports centralized identity management for access to apps and VMs.  However, it is not able to identify misconfigurations or notify you of such issues.

-------------------------

## Anthos & Multi-Clouds

A software product development company has development, test, and operations teams working together.  The entire software development pipeline uses VMs.  They are moving their entire dev environment to Google Cloud. In the past, attempts at improving process speed hit hurdles around inconsistent environments between development, test, and operations.  What could be a good approach for them on Google Cloud?

* Anthos is a good fit for this requirement.  Anthos uses containers and can create a consistent environment between software development stages. It can help you build a secure, scalable, automated CI/CD pipeline.

* Just using Cloud Build or Jenkins to change the CI/CD process does not meet the other requirements, like inconsistent production environments and differences between dev and prod environments.

* Allowing Dev and Test to use one environment and production to use another will again lead to inconsistencies.

* "Migrate for Anthos and GKE makes it fast and easy to modernize traditional applications away from virtual machines and into native containers. Our unique automated approach extracts the critical application elements from the VM so you can easily insert those elements into containers in Google Kubernetes Engine or Anthos clusters without the VM layers (like Guest OS) that become unnecessary with containers."

* Migrate for Compute moves VMs as VMs.

* The requirement is not to only move Databases.

* VMs are not a workload supported by k8s. ** Cannot be directly migrated"".

-------------------------

## Networking

One of your customers used to have a private data center.  While within their data center itself, they were consuming some Google services via API calls and other public, well known addresses published by Google.  Now they're evacuating their private data center and are moving to Google Cloud.  Could they improve some of their existing architecture with respect to security?

* "VM instances that only have internal IP addresses (no external IP addresses) can use Private Google Access. They can reach the external IP addresses of Google APIs and services. If you disable Private Google Access, the VM instances can no longer reach Google APIs and services; they can only send traffic within the VPC network."

* There is no Google Cloud organization to peer or share networks with. 

* Using private addresses alone, the public services cannot be accessed, even if your VMs are running within GCP.

### Router VPN NAT FIrewall diff

* "Cloud NAT, Google Cloud's managed Network Address Translation service, enables you to provision your application instances without public IP addresses while also allowing them to access the internet"

* Cloud VPN is used to secure traffic between two well known networks.  It is not for public internet access from general end users. Cloud VPN securely extends your peer network to Google's network through an IPsec VPN tunnel. Traffic is encrypted and travels between the two networks over the public internet. Cloud VPN is useful for low-volume data connections. For additional connection options, see the Hybrid Connectivity product page.

* Firewall rules - creating public IP addresses and then denying public traffic is not a good idea.

* Cloud Router enables you to dynamically exchange routes between your Virtual Private Cloud (VPC) and on-premises networks by using Border Gateway Protocol (BGP).

### Point2Point Network? VPN

* Dedicated Interconnect is for hybrid connectivity to Google Cloud.  It is a long term solution with high capacity that is excessive for this requirement.
  (Local Datacenter <---> GCP VPC)

* Partner Interconnect is also a long term solution with potentially high capacity.  Setting it up takes time and is not suitable for this requirement.

* Exposing a VM to the public internet is not secure.

-------------------------

## Storage

### Spanner

《Spanner: Google’s Globally-Distributed Database》，其中介绍了谷歌第二代的数据库，也就是Bigtable的继任者——Spanner。在使用Bigtable的过程中，谷歌的开发人员逐渐意识到Bigtable的一些不足之处，比如不能处理变化的数据格式，不能保证大范围内数据库的一致性以及对跨行事务的处理。谷歌为了解决这些问题，开发出了Spanner。

使用SQL的谷歌数据库有：CloudSQL、Spanner、BigQuery。CloudSQL是谷歌的关系型数据库，Spanner是谷歌的分布式数据库，BigQuery是谷歌的大数据分析数据库。

### Only want to know what's changed in the data stored in the GCS

* Object versioning on Cloud Storage is the easiest way.

* Writing a Cloud Function and analysing it in a database is unnecessary extra work.

-------------------------

## SLO SLA SLI

- SLA （service level agreement）:服务等级协议
    - 指的是整个协议，协议的内容包含了SLI，SLO以及恢复的方式和时间等等一系列所构成的协议
- SLI（service level indicator）:服务等级指标
    - 指的是对象，例如：qps，响应时间，准确性等
- SLO（service level objective）:服务等级目标
    - 指的是目标，例如：qps 99.99% ，响应时间10ms等

### HA when negotiating SLA-level with customers

e.g. you mean four 9s, customer wants five 9s

* Even though 0.0009 % increase it looks like a small increment, an addition of a single 9 reduces the possible downtime by 10 times.  So the effort is often much greater. 

* In many cases, customers might not know the implications of the 9s with respect to scheduled maintenance, upgrades, etc.  It's possible that they are holding unnecessary expectations that significantly exceed their requirements.  So a discussion to clarify that would be good.

-------------------------

## ML

### 过拟合 Overfitting

Training data set is too small, or the model is too complex.

### extracting text and recognize picture stamps from a document

* Cloud Vision API allows you to programmatically identify images, text, etc. in the document.  This would be the best option.

* AutoML Vision will help you identify a specify label.  You'll have to do more custom work to extract the different text.

* TensorFlow is a possibility, but you will have to spend more time writing the code, validating it, testing it, etc.  No reason to take this when there is an easier option.

* Data Labeling service is offline.  It also works in larger volumes.  Can't integrate into a continuous data pipeline.

### labelling

* Google's Data Labeling Service lets you work with human labelers to generate highly accurate labels for a collection of data that you can use in machine learning models.

-------------------------

## Data Analytics

### Move someone's own data analytics store to GCP

* BigQuery is the data warehousing option on Google Cloud.  Since the source data has already been used for analysis, it should easily fit the BigQuery structure too.

* Cloud Spanner is built for OLTP workloads and not OLAP workloads. 事物处理而非分析处理

* Bigtable is a NoSQL database and is not suitable for analytics.

* Migrating to multiple databases is not useful because we want a centralized data warehouse.

-------------------------

## Data Management

### Chaching

* Cloud Memorystore is an in-memory database that has sub-millisecond latency.  This is ideal for caching application data that also changes once in a while.

* Cloud Storage is useful for static files more than frequently changing application data. 

### USer Transaction Oriented SQL to Cloud: Spanner

* Cloud Spanner is a global scale SQL database that scales extremely well.  That would be the best choice.

* Cloud SQL is regional and will have limitations on multiple writes from different parts of the world.

* Bigtable is a NoSQL database.  It has tremendous scale, but you will have to rewrite the application data layer.

* BigQuery is an analytics database and not suited well for transactional systems.