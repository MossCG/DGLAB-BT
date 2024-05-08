import BasicData
import BasicIO


async def setStrength(channelA, channelB):
    batteryUUID = "955a1504-0fe2-f5aa-a094-84b8d4f3e8ad"
    array = bytearray()
    array.append((int(channelA)) * 7)
    array.append((int(channelB)) * 7)
    await BasicData.client.write_gatt_char(batteryUUID, array)
    data = await BasicData.client.read_gatt_char(batteryUUID)
    BasicIO.output_command("event", "updateStrength " + str(data[0] / 7) + " " + str(data[1] / 7))
