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

### Google Cloud Identity vs Identity Platform

- Cloud Identity: Good for your own employees.  It is a SaaS solution that provides a single sign-on for your employees.  It is a good solution for your own employees, but not for your customers.
- Identity Platform: Good for your customers.  It is a PaaS solution that provides a single sign-on for your customers by plugging-in Google Identity into your applications.  It is a good solution for your customers, but not for your own employees.

### Extremmely Sensistive Data Processing

* Confidential Compute is the option that allows you to encrypt data in use—while it’s being processed. **Enable it!**

* Data is encrypted by Google Cloud at rest and in transit on Google Cloud.  However, encryption at time of processing is optional.

* Even for Customer Supplied Encryption Keys, the data will be decrypted at the time of processing.

* Hardened OSs does not automatically provided the confidential compute option of encrypting data while it is being processed.

### APIs SLA not supported

* GA (General Availability) is the stage where SLAs apply.

* Deprecated - in the deprecated stage, you should start moving away from those APIs and products.  Depending on the deprecation policy, SLAs could still be valid.

* Preview, Early Access, Alpha, and Beta do not have any SLA commitments.

