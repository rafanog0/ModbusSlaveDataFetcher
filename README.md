# Documentação

Esse arquivo em markdown é uma documentação do que foi realizado até agora no projeto e as respectivas lições aprendidas.

O objetivo do projeto é obter leituras de um dispositivo Gavazzi EM-210 por meio de protocolo MODBUS e enviá-las para a nuvem Azure, para monitoramento de gasto energético na sala onde o dispositivo está instalado. 

Além disso, o projeto inicial envolve uso de inteligência artificial para monitoramento de quantidade de pessoas na sala por meio das plataformas do Azure Vision Studio e Câmera IP Hikivision Modelo DS-2CE57D3T para assim realizar leituras de número de pessoas no ambiente, e, desse modo, tomar decisões para controle de gastos energéticos.

Como questão de segurança, os códigos aqui apresentados não incluem as chaves para conexão com a Azure. Esse código é replicável e pode ser utilizado para qualquer implantação com a adaptação correta do código.



## Conectando leitor energético EM-210 via TCP-IP:

Para conectar ao EM-210, é necessário passar a conexão serial para ethernet. O conversor utilizado foi o USR-TCP232-304 da PUSR. Então, para acessar o que o conversor envia via protocolo TCP, é necessário sincronizar a máquina com a mesma rede de ip. 

Em nossos testes, a rede utilizada foi local, de IP ```192.168.0.7``` para o conversor e ```192.168.0.30``` para a máquina que recebe os dados. 

Testado o ip por meio do comando ```ping 192.168.0.7``` e verificada a conexão, é necessário auxílio de código para a primeira leitura ser feita.

O grupo utilizou da ferramenta "Radzio! Modbus Master Simulator" para testar e receber os dados já no formato TCP-IP.

Para formalização de uso, é necessário que o IP e a porta do Gavazzi sejam buscados pelo código que interpretará os dados, então foi utilizado o padrão do conversor, que é a porta ```8234```

## Código para leitura e recebimento de dados do slave:

Neste repositório, o arquivo ```modbus_to_azure.py``` enviará os dados não tratados para o Azure, e dependerá do Azure para responder quando houver requisição.

O código trabalha da seguinte forma para coletar os dados:

- Recebe o payload em RTU
- Decodifica para dados legíveis
- São escolhidos os dados relevantes ao escopo do projeto
- Coleta e imprime iteradamente a cada 1s em um .json as informações de: voltagem, amperagem e kWh e salva com o timestamp da coleta
- Cria um novo arquivo .json a cada hora com o timestamp da hora criada no formato: HHh-MMm.json
- Envia a cada hora o json para o Azure

## Entrega final
Para o cliente, entregamos a solução do código e esta documentação. Temos certeza da que a solução poderá ser replicada e ajudará a padronização da implantação de leitores de energia via RTU over TCP.
