from bleak import BleakScanner

import BasicIO


async def cmd_scan():
    BasicIO.output_command("msg", "正在搜索设备......")
    BasicIO.output_command("event", "scanStart")
    devices = await BleakScanner.discover()
    list_device = []
    for device in devices:
        name = device.name
        if name is None:
            continue
        if name.find("D-LAB") > -1:
            BasicIO.output_command("msg", "发现郊狼设备：" + device.address + "/" + device.name)
            list_device.append(device)
            BasicIO.output_command("event", "deviceFound " + device.address)
        else:
            BasicIO.output_command("msg", "发现设备：" + device.address + "/" + device.name)
    BasicIO.output_command("event", "scanComplete")
