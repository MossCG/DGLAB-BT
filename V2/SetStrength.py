import BasicData
import BasicIO


async def setStrength(channelA, channelB):
    strengthUUID = "955a1504-0fe2-f5aa-a094-84b8d4f3e8ad"
    AChannelBits = (int(channelA)*7) & 0x7FF
    BChannelBits = ((int(channelB)*7) & 0x7FF) << 11
    dataSend = (BChannelBits | AChannelBits).to_bytes(3, byteorder='little')
    await BasicData.client.write_gatt_char(strengthUUID, dataSend)
    BasicIO.output_command("event", "updateStrength " + str(channelA) + " " + str(channelB))
    # dataReceive = await BasicData.client.read_gatt_char(strengthUUID)
    # dataInt = int.from_bytes(dataReceive, byteorder='little')
    # AResult = int((dataInt & 0x7FF) / 7)
    # BResult = int(((dataInt >> 11) & 0x7FF) / 7)
    # BasicIO.output_command("event", "updateStrength " + str(AResult) + " " + str(BResult))
