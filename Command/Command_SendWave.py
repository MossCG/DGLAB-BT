import BasicData
import V2.SendWave


async def cmd_sendWave(channel,x,y,z):
    if BasicData.deviceVersion == 2:
        await V2.SendWave.sendWave(channel, x, y, z)
    else:
        # V3暂时留空
        data = None
