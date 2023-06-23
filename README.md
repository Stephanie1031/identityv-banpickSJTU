<h1 align="center">第五人格比赛banpick画面</h1>

>利用Pyside6库写成的第五人格banpick可视化界面，原作者为FDU的Pise1don，来自SJTU的本人Stephanie进行了一些修改与调整~(联系方式：QQ 871612785, ~~（第五人格ID: 207040762）~~

## 简介

>本画面供`上海交通大学第五人格校内赛`使用，代码改编自复旦大学第五人格社团初创的程序，欢迎大家继续进行改进！

本画面中所有的图像均来自`第五人格wiki`以及`游戏海外官网`。

在bpsystem文件夹中含有pyinstaller生成的可执行文件，可供没有安装Python与Pyside6库的设备直接运行使用。

originalcode文件夹中包含了Python源代码，以及各种图片资源，可根据自己的需要进行修改，从而满足不同游戏banpick的需求。

## 使用方法

实际运行过程中会产生一个后台窗口及一个用于直播时展示的bp界面窗口。

<p align='center'><img width="600" src="https://github.com/Stephanie1031/identityv-banpickSJTU/blob/main/background.png"></p>
<h5 align="center">后台窗口</h5>

<p align='center'><img width="600" src="https://github.com/Stephanie1031/identityv-banpickSJTU/blob/main/bp-example.png"></p>
<h5 align="center">bp界面演示</h5>

后台窗口中所有的选项都可以通过拼音首字母进行快速筛选，当前代码版本更新至求生者角色“教授”，后续是否会维护尚且不知：P

///////////////////////////////分割线//////////////////////////////////

2022/9/25更新

>加入了新求生——`古董商`，以及新监管——`隐士`

>——另外更新了exe的icon，是本人亲自绘制的佣兵头像///

>附加原作者在代码后写的一段README，如果使用中还存在什么问题可以看下面这段详细解说~


///////////////////////////////分割线//////////////////////////////////

2023/3/30更新

>加入了新求生——`作曲家`，以及新监管——`守夜人`

>突然发现字体文件没放进来，主目录里的.ttf文件右键安装即可（不装也不影响程序使用就是了）

///////////////////////////////分割线//////////////////////////////////

2023/6/23**超级大更新！！**~~(且有可能为已毕业的本人最后一次维护)~~

>加入了新求生——`记者`

>更新了exe的icon，改为SJTU第五人格的图标

>更新加入**比分页面UI**，可以在原有后台程序中输入bo3/5各局比分并计算显示~

## 比分界面使用方式

输入各局比分后点击`“生成比分界面”按钮`，bp系统会根据当前模式和输赢情况显示到比分UI中。

<p align='center'><img width="600" src="https://github.com/Stephanie1031/identityv-banpickSJTU/blob/main/point-example.png"></p>
<h5 align="center">比分界面演示</h5>

注：由于本人能力有限，当前版本仅支持选择比赛模式(bo3/bo5)并输入比分后进行手动按钮同步，还望后续有人能够完善此代码~

~~也许以后会小更新一个比赛中使用的比分悬浮窗？敬请期待！~~



<h1 align="center">原作者代码说明</h1>
#

作者：Pise1don，复旦大学第五人格协会成员，QQ: 307958871 ~~，（第五人格ID: 60781755）~~

**本软件严禁商用**

---

## 简介

本软件最初是为复旦大学电子竞技联盟2022FEG(Fudan Esports Gaming)第五人格项目比赛转播定制的，现考虑到有一些朋友也想使用，特做修改并发布。

本软件的制作基本可以说是临时起意的。软件作者此前并没有接触过PyQt，也并没有开发项目的经验，在短短两天内突击学习了PyQt并写出了此软件。因此软件的代码中可能有大量不符工业标准的问题，代码的写法也略显简单粗暴，其中求生者、监管者、地图列表的处理方法可以说颇为低级。如果计算机相关专业的同好有热情且有时间的话，欢迎对此软件做出修改，如果可能，希望可以将优化过的软件分享给作者，十分感谢。

软件中使用到的背景图片修改自2019IVC冬季精英赛线上赛的bp界面，此仓库中附有该背景图片的Photoshop文件和来自官方录像的初始素材，在Photoshop文件中作者对初始素材图层做出过不可逆改动，如有需要建议使用初始素材。

软件中使用到的游戏角色图片和地图图片来自[第五人格BWIKI](https://dwrg.wiki/)。

## 授权相关

* 软件内用到的图片资源（如2019IVC冬季精英赛bp界面、角色图片、地图图片）均已获**第五人格官方**的非商用授权；
* 使用的`华康POP`字体在**非商用**情形可使用；
* 如您想要分享/修改本软件，请遵循[CC BY-NC-SA 4.0协议](https://creativecommons.org/licenses/by-nc-sa/4.0/)（创作共用-署名-非商业性-相同方式共享）。

## 运行要求

* 对于想直接运行源码的使用者，应有Python3，并有PySide6库；对于想使用打包版本的使用者，应为Windows系统。
* (推荐 ~~，你也可以理解为必须~~) 安装主目录下的`华康POP繁简完全版.ttf`，这将使显示风格更加接近游戏内风格。

## 操作指南

在以下两种方式中选一：

* 使用打包版本：直接解压目录下的`第五人格bp界面打包.zip`，运行其中的`bpsystem.exe`。
* 直接运行源码：使用Python3解释器运行`程序`目录下的`bpsystem.py`。

软件运行后会出现bp系统后台界面，点击右上角`生成bp界面`按钮后即可生成bp界面（即应由OBS捕捉并播出的界面）。后台中所有下拉菜单均有搜索功能，所有候选项后添加了拼音缩写以便快速筛选 ~~（这可能使得后台很丑，但好用啊，反正又不播出）~~。当后台中内容发生改动时bp界面将会自动更新信息。

## 与OBS结合使用的建议

* 建议使用原生OBS（[点此访问官网](https://obsproject.com/)）而不是直播平台打包过的简易版；
* 请在**软件运行时**使用OBS捕获bp界面窗口，请选择`窗口采集`模式，并在设置中选择`窗口标题必须匹配`（否则OBS可能会捕捉到后台窗口），并取消勾选`显示鼠标指针`；
* 运行过程中**不可将前台窗口最小化**，否则OBS将无法捕捉其变化；
* 目前软件仍未经过数量可靠的测试，因此使用过程中请注意播出界面，以防出现意外。

**注：** 如果使用由直播平台打包的OBS简易版（如B站直播姬，下以直播姬为例），其可能在窗口捕捉时不提供`窗口标题必须匹配`选项，而只按照进程名匹配。这样如果关闭bp界面窗口，直播姬会转而捕捉后台窗口将其播出，这将成为播出事故。个人的建议是捕捉bp界面成功后不再关闭bp界面，需要隐藏时在直播姬中隐藏对应素材即可。

## 关于复旦大学第五人格协会

**以下内容经复旦大学第五人格协会授权**

本次复旦大学电子竞技联盟2022FEG第五人格项目比赛引发了一定的关注，在此我谨代表协会对热情的玩家们表示感谢。尚未加入并想加入协会的**复旦大学**第五人格玩家请通过校内渠道（如社团系统）联系我们，完成审核后即可加入。考虑到协会为校内组织，校内交流性质为主，我们目前**谢绝校外人员加入交流群**。同时，**我们十分期待与其他高校的第五人格组织保持联系和联谊**。

**联谊相关：** 如有其他高校第五人格组织想要与我协会联谊，请**组织负责人**以**高校域名邮箱**（即学邮，一般以`edu.cn`结尾）发邮件至[fudanes_idv@163.com](mailto:fudanes_idv@163.com)，邮件内请写明**学校**和负责人**联系方式**。**请勿以个人身份联系协会**，这将对我们的日常工作造成极大的困扰，感谢大家配合。