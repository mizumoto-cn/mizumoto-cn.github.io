---
type: post
title: Docker Desktop Installation Troubleshooting
subtitle: Awful Docker Desktop Installation Troubleshooting
thumbnail-img: ""
share-img: /assets/img/path.jpg
tags: [Docker]
---

### When you need hyper-v

When you need that shit on your Windows 10 family version, you need to install the Hyper-V manually.

```bash
pushd "%~dp0"
dir /b %SystemRoot%\servicing\Packages\*Hyper-V*.mum >hyper-v.txt
for /f %%i in ('findstr /i . hyper-v.txt 2^>nul') do dism /online /norestart /add-package:"%SystemRoot%\servicing\Packages\%%i"
del hyper-v.txt
Dism /online /enable-feature /featurename:Microsoft-Hyper-V-All /LimitAccess /ALL
```

Then press `Y` to reboot your computer for updating the Hyper-V.

Or you'll probably see `Hyper-V Requirements: A hypervisor has been detected. Features required for Hyper-V will not be displayed.` shit, when you type `systeminfo` into your terminal if you are not the `Professional` version or shit or so.

### Switch your f@cking wsl to wsl2

```bat
PS C:\Windows> wsl -l -v
  NAME              STATE           VERSION
* Ubuntu-20.04      Stopped         1
  docker-desktop    Running         2
PS C:\Windows> wsl --set-default-version 2
有关与 WSL 2 的主要区别的信息，请访问 https://aka.ms/wsl2
操作成功完成。
PS C:\Windows> wsl.exe --set-version Ubuntu-20.04 2
正在进行转换，这可能需要几分钟时间...
有关与 WSL 2 的主要区别的信息，请访问 https://aka.ms/wsl2
转换完成。
PS C:\Windows> wsl -l -v
  NAME              STATE           VERSION
* Ubuntu-20.04      Stopped         2
  docker-desktop    Running         2
```

You may need to type `.exe` in the terminal to make it work.

You may also need to type `Ubuntu` or `Ubuntu-20.04` or shit or so.

### When it's port got fucked

This shitty software will throw you a simple 

```java
System.InvalidOperationException:
Failed to set version to docker-desktop: exit code: -1　
```

And you'll never get to know what's wrong.

Until you searched through the internet, and find it cannot automatically switch its default port, which cannot be configured in the settings json file either.

Then you'll have to simply reset the winsock:

```bash
netsh winsock reset
```

or maybe you'll try `NoLso.exe` at <https://github.com/dyingsu/nolsp>.

Just simple do it in administrator mode.

```bash
NoLsp.exe %fuckingwsl2path%
```

 I'll never want to use this on my computer again.

I'll always do that on linux...

Good Night, Peace.
