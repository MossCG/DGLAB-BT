import BasicData
import BasicIO


async def cmd_getStrength():
    if BasicData.deviceVersion == 2:
        batteryUUID = "955a1504-0fe2-f5aa-a094-84b8d4f3e8ad"
        data = await BasicData.client.read_gatt_char(batteryUUID)
        BasicIO.output_command("event",f"updateStrength {data}")
    else:
        # V3暂时留空
        data = None
