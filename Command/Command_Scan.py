from bleak import BleakScanner, BleakClient

import BasicIO


async def cmd_scan():
    BasicIO.output_command("msg", "正在搜索设备......")
    BasicIO.output_command("event", "scanStart")
    devices = await BleakScanner.discover()
    for device in devices:
        if device.name is None:
            continue
        if device.name.find("D-LAB ESTIM01") > -1:
            BasicIO.output_command("msg", "发现郊狼V2设备：" + device.address + "/" + device.name)
            BasicIO.output_command("event", "deviceFound " + device.address)
            continue
        if device.name.find("47L121000") > -1:
            BasicIO.output_command("msg", "发现郊狼V3设备：" + device.address + "/" + device.name)
            BasicIO.output_command("event", "deviceFound " + device.address)
        BasicIO.output_command("msg", "发现设备：" + device.address + "/" + device.name)
    BasicIO.output_command("event", "scanComplete")
