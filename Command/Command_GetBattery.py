import BasicData
import V2.GetBattery


async def cmd_getBattery():
    if BasicData.deviceVersion == 2:
        await V2.GetBattery.getBattery()
    else:
        # V3暂时留空
        data = None
