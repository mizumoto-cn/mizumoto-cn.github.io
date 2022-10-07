---
layout: page
title: GCP CLI
subtitle: GCP notes by M." B.U.T.A"O.
---

## Installation

**Windows**

```powershell
(New-Object Net.WebClient).DownloadFile("https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe", "$env:Temp\GoogleCloudSDKInstaller.exe") & $env:Temp\GoogleCloudSDKInstaller.exe
```

For other platforms, see [Installing Cloud SDK](https://cloud.google.com/sdk/docs/install).

After installation, GCP SDK will automatically run command `gcloud init` to initialize the SDK. It will ask you to login with your GCP account in a pop-out browser window.

### Cheat Sheet

[Google Cloud SDK Cheat Sheet](https://cloud.google.com/sdk/docs/cheatsheet)