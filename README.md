# 警告
**为了我们都省点事，请勿在*任何公开场合*提到该项目，否则极有可能受到官方针对而无效。**

---

# 安装
## 1.安装Airtest
点击[AirtestIDE](https://airtest.netease.com/changelog.html)下载AirtestIDE，选择最新版即可。

## 2.安装雷电模拟器
点击[雷电模拟器9.0.19](https://res.ldmnq.com/download/leidian9/ldinst9_9.0.19.exe)下载

## 3.Root雷电模拟器
[雷电模拟器Root教程](https://www.52pojie.cn/thread-1688786-1-1.html)

**注意**：只需要安装Magisk，不要安装LSPosed，否则可能对造成系统不稳定。使用时需要将雷电模拟器设置为手机版1080x1920。

## 4.安装Fakelocation
下载[Fakelocation](https://github.com/Lerist/FakeLocation/releases)拖进雷电模拟器会自动安装。

**注意**：软件需要付费，安装完成后在设置里选择数据导入`FakelocationConfig.bak`

## 5.安装跑步软件
下载[跑步软件](https://gmxq.qust.edu.cn/system/_content/download.jsp?urltype=news.DownloadAttachUrl&owner=1693119841&wbfileid=11679501)拖进雷电模拟器

**注意**：可以从安装自己的安卓手机提取安装包来替代上面下载的安装包。

# 配置文件说明
## config.txt
目前只有一个参数`init_flag=0`，为0时不自动打开fakelocation。
## finished_accounts.txt
存储已经跑完的账号，一行一个账号，文件末尾必须有空行。添加进这个文件的账号不会进入待跑列表(waitlist)。
## repo.txt
账号仓库，需要跑的账号就添加在这里面。文件格式`账号 密码 剩余次数`。使用空格对每个数据进行间隔。文件末尾必须有空行。

# 运行说明
1. 打开AirtestIDE和雷电模拟器。
2. 使用AirtestIDE的ADB连接雷电模拟器。
3. 点击AirtestIDE的运行按钮。

**注意**：因为Airtest是根据坐标进行定位的，所以建议将模拟器桌面整理图中样子。至少保证Fakelocation和run app的位置如图，否则会导致程序运行失败。你也可以自己修改程序中的坐标来实现自定义位置。
![](./resources/img1.png)

# 附加说明
## 已知问题
1. AirtestIDE在运行时GUI界面莫名退出。
2. 当模拟器运行速度过慢时会到时判断时间超出程序设定范围，进而程序出错。

## 待优化内容
1. 增加更多意外情况的处理，提高程序的稳定性。
2. 配置文件读取过于死板，比如文件末尾必须有空行。

## 如果有兴趣改进该项目，欢迎提交PR。如果有问题请提Issue。