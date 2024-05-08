import BasicData
import BasicIO


async def getStrength():
    batteryUUID = "955a1504-0fe2-f5aa-a094-84b8d4f3e8ad"
    data = await BasicData.client.read_gatt_char(batteryUUID)
    BasicIO.output_command("event", "updateStrength "+str(data[0]/7)+" "+str(data[1]/7))