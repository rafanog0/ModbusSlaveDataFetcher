# Logs e workflow 
Esse arquivo servirá para registrar o que foi feito em cada dia do trabalho e quais escolhas foram tomadas ao longo do processo.
### 03-04 à 15-05
Foram realizados estudos extensos do protocolo Modbus, do Manual de comunicação e instalação do Gavazzi EM-210, do conector RTU to TCP USR-TCP232-304 da PUSR e das bibliotecas modbus-server e PyModBus para auxílio nas medições realizadas no projeto.
### 17-05-2023
Escolhida biblioteca PyModBus (python) ao invés da modbus-server(NPM e Node.Js) devido à facilidade do grupo com a linguagem e utilização ser mais rápida.
Primeiro código foi executado com sucesso no cliente real. 

### 19-05-2023
Refinamento do código e feitas escolhas de projeto. Foram definidas:
  - Quantas requisições serão feitas por período de tempo: uma leitura por segundo (no dispositivo), é salvo um novo arquivo a cada minuto e os 60 arquivos gerados são mandados à cada hora à rede Azure;
  - Como serão armazenados os dados no dispositivo: Os dados continuam no Raspberry por 7 dias, após 7 dias da coleta do dado, ele é apagado para evitar que a máquina fique sobrecarregada.

### 22-05-2023
Estudo e tentativa de implementação da solução de IoT da Azure com simulador de cliente e uso do código de servidor desenvolvido pelo grupo.

### 29-05-2023
Finalizada implantação com o cliente. Dados sendo enviados à Azure para processamento e tratamento de dados.

### 07-06-2023
Apresentação à Crazy Tech Labs

### 07-06-2023
Apresentação aos colegas da faculdade no encerramento do IDP Sprint


