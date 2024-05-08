# 郊狼蓝牙开发API
这是一个不需要动脑就可以用的郊狼API<br>
你只需要会输入指令就能用
* * *

# 支持范围
## 郊狼2.0
- 连接
- 设置强度
- 传输波形
- 获取电量
## 郊狼3.0
- 没写完呢，3.0还不支持
* * *

# 调用方式
## Python
- 都用Python了，你直接扒拉我代码就行
## Java（及其他平台）
- 仅供参考喵
- 具体代码不写了因为咱懒
- 反正就是用Process调该项目构建出来的exe文件
- 参考下面输入输出就行了
* * *

# 读写方案
- 逐行输入，一行为一个指令
- 逐行输出，一行为一条消息

# 参考操作
```
scan
connect xx:xx:xx:xx:xx:xx
getBattery
setStrength 0 10
sendWave 5 135 20
```
* * *

# 构建环境
| 依赖/环境       | 版本     |
|-------------|--------|
| Windows     | 11     |
| Python      | 3.12   |
| bleak       | 0.22.0 |
| pyinstaller | 6.6.0  |

# 构建方法
```
pip install bleak
pip install pyinstaller
cd 项目文件夹
pyinstaller DGLAB-BT-EXE.spec
```
构建出来的exe会存放在dist文件夹里面
* * *

# 输出
## msg
```
- 输出描述：消息
- 输出格式：msg 文本信息
```
## event
```
- 输出描述：事件，具体事件及参数见下
- 输出格式：event 事件名称 事件参数1 事件参数2......
```
* * *

# 输入
## stop
```
- 操作描述：退出软件
- 输入格式：stop
```
## scan
```
- 操作描述：开始搜索蓝牙设备
- 输入格式：scan
```
## connect
```
- 操作描述：连接蓝牙郊狼设备
- 输入格式：connect 地址
```
## getBattery
```
- 操作描述：获取郊狼电量
- 输入格式：getBattery
```
## setStrength
```
- 操作描述：设置强度
- 输入格式：setStrength A通道强度 B通道强度
```
## sendWave
```
- 操作描述：发送波形
- 输入格式：sendWave A/B x y z 
```

# 事件
## start
```
- 事件描述：启动时发出的消息，标识启动完成
- 输出格式：event start
```
## stop
```
- 事件描述：关闭时发出的消息，标识已关闭
- 输出格式：event stop
```
## scanStart
```
- 事件描述：开始扫描设备
- 输出格式：event scanStart
```
## scanComplete
```
- 事件描述：设备扫描完成，可以进行下一轮扫描
- 输出格式：event scanComplete
```
## deviceFound
```
- 事件描述：发现疑似郊狼的设备
- 输出格式：event deviceFound 设备地址
```
## deviceVersion
```
- 事件描述：判断郊狼版本
- 输出格式：event deviceVersion 2或3
```
## connectStart
```
- 事件描述：尝试连接到郊狼
- 输出格式：event connectStart
```
## connectSucceed
```
- 事件描述：连接郊狼成功
- 输出格式：event connectSucceed
```
## connectFailed
```
- 事件描述：连接郊狼失败
- 输出格式：event connectFailed
```
## updateBattery
```
- 事件描述：电量更新
- 输出格式：event updateBattery 电量
```
## updateStrength
```
- 事件描述：强度更新
- 输出格式：event updateStrength A通道强度 B通道强度
```
## updateWave
```
- 事件描述：波形更新
- 输出格式：event updateWave A通道强度 B通道强度
```

# 碎碎念
Java在Windows下的BLE开发真TM气人！<br>
要不是这个原因我就用Java写了！！！<br>
气死老娘了