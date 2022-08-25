---
layout: page
title: AWS SAA-C02 Management
subtitle: AWS notes by M." B.U.T.A"O.
tags: [AWS]
---

## IAM

Policies: See [AWS IAM Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) & [My blog note](../_posts/2022-07-23-IAM-in-Depth.md)

- key entities
  - users
  - groups
  - roles
  - policies
    - identity policies
    - resource policies
- universal: not specific to region
- new users have NO permissions by default when created
- Access Key ID abd secret access keys are assigned to new users
  - not same as passwords, can only be used via SDK and CLI
  - can only be viewed once so save them after creating
  - (for EC2) better to create IAM roles instead of keeping credentials 
- you can give federated users single sign-on (SSO) access to AWS management console with SAML (Sercurity Assertion Markup Language)
- Amazon Resource Name (ARN) is a string that uniquely identifies an AWS resource
  - begins with `arn:partition:service:region:account-id`, ends with `resource` or `resource-type`
  - e.g. `arn:aws:ec2:us-east-1:123456789012:instance/i-12345678`
- IAM policy can only have effect after it was attached to a user or group
- IAM policies rules
  - not explicitly allowed means implicitly denied
  - explicit deny > everything else
  - AWS joins all applicable policies
  - AWS-managed v.s. customer-managed
  - can control access based on tags