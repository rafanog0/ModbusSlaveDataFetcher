import json
from pymodbus.client import ModbusTcpClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
from pymodbus.transaction import ModbusRtuFramer
from time import sleep
from datetime import datetime
import os

# Padrão de nome do arquivo json -> dia_mes_ano-hora.json

#Arquivo teste sem conexão com azure


SERVER_HOST = "127.0.0.1"
SERVER_PORT = 502
SLAVE_ADDRESS = 1

client = ModbusTcpClient(SERVER_HOST, port=SERVER_PORT, framer=ModbusRtuFramer)

client.connect()


while True:
    time_now = datetime.now()
    file_name = time_now.strftime("%d_%m_%Y-%H") + ".json"
    if not(os.path.exists(file_name)):        
        with open(file_name, "w"):
            pass

    result = client.read_holding_registers(address = 0, count = 60, slave = SLAVE_ADDRESS) # Ler um registro do dispositivo "slave"
    decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big)
    volt = decoder._payload[0:2] # Endereço fisico -> 0000h
    amp = decoder._payload[24:26] # Endereço fisico -> 000Ch
    kWh = decoder._payload[104:106] # Endereço fisico -> 0034h

    sleep(1)
    if result.isError():
        print(result)
        print("Error reading registers from the device")
    else:
        data = {
            "SLAVE_1": {
                "AMP": int.from_bytes(amp, byteorder = 'big'),
                "VOLT": int.from_bytes(volt, byteorder = 'big'),
                "KWH": int.from_bytes(kWh, byteorder = 'big'),
                "TIME": str(datetime.now())
            }
        }
        json_str = json.dumps(data)
        os.system("cls")
        print("<---------- SLAVE 1 ---------->")
        print("JSON data:", json_str)
        with open (file_name, "a") as f:
            f.write(json_str)
            f.write("\n")


client.close()