---
layout: page
title: Google Cloud Digital Leader Certification Flaw Sweeper
subtitle: GCP CDL notes by M." B.U.T.A"O.
---

- What is the no-code data pipeline tool?
  - Data Fusion - similar to CDAP

- Dataproc - like Hadoop/Spark - Parallel Computing - Stream Computing

- Dataflow- Apache Beam - Stream Processing and batch processing

- Cloud Composer - like Airflow - Workflow Management - 小规模任务调度

Dataflow是Google Cloud的一款拳头产品。Dataflow上提供了对数据批处理 (Batch Processing) 和流处理 (Streaming Processing) 的能力。简单的来说，可以把Dataflow想象成跑在云上的一个Hadoop+Storm共同体。
Apache Beam是一套用来编写数据处理任务的API，Beam旨在提供一种统一的API来编写批处理和流处理Job，也就是说可以实现同一套代码，既可以用来做批处理，也可以用来做流处理。需要注意的是，Beam本身并不处理数据，而是用来描述一个数据处理任务应该如何进行的，真正运行处理的是Runner，现在比较常见的，并且支持Beam的Runner有Google Dataflow，Flink，Spark，Heron（手动狗头）等。Beam就是Google Dataflow的底层实现，也就是说，Google Dataflow就是Beam的一个Runner。

Dataproc 是一项托管式 Spark 和 Hadoop 服务

Data Fusion:  build and manage ETL/ELT data pipelines. CDAP

What is GCP dataprep?
Dataprep by Trifacta is an intelligent data service for visually exploring, cleaning, and preparing structured and unstructured data for analysis, reporting, and machine learning. Because Dataprep is serverless and works at any scale, there is no infrastructure to deploy or manage. Data prep - wrangle data based on tabular, interactive, visual structure.

Cloud Composer是一个任务流托管服务

-------------------------

* Data Fusion, a codeless environment for creating data pipelines using a drag-and-drop interface. Data Fusion actually uses Dataproc as its Compute Engine, so everything we have mentioned earlier applies also to the case of Data Fusion. If your team prefers to create data pipelines without having to write any code, Data Fusion is the right tool.

* Dataflow - you have to write code.  Either Java or Python, as of this writing.

* Dataproc - is used to run Hadoop/Spark workloads.  Requires coding.

* Datastream - this is not used for data processing. Used to replicate and synchronize data.

References:

* https://cloud.google.com/blog/products/data-analytics/building-the-data-engineering-driven-organization

* https://cloud.google.com/data-fusion

-------------------------

- Scaling types and their differences?
  - Horizontal scaling, also called scaling out, adds new VMs to increase application capacity.
  - Vertical scaling, also called scaling up, keeps the number of resources (like VMs) constant but increases its power/performance by increasing number of CPUs, RAM, storage, etc.

- There is no such thing as triangular or circular scaling. 

-------------------------

- No Code App
  - AppSheet

-------------------------

- Capital Expenditure (CapEx) vs. Operational Expenditure (OpEx)
  - Captal expenditure (CapEx) is the cost of purchasing or upgrading a long-term asset, such as a building or a piece of equipment. CapEx is often paid for with cash or a loan, and the asset is depreciated over time.
  - Operational expenditure (OpEx) is the cost of running a business on a day-to-day basis. OpEx is often paid for with cash or a credit card, and the cost is expensed in the period in which it is incurred.

- Primary source of expenditure on public cloud?
  - CapEx is an approach where you pay for the expenses up front. In the OpEx model, you pay for resources as you use them. The cloud uses the OpEx model.

-------------------------

Nearline Storage vs standard storage vs Coldline storage vs Archival storage:
- Nearline Storage is a low-cost storage option that is designed for data that is accessed less frequently. Nearline Storage is ideal for data that is accessed once a month or less.
- Standard Storage is a high-performance storage option that is designed for frequently accessed data. Standard Storage is ideal for data that is accessed once a day or more.
- Coldline storage is for data that is accessed infrequently and requires rapid access when needed. e.g. for data that is not accessed for more than 30 days, but may need to be accessed within 24 hours.
- Archival storage is for data that is accessed infrequently and requires long-term storage. e.g. for data that is not accessed for more than 180 days, but may need to be accessed within 7 days.

- Cloud storage supports Object Lifecycle Management. To support common use cases like setting a Time to Live (TTL) for objects, retaining noncurrent versions of objects, or "downgrading" storage classes of objects to help manage costs, Cloud Storage offers the Object Lifecycle Management feature.

Standard storage is recommended for frequently accessed data and Archive for data accessed less than once a year. Nearline, Coldline, and Archive offer ultra low-cost, highly-durable, highly available archival storage. For data accessed less than once a year, Archive is a cost-effective storage option for long-term preservation of data. Coldline is also ideal for cold storage—data your business expects to touch less than once a quarter. For warmer storage, choose Nearline: data you expect to access less than once a month, but possibly multiple times throughout the year.



Additional notes based on a question that was asked:

From a blog post: In the case of "hot" or "standard" storage, the contract has a higher per-GB monthly storage price, but there are no additional per-GB fees for retrieval or early deletion. For "cooler" storage classes, your monthly per-GB storage costs can be much lower, and you will need to consider per-GB fees for retrieval and for early deletion.

Ref: https://cloud.google.com/blog/products/storage-data-transfer/how-to-save-on-google-cloud-storage-costs

The graph on that page also gives you a comparison of costs which is a combination of how much you store and how often you retrieve it. (https://storage.googleapis.com/gweb-cloudblog-publish/images/visualization.max-2000x2000.jpg)    Data that is frequently accessed will therefore be most cost optimal on standard rather than any of the others.

-------------------------

about 50TB of data from S3 to GCS

* Storage Transfer Service provides options that make data transfers and synchronization easier. We can also schedule one-time transfer operations or recurring transfer operations.

* gsutil is preferable for smaller data transfers.  Setting up recurring transfers is also difficult.

* Data is not big enough for Transfer Appliance.  Unnecessary to download S3 data to on-premise and then again load it up on Transfer Appliance.

* It would be cumbersome, time-consuming, and inefficient to transfer so much data via the console's drag and drop.

References:

* https://cloud.google.com/storage-transfer/docs/overview

* https://cloud.google.com/architecture/transferring-data-from-amazon-s3-to-cloud-storage-using-vpc-service-controls-and-storage-transfer-service

-------------------------

About discounts
* Compute Engine lets you purchase committed use contracts in return for deeply discounted prices for VM usage. These discounts are referred to as committed use discounts.  Committed use discounts are ideal for workloads with predictable resource needs. When you purchase a committed use contract, you purchase Compute Engine resources—such as vCPUs, memory, GPUs, local SSDs, and sole-tenant nodes—at a discounted price in return for committing to paying for those resources for 1 year or 3 years. The discount is up to 57% for most resources like machine types or GPUs. The discount is up to 70% for memory-optimized machine types.

* A sustained use discount doesn't have to be asked for.  It will automatically be applied.

* It might be possible to negotiate with other cloud vendors based on this, but a change might take much longer.  Also even if a slightly better pricing was received only on compute, a move of other workloads might not have a positive impact.

* Cutting down VMs will mean less capacity to serve user requests.

-------------------------

AppEngine Standard and Cloud Functions are serverless options.  It is not possible to run databases on them.

-------------------------

* AutoML Vision Edge model can be deployed to one of several types of edge devices, such as mobile phones, ARM-based devices, and the Coral Edge TPU.

-------------------------

Containers and kubernetes are ideal for the kind of requirement mentioned here - separate microservices that need to scale independently.

-------------------------

The resource hierarchy permissions are additive and a union of the permissions above it. If a resource higher up has given a permission, a lower level resource cannot revoke it.

-------------------------

It is generally recommended that application to use that work together be moved together.

Imagine if you did not move all tiers together. Then, for example, the frontend will be on Google Cloud while the backend and DB will be on premise. The front end will have to communicate all the time across the network. That is going to be slow and error prone. Similarly if you move any of the other tiers without moving all.

-------------------------

* Multi-region option will use multiple datacenters that are within the European Union.  More regions will also help with lower latency since users are spread across the EU.

* Dual-region will have lesser datacenters being used.  Though the data is guaranteed to be within the EU, the latency for users could be higher.

* So also for the single region storage, that the latency increases for end users.

* Cloud Filestore is an NFS storage.  It is attached to VMs and mostly used for internal shared usage.  It is not the ideal product for serving end users via web browsers.

-------------------------

* Integrated repository for analytics and ML: The highest level of availability and performance within a single region is ideal for compute, analytics, and machine learning workloads in a particular region. Cloud Storage is also strongly consistent, giving you confidence and accuracy in analytics workloads.

* dual-region and multi-region are useful for redundancy, but it would be costlier for large scale analytics workloads.

* The storage classes on Cloud Storage are charged on two parameters - how much you store and how often you retrieve it. Since this question requires that the data be read very often, nearline storage is going to end up costing you more than standard storage.

-------------------------

Your team is using BigQuery as your central data warehouse.  You are in an experimental phase with your analytics project.  Which of the following would be an appropriate pricing model to use?

-- On-demand pricing

* Since we are experimenting, we don't have a good estimate on how much processing will be done.  With the on-demand pricing model, you are charged for the number of bytes processed by each query. The per-byte-scanned billing model can be advantageous in that you pay precisely for what you use, with the amount of scanned data as a proxy for compute consumption.

* BigQuery Monthly and Annual reservations can be used for cost predictability and to provide guaranteed capacity for workloads with SLAs.

* BigQuery Flex Slots for cyclical workloads that require extra capacity, or for workloads that need to process a lot of data in a short time, and so would be less expensive to run using reserved slots for a short time.

* 1 TB per month might not cover your analytics needs, except for the smallest, temporary projects.  It's better to plan to get better pricing.

-------------------------

Chronicle is a cloud service, built as a specialized layer on top of core Google infrastructure, designed for enterprises to privately retain, analyze, and search the massive amounts of security and network telemetry they generate. Chronicle normalizes, indexes, correlates, and analyzes the data to provide instant analysis and context on risky activity.

* Cloud Logging is not a place to retain or analyze external logs.

* Building a custom solution is too roundabout.  Furthermore, the global threat intelligence that Google's team brings is not available

-------------------------

* IDaaS - provides a centralized identity management for user credentials, authentication, and possibly authorization

-------------------------

About log-in:

* Cloud Identity is natively in Google Cloud, integrates well with other applications.  These contract based agents also does not need to be given tools like Gmail, Slides, Sheets, etc.

* Google Workspace also comes with Gmail, Slides, Sheets, etc., which is not required for this group.

* Cloud Identity could work with OpenId, SAML solutions from any provider, however it increases the dev and IT overhead, and it wouldn't be preferred as a first option.

-------------------------

Firebase v.s. CloudSQL

* Firebase/Firestore is easy to build and is suitable for user information that could vary in structure/schema.

* Cloud Spanner is suitable for large scale, global, SQL based, transactionr requirements.

* Cloud SQL is also a SQL based transaction database. These databases have stricter structure. A quick database to hold varying data information is Firebase/Firestore.

* Cloud Storage stores entire files and is not suitable for holding information like user credentials and information.

-------------------------

* Cloud SQL supports MySQL, PostgreSQL, Microsoft SQL Server

-------------------------

* Even when using compute optimized machines, they still use CPUs.  Those are great for general computing tasks.  GPUs are optimized for number crunching.

-------------------------

* Compute Engine VMs are the preferred compute option as they are long running.

* Cloud Run and Cloud Functions are primarily for event driven, stateless jobs.

* Since the systems already exist on-premise, it will take more effort to migrate them to an AppEngine architecture.

-------------------------