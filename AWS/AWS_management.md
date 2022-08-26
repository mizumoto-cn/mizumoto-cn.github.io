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
- inline policy: only effective for specific roles
- permission boundaries
  - used to delegate(授权，把……委托给) admin to other users
  - prevent privilege escalation(increase to counteract a perceived discrepancy) or unnecessary broad permissions
  - control maximum permissions an IAM policy can grant
- "owner" (in permission policy) refers to the identity and email address used to create the AWS account

### Organization

- paying account should be used for billing purposes only; do not deploy resources in paying account
- enable/disable AWS services using Service Control Policies(SCP) either on OU (Organization Unit) or on individual accounts
  - SCPs affect **only IAM** users and roles that are managed by accounts that are part of the organization (including the root user). SCPs don't affect resource-based policies directly. That also doesn't affect users or roles from accounts outside the organization.
- RAM: Resource Access Manager
  - can share AWS resources between accounts
    - e.g. EC2, Aurora, Route 53, resource groups
  - sharing must be enabled with the master account
  - only resources owned by the account can be shared; cannot re-share resources owned by other accounts
  - resource sharing can be done at an individual account if RAM is not enabled
- SSO helps centrally manage access to AWS accounts
  - exam tip: SAML in question -> SSO in answer

### AWS Directory Service

- a family of managed services heavily integrated with Microsoft Active Directory(AD)
- connect AWS resources with on-premise AD //TODO
- standalone directory in the cloud
- use existing corporate credentials
- enable SSO to any domain-joined EC2 instance
- provides AD domain controllers(DCs) running 