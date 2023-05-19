import json
from azure.iot.device import IoTHubDeviceClient
from pymodbus.client import ModbusTcpClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
from pymodbus.transaction import ModbusRtuFramer
from time import sleep
from datetime import datetime, timedelta
import os


# Padrão de nome do arquivo json -> dia_mes_ano-hora.json

# Através do manual do Gavazzi EM-210, esses são os endereços físicos de onde vamos coletar os dados:
    # Endereço fisico do registrador VOLT -> 0000h
    # Endereço fisico do registrador AMP -> 000Ch
    # Endereço fisico do registrador KWH -> 0034h


CONNECTION_STRING = ""

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 502
SLAVE_ADDRESS = 1

client = ModbusTcpClient(SERVER_HOST, port=SERVER_PORT, framer=ModbusRtuFramer)

client.connect()

client_iot = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

while True:
    time_now = datetime.now() 
    file_name = time_now.strftime("%d_%m_%Y-%H-%M") + ".json"  # VERSÃO TESTE POR MINUTO
    if not(os.path.exists(file_name)): #Caso não exista o arquivo, cria um novo
        previous_time = time_now - timedelta(minutes = 1)
        previous_file_name = previous_time.strftime("%d_%m_%Y-%H-%M") + ".json"
        if os.path.exists(previous_file_name): #Verifica se o arquivo anterior existe, caso exista envia para azure
            print("Enviando arquivo para o Azure", previous_file_name) 
            send_to_azure(previous_file_name)
    
        with open(file_name, "w"):
            pass

    result = client.read_holding_registers(address = 0, count = 60, slave = SLAVE_ADDRESS) # Ler um registro do dispositivo "slave"
    decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big)
    volt = decoder._payload[0:2] # # Endereço fisico -> 0000h
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
        with open (file_name, "a") as f: #Append dos dados no arquivo
            f.write(json_str)
            f.write("\n")


# Função que abre o arquivo e envia o conteudo para o Azure
    def send_to_azure(file_name):
        with open(file_name, "r") as f:
            data = f.read()
            print(type(data))
            client_iot.send_message(data)
            print("Arquivo enviado para o Azure")


client.close()