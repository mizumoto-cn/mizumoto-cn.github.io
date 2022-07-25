---
type: post
title: IAM Policy Inheritance in Depth
subtitle: AWS-SAA-C02 Note
thumbnail-img: ""
share-img: /assets/img/path.jpg
tags: [AWS]
---

## Group Policy & Individual Policy (inline)

* Group policy applies to everyone belonging to the group.
* Inline policy applies to the individual users, no matter what group they belong to.

## Policy Inheritance

![inheritance](/assets/img/AWS-SAA/IAM/policy-inheritance.png)

So Charles will inherit the policy from both group "Developers" and "Audit Team".


## .json Document Format for IAM Policies

```json
{
  "Version": "2012-10-17",
  "Id": "SAA-C02-IAM-Policy-Inheritance",
  "Statement": [
    {
      "Sid": "1",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:root"
      },
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": [
        "arn:aws:s3:::mybucket/*"
      ]
    }
  ]
}
```

* Version: The version of the policy. Usually "2012-10-17".
* Id: The indentifier of the policy. It's optional.
* Statement: The list of statements in the policy.(required)
  * Sid: The identifier of the statement. It's optional.
  * Effect: Decides whether the statement allows or denies access. It's required.
  * Principal: The account/user/role to whom this policy is applied to.
  * Action: The list of actions that is allowed or denied.
  * Resource: The resources to which the action is applied to.
  * Condition: The condition for when this policy shall be applied.

