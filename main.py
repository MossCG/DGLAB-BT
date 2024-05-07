import asyncio

import BasicData
from BasicIO import *
from Command.Command_Connect import cmd_connect
from Command.Command_GetBattery import cmd_getBattery
from Command.Command_GetStrength import cmd_getStrength
from Command.Command_Scan import cmd_scan
from Command.Command_Stop import cmd_stop
from Command.Command_SetStrength import cmd_setStrength


# 郊狼Python开发API
# Java|Windows的BLE环境属实气死我了，我选择套一个python（麻）


# 主类
def main():
    BasicData.init()
    output_command("msg", "DGLAB蓝牙核心已启动！")
    output_command("event", "start")
    while 1 == 1:
        cmd = input_command()[0]
        if len(cmd) <= 0:
            continue
        key = cmd.split()
        # 指令模块
        if key[0] == "stop":
            cmd_stop()
        if key[0] == "scan":
            asyncio.run(cmd_scan())
        if key[0] == "connect":
            asyncio.run(cmd_connect(key[1]))
        if key[0] == "getBattery":
            asyncio.run(cmd_getBattery())
        if key[0] == "setStrength":
            asyncio.run(cmd_setStrength(key[1], key[2]))
        if key[0] == "getStrength":
            asyncio.run(cmd_getStrength())


# 运行主类
main()
