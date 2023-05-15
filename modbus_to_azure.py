import json
from azure.iot.device import IoTHubDeviceClient
from pymodbus.client import ModbusTcpClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
from pymodbus.transaction import ModbusRtuFramer
from time import sleep
import os

CONNECTION_STRING = "<your-iot-hub-connection-string>"

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 502
SLAVE_ADDRESS = 1

client = ModbusTcpClient(SERVER_HOST, port=SERVER_PORT, framer=ModbusRtuFramer)

client.connect()

client_iot = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

while True:
    result = client.read_holding_registers(address=0, count=49, unit=1)  # Read registers from the slave device
    decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big)
    sleep(1)
    if result.isError():
        print(result)
        print("Error reading registers from the device")
    else:
        data = {
            "SLAVE_1": {
                "AMPERAGEM": decoder.decode_16bit_int()
            }
        }
        json_str = json.dumps(data)
        os.system("cls")
        print("<---------- SLAVE 1 ---------->")
        print("JSON data:", json_str)

        # Envia menssagem para o IoT Hub
        message = json_str.encode("utf-8")
        client_iot.send_message(message)


client.close()