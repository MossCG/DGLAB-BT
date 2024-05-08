import BasicData
import V2.SetStrength


async def cmd_setStrength(channelA, channelB):
    if BasicData.deviceVersion == 2:
        await V2.SetStrength.setStrength(channelA, channelB)
    else:
        # V3暂时留空
        data = None
