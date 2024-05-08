import BasicData
import BasicIO


async def sendWave(channel, x, y, z):
    if channel == "A":
        channelUUID = "955A1505-0FE2-F5AA-A094-84B8D4F3E8AD"
    else:
        channelUUID = "955A1506-0FE2-F5AA-A094-84B8D4F3E8AD"
    array = bytearray()
    array.append(int(x))
    array.append(int(y))
    array.append(int(z))
    await BasicData.client.write_gatt_char(channelUUID, array)
    data = await BasicData.client.read_gatt_char(channelUUID)
    BasicIO.output_command("event", "updateWave "+str(data[0])+" "+str(data[1])+" "+str(data[2]))
