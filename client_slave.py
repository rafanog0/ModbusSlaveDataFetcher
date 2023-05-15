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
    result = client.read_holding_registers(address = 0, count = 5, slave = SLAVE_ADDRESS) # Ler um registro do dispositivo "slave"
    decoder = BinaryPayloadDecoder.fromRegisters(result.registers, byteorder=Endian.Big)
    
    sleep(1)

    if result.isError(): #Verifica se houve erro na leitura
        print(result)
        print("Erro ao ler registro do dispositivo")
    else:
        os.system("cls")
        print("<---------- SLAVE 1 ---------->")
        print("Info1: ", decoder.decode_16bit_int())

# Encerrar a conexão com o servidor Modbus

client.close()
