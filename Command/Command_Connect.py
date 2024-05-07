from bleak import BleakClient

import BasicData
import BasicIO


# noinspection PyBroadException,PyGlobalUndefined
async def cmd_connect(address):
    BasicIO.output_command("msg", "正在连接设备......")
    try:
        BasicIO.output_command("event", "connectStart")
        BasicData.client = BleakClient(address)
        await BasicData.client.connect()
        for service in BasicData.client.services:
            BasicIO.output_command("msg", "发现服务：" + service.uuid)
            if service.uuid == "955a180a-0fe2-f5aa-a094-84b8d4f3e8ad":
                BasicIO.output_command("event", "deviceVersion 2")
                BasicData.deviceVersion = 2
            if service.uuid == "0000180c-0000-1000-8000-00805f9b34fb":
                BasicIO.output_command("event", "deviceVersion 2")
                BasicData.deviceVersion = 3
        if BasicData.deviceVersion is None:
            await BasicData.client.disconnect()
            BasicIO.output_command("event", "connectFailed")
        else:
            BasicIO.output_command("event", "connectSucceed")
    except Exception:
        if BasicData.client.is_connected:
            await BasicData.client.disconnect()
        BasicIO.output_command("event", "connectFailed")
