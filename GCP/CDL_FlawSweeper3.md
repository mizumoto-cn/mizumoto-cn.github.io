---
layout: page
title: Google Cloud Digital Leader Certification Flaw Sweeper 2
subtitle: GCP CDL notes by M." B.U.T.A"O.
---

## Performance Analysis

* Cloud Profiler continuously analyzes the performance of CPU or memory-intensive functions executed across an application. Cloud Profiler presents the call hierarchy and resource consumption of the relevant function in an interactive flame graph that helps developers understand which paths consume the most resources and the different ways in which their code is actually called.

* Adding logging statements does not do a good job of showing performance data.  Though possible, it adds other problems of changing the performance data.

* Cloud Trace is used for analyzing latency.

## High Serenity Authentication

* Titan Security Keys provide the highest level of security.

* Google Authenticator app is the next best thing after the Titan Security Keys.  But if somebody gets access to your phone, then it could be compromised.

* SMS and Email based 2FA are not recommended as an option for greater levels of security.

## ML Fetching Car Brand from Pictures

* It would be most straightforward to use AutoML Image.  Put the images in Cloud Storage, point to it from AutoML, and start the model building process.

* Cloud Vision AI is a minor possibility.  It is able to detect logos, but I don't think it can detect brands within that, especially different car models.  We will need to build a custom model for that.

* TensorFlow models will be way more involved and time consuming build.  They won't be able to build something good within that time.

* Deep Learning Containers provide the environment, but the model still needs to be manually built.  Again, won't finish within the hackathon timeline.

## Support Level

* Premium Support will have a 15-minute response time with 24/7 response for high & critical-impact issues.
* Enhanced: 1hr response time with 24/7 response for high & critical-impact issues.

## Creating multiple projects for students with certain resources

* Use Infrastructure as Code tools like Cloud Deployment Manager or Terraform. This gives consistency and repeatability.

* Setting up a VM and cloning it is more cumbersome.  Also, this is only mentioning VMs.  The question talks about resources in general and could also contain other products like BigQuery, databases, ML tools, etc.

* Using Compute Engine API is also possible, but has the same issues - more work.  IaC tools make it much more easier by providing a declarative approach to setting up infrastructure.

## Google Cloud Identity vs Identity Platform

- Cloud Identity: Good for your own employees.  It is a SaaS solution that provides a single sign-on for your employees.  It is a good solution for your own employees, but not for your customers.
- Identity Platform: Good for your customers.  It is a PaaS solution that provides a single sign-on for your customers by plugging-in Google Identity into your applications.  It is a good solution for your customers, but not for your own employees.

## Extremmely Sensistive Data Processing

* Confidential Compute is the option that allows you to encrypt data in use—while it’s being processed. **Enable it!**

* Data is encrypted by Google Cloud at rest and in transit on Google Cloud.  However, encryption at time of processing is optional.

* Even for Customer Supplied Encryption Keys, the data will be decrypted at the time of processing.

* Hardened OSs does not automatically provided the confidential compute option of encrypting data while it is being processed.

## APIs SLA not supported

* GA (General Availability) is the stage where SLAs apply.

* Deprecated - in the deprecated stage, you should start moving away from those APIs and products.  Depending on the deprecation policy, SLAs could still be valid.

* Preview, Early Access, Alpha, and Beta do not have any SLA commitments.

## Migrate to Compute Engine or Anthos?

* Migrate for Compute Engine’s advanced replication migration technology copies instance data to Google Cloud in the background with no interruptions to the source workload that’s running.

* Migrate for Anthos will move the VMs to containers.  The client does not want that change.

## NoSQL databases are best suited for datas that varies widely.

## Preemptible VMs 可抢占VM

* Preemptible VMs are short lived compute instances suitable for batch jobs and fault-tolerant workloads.  You can get up to 80% discount on these machines and is ideal for the kind of workload in this question.

* MIGs will help with scaling, but the cost is still going to be quite high.

## Connect to Hybrid Cloud

* There is a lot of data to be constantly moved around.  So it makes sense to have a devoted network connection.  Since it is close to a Google Facility, we should be able to draw a direct line between the DCs.

* Even if the public cloud is a possibility, it raises questions of security and reliability.  Latency and bandwidth also could be limitations.

* Since there is a Google facility nearby, there is no need to go with a partner.

https://cloud.google.com/hybrid-connectivity

## Anthos vs GKE

Anthos比K8s更好的地方在于，它可以让你在不同的云上部署K8s，而不是只能在GCP上部署K8s。这样就可以让你的应用程序在不同的云上运行，而不是只能在GCP上运行。

而且Anthos管理容器更简单。

## AIs

* Lending DocAI is a pre-packaged AI solution that speeds "up the mortgage workflow processes to easily process loans and automate document data capture, while ensuring the accuracy and breadth of different documents (e.g., tax statements and asset documents)."

* Using TensorFlow and Cloud Vision API is too much additional work and a solution could be significantly delayed.

* Natural Language API is not enough by itself to process images and extract information from it.

## Global Transaction

* This system has to support transactions.  So the typical options are Cloud SQL or Cloud Spanner.  However, Cloud SQL is regional.

* Cloud Spanner: "Fully managed relational database with unlimited scale, strong consistency, and up to 99.999% availability."

* Cloud Datastore is a NoSQL database and would not be an ideal fit for transactions or for analysing data with the popular SQL language.

* Cloud Storage is an object storage.  It is not possible to store transaction data in an easily analyzable way.

## Potential Peaking

* When there are huge surges in demand, it is preferable to user serverless technologies that automatically scale on demand.  In this case, the key concern is the data ingestion.  Pub/Sub is a serverless system that can expand to absorb such demand.

## Transfer Appliance

* Transfer Appliance is a hardware appliance you can use to securely migrate large volumes of data (from hundreds of terabytes up to 1 petabyte) to Google Cloud Platform without disrupting business operations.

将数据转移并安全寄送到 Google 上传网点，我们会在上传网点将您的数据上传到 Cloud Storage。

## 