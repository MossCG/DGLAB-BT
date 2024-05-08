import BasicData
import V2.GetStrength


async def cmd_getStrength():
    if BasicData.deviceVersion == 2:
        await V2.GetStrength.getStrength()
    else:
        # V3暂时留空
        data = None
