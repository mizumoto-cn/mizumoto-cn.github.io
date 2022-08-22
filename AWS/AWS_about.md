---
layout: page
title: AWS SAA-C02 ABOUT
subtitle: AWS notes by M." B.U.T.A"O.
---

## About the exam

### Outline

- 65 questions
  - some are multiple selection questions
  - No PENALTY for incorrect answers so guess
- can mark for later review
- identify the key AWS features in each question
  - look for phrases like "with minimum cost"

### Axioms

- Single AZs are expected to unlikely to be the right answer
- AWS-managed services are always preferred
- fault tolerant is not equivalent to high availability
- expect everything will fail at some point
- if data is **unstructured**, **S3** is usually the preferred solution
- **Security Groups** only allow, **NACLs** only deny
- IAM roles are preferred to access keys
- for flexible schema, **DynamoDB** is the preferred solution
- SAML <==> SSO
- DDoS <==> AWS Shield + AWS WAF
- **Orchestration**
  - Container <==> ECS
  - Serverless <==> AWS Step Functions
  - Tasks <==> SWF
- IPSec <==> AWS VPC VPN
- usually bad practice to use SQS with db for performance; use **replicas**, **elasticache** or **auto scaling** if possible
- WORM <==> object lock (in S3)
- FIPS 140-2 Level 2 <==> AWS KMS
- FIPS 140-2 Level 3 <==> CloudHSM
- most AWS services use VPC **Interface** Endpoint except for S3 and DynamoDB, which use VPC **Gateway** Endpoint

### Tips for exams

- when creating a VPC, **subnet** and **IGW** are NOT created automatically; **route table**, **NACL** and **Security Group** are created automatically
- when migrating, AWS does NOT copy **launch permissions**, **user-defined tags**, or Amazon **S3 bucket permissions** from the source AMI to the target AMI.
- 3 levels of VPC flow log
  - VPC level
  - subnet level
  - Network Interface level
- **Gateway** Endpoint for S3 and DynamoDB, while **Interface** Endpoint for all other services
- CloudFormation major sections:
  - Format Version
  - Description
  - Metadata
  - Parameters
  - Mappings
  - Conditions
  - Transform
  - Resources (required)
  - Outputs
