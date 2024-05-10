import BasicData
import BasicIO


async def sendWave(channel, x, y, z):
    if channel == "A":
        channelUUID = "955A1506-0FE2-F5AA-A094-84B8D4F3E8AD"
    else:
        channelUUID = "955A1505-0FE2-F5AA-A094-84B8D4F3E8AD"
    xBits = int(x) & 0x1F
    yBits = (int(y) & 0x3FF) << 5
    zBits = (int(z) & 0x1F) << 15
    dataSend = (zBits | yBits | xBits).to_bytes(3, byteorder='little')
    await BasicData.client.write_gatt_char(channelUUID, dataSend)
    BasicIO.output_command("event", "updateWave " + str(x) + " " + str(y) + " " + str(z))
    # dataReceive = await BasicData.client.read_gatt_char(channelUUID)
    # dataInt = int.from_bytes(dataReceive, byteorder='little')
    # xResult = dataInt & 0x1F
    # yResult = (dataInt >> 5) & 0x3FF
    # zResult = (dataInt >> 15) & 0x1F
    # BasicIO.output_command("event", "updateWave "+str(xResult)+" "+str(yResult)+" "+str(zResult))
