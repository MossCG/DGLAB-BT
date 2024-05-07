import BasicData
import BasicIO


async def cmd_getBattery():
    if BasicData.deviceVersion == 2:
        batteryUUID = "955a1500-0fe2-f5aa-a094-84b8d4f3e8ad"
        data = await BasicData.client.read_gatt_char(batteryUUID)
        BasicIO.output_command("event","updateBattery "+str(data[0]))
    else:
        # V3暂时留空
        data = None
