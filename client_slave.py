from pymodbus.client import ModbusTcpClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
from pymodbus.transaction import ModbusRtuFramer

from time import sleep
import os

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 502

SLAVE_ADDRESS = 1

client = ModbusTcpClient(SERVER_HOST, port=SERVER_PORT, framer = ModbusRtuFramer) # Conecta 

client.connect()


while True:
    result = client.read_holding_registers(address = 0, count = 10, slave = SLAVE_ADDRESS) 
    decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big)
    kWh = decoder._payload[6:8]
    print(list(decoder._payload))
    print(decoder._payload)
    sleep(1)

    if result.isError(): #Verifica se houve erro
        print(result)
        print("Erro ao ler registro do dispositivo")
    else:
        os.system("cls")
        print("<---------- SLAVE 1 ---------->")
        print("Info1: ", decoder._payload[7:9])
        print("Teste: " , kWh)
        print("Info1: ", int.from_bytes(kWh, byteorder = 'big'))
    
# .decode_16bit_int()
# Encerrar a conexão com o servidor Modbus

client.close()
