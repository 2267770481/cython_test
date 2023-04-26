nuitka将python源码转成C++（这里得到的是二进制的pyd文件，防止了反编译），然后再编译成可执行文件。提高安全性和运行速度。

#### 安装
```
pip install nuitka
pip install ordered-set # 加速编译
pip install zstandard # onefile时压缩文件
```

#### 打包

**windows下打包命令**

`python -m nuitka --standalone --show-memory --show-progress --nofollow-imports --plugin-enable=numpy --follow-import-to=apps --output-dir=out --windows-icon-from-ico=./favicon.ico app.py
`

执行结果：
![image](https://img2023.cnblogs.com/blog/1224392/202304/1224392-20230426190235048-2111041658.png)

等打包完后，会生成个out文件夹，里边的app.dist就是我们需要的东西。
![image](https://img2023.cnblogs.com/blog/1224392/202304/1224392-20230426191218687-586829539.png)


如果直接运行 app.dist/app.exe 程序的时候，有时候会出现缺少某个模块的情况，这是因为我们**只将自己的代码转成C++,不管这些大型的第三方包！**。所以我们需要在python依赖包文件夹(Lib\site-packages)中找到这些包，并复制到app.dist中。(比较懒的做法是将site-packages中的所有文件直接复制到app.dist中，如果有出现冲突的就选择跳过)

现在可以直接运行app.exe应用程序。
![image](https://img2023.cnblogs.com/blog/1224392/202304/1224392-20230426191514315-884376577.png)

接口调用
http://127.0.0.1:1111/module_a/a_a
![image](https://img2023.cnblogs.com/blog/1224392/202304/1224392-20230426191545538-1211473702.png)





#### 指令集
```
--mingw64 #默认为已经安装的vs2017去编译，否则就按指定的比如mingw(官方建议)
--standalone 独立环境，这是必须的(否则拷给别人无法使用) 不需要再安装python等之类的
--windows-disable-console 没有CMD控制窗口
--output-dir=out 生成exe到out文件夹下面去
--show-progress 显示编译的进度，很直观
--show-memory 显示内存的占用
--nofollow-imports：不编译代码中所有的import，比如keras，numpy之类的。
--follow-import-to=utils,src：需要编译成C++代码的指定的2个包含源码的文件夹，这里用,来进行分隔。
--enable-plugin=pyside6
--plugin-enable=tk-inter 打包tkinter模块的刚需
--plugin-enable=numpy 打包numpy,pandas,matplotlib模块的刚需
--plugin-enable=torch 打包pytorch的刚需
--plugin-enable=tensorflow 打包tensorflow的刚需
--windows-icon-from-ico=你的.ico 软件的图标
--windows-company-name=Windows下软件公司信息
--windows-product-name=Windows下软件名称
--windows-file-version=Windows下软件的信息
--windows-product-version=Windows下软件的产品信息
--windows-file-description=Windows下软件的作用描述
--windows-uac-admin=Windows下用户可以使用管理员权限来安装
--windows-disable-console：运行exe取消弹框。这里没有放上去是因为我们还需要调试，可能哪里还有问题之类的。
--linux-onefile-icon=Linux下的图标位置
--onefile 单文件打包
–-remove-output 在打包结束后，清理打包过程中生成的临时文件
--include-package=复制比如numpy,PyQt5 这些带文件夹的叫包或者轮子
--include-module=复制比如when.py 这些以.py结尾的叫模块
```
