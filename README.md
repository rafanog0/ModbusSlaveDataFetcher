# Documentação

Esse arquivo em markdown é uma documentação do que foi realizado até agora no projeto e as respectivas lições aprendidas.

O objetivo do projeto é obter leituras de um dispositivo Gavazzi EM-210 por meio de protocolo MODBUS e enviá-las para a nuvem Azure, para monitoramento de gasto energético na sala onde o dispositivo está instalado. 

Além disso, o projeto inicial envolve leitura e uso de inteligência artificial para monitoramento de quantidade de pessoas na sala, para assim poder entender o gasto energético por pessoa presente, e, desse modo, tomar decisões para redução de gasto energético.




## Conectando via TCP-IP

Para conectar ao EM-210, é necessário passar a conexão serial para ethernet. O conversor utilizado foi o USR-TCP232-304 da PUSR. Então, para acessar o que o conversor envia via protocolo TCP, é necessário sincronizar a máquina com a mesma rede de ip. 

Em nossos testes, a rede utilizada foi local, de IP ```192.168.0.7``` para o conversor e ```192.168.0.30``` para a máquina que recebe os dados. 

Testado o ip por meio do comando ```ping 192.168.0.7``` e verificada a conexão, é necessário auxílio de código para a primeira leitura ser feita.

O grupo utilizou da ferramenta "Radzio! Modbus Master Simulator" para testar e receber os dados já no formato TCP-IP.

Para formalização de uso, é necessário que o IP e a porta do Gavazzi sejam buscados pelo código que interpretará os dados, então foi utilizado o padrão do conversor, que é a porta ```8234```

É necessário estabeler a forma mais econômica possível para leitura e interpretação de dados, já que a Azure cobra por requisição e por quantidade de dados enviados. Para isso, o grupo estudou se é possivel fazer uma requisição por meio da câmera: cada vez que a quantidade de pessoas na sala mudar, é feita uma requisição de leitura de gasto energético. Com esses dados, fica possível fazer uma diferença da forma 
```Δe * Δt / nPessoas``` ,onde:

  Δe = variação do gasto energético em kW;

  Δt = variação do tempo t2 - t1

  nPessoas = quantidade de pessoas na sala

  




