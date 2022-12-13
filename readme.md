# **Relatório**

Este arquivo apresenta as informações como o objetivo do repositório, de que forma o código foi implementado, dentre outras que estão disponíveis logo abaixo.

<details>
<summary>

## **Introdução**

</summary>

Este repositório apresenta o trabalho do grupo constituído por [Daniel Brito dos Santos][GitHubDani], [João Vítor Fernandes Dias][GitHubJVFD] e [João Víttor Vieira Pinto][GitHubJVVP] para a disciplina *Sistemas Distribuídos* ministrada pelo professor [João Luiz][GitHubProf].

O trabalho consiste em desenvolver um sistema de comunicação por mensagens utilizando da abordagem de sistemas distribuídos RMI/RPC. Como durante a parte inicial do desenvolvimento, ocorreram divergências quanto a estrutura, biblioteca utilizada e paradigma de programação, optamos por desenvolver de forma segmentada, mesmo que todos tenham utilizado Python como linguagem de programação.

O Repositório está organizado em diversas pastas associadas a diversas vertentes de modelos de desenvolvimento que foram pesquisados e analisados como alternativas. Entretanto, os dois que apresentam maior relevância são os "dani_rpc" e o "jvfd_xmlrpc" que utilizam da biblioteca XMLRPC.

</details>

<details>
<summary>

## **Metodologia utilizada**

</summary>

Abaixo estão listadas alguns pontos marcantes em relação às escolhas tidas pelos integrantes do grupo quanto a linguagem, paradigmas, bibliotecas, e outros parâmetros utilizados ao longo do trabalho.

### Linguagem: Python 3

A linguagem [Python][LinkPython] foi escolhida por ser uma linguagem de alto nível de fácil entendimento. E também por ser uma linguagem de conhecimento comum dos integrantes. Além disso, por apresentar vasta gama de bibliotecas e implementações, ela se mostrou uma linguagem apropriada para o trabalho.

### Paradigma: Orientado a Objetos e Procedural

Inicialmente a proposta do trabalho seria desenvolver a aplicação utilizando a orientação a objetos. Entretanto, como forma de testar a heterogeneidade, uma dos problemas encontrados no desenvolvimento de sistemas distribuídos, optou-se por também ser desenvolvido uma aplicação utilizando o paradigma procedural.

### Bibliotecas: xmlrpc e socket

Diversas bibliotecas foram pesquisadas para cumprir com a proposta do trabalho, dentre elas [redis][LinkRedis], [redisrpc][LinkRedisrpc], [pyro 3][LinkPyro3], [RPyC][LinkRPyC], etc. Entretanto foram escolhidas as bibliotecas [xmlrpc][LinkXMLRPC] e [socket][LinkSocket]. A primeira por apresentar aplicações que aparentavam ser simples de entender e modificar, a segunda por permitir um contato mais direto entre o cliente e servidor, ambas sendo bibliotecas nativa do próprio Python.

### IDE: [Visual Studio Code][LinkVSCode]

É a IDE mais comumente utilizada pelos integrantes do grupo.

### Versionamento: [GitHub][LinkGitHub]

Uma das ferramentas de versionamento mais amplamente utilizada pelos desenvolvedores.

### Modelo de aplicação: Cliente-Servidor

Um dos modelos de aplicação propostos pelo professor para o desenvolvimento do trabalho.

</details>

<details>
<summary>

## **Resultados**

</summary>

Como foi implementado o sistema. Detalhes relevantes, como o programa tá estruturado, diagramas, testes realizados (metodologia) e resultados de fato

Como comentado previamente, diversas bibliotecas foram pesquisadas e também implementações respectivas, entretanto, essas empreitadas não se mostraram tão frutíferas. Abaixo seguem maiores informações quanto aos resultados alcançados.

### [Daniel Brito][GitHubDani]

<!-- Deixar Daniel preencher com mais detalhes depois -->
[Daniel Brito][GitHubDani] optou por desenvolver a comunicação em um modelo cliente-servidor, programando utilizando o paradigma orientado a objetos, assim como foi inicialmente solicitado no trabalho. Em seu código, ele utilizou a biblioteca xmlrpc. Seu código é constituído por 4 arquivos principais:

- chat.py
  - É onde estão as implementações das funções definidas em aula.
- chat_client.py
  - Lida com a interface do cliente e também apresenta um exemplo de execução.
- chat_server.py
  - Configura o servidor.
- xmlrpc_wrapper.py
  - Agrupa as funções padrões de cliente e servidor.

Além disso, também foi desenvolvido por ele um outro sistema de comunicação, também orientado a objetos com modelo cliente-servidor, mas dessa vez utilizando a biblioteca socket, tendo então uma abordagem de mais baixo nível para estabelecer uma conexão direta entre cliente e servidor que era antes auxiliada pelo xmlrpc. Este código, por ser mais direto, apresenta apenas um arquivo:

- sock_chat.py
  - Contém tudo, desde a implementação do servidor e cliente, até uma simulação da execução do programa.

### [João Dias][GitHubJVFD]

O aluno [João Dias][GitHubJVFD] optou por implementar o modelo cliente-servidor também utilizando a biblioteca [xmlrpc][LinkXMLRPC], entretanto, não utilizando do paradigma orientado a objetos. Sua implementação conta com dois arquivos:

- client.py
  - Conta com a conexão do cliente com o serviddor, sua interface e implementação das funções a serem executadas.
- server.py
  - Configura o servidor e define as funções que poderão ser chamadas pelos clientes.

Essa implementação, passou por algumas iterações que estão divididas em pastas, indo (mais ou menos) desde o mais simples ao mais avançado. Finalizando com uma aplicação que permite o envio de mensagem entre clientes e um servidor através de envios de mensagens de texto em formato de [json][LinkJson], para que possam ser processadas de forma padrão entre as aplicações dos alunos.

### [João Pinto][GitHubJVVP]

[João Pinto][GitHubJVVP] utilizou da implementação em [Python 2][LinkPython2] disponibilizada pelo Siddhartha Sahu em seu [GitHub][GitHubP2P] que apresenta uma estrutura simples e monolítica, entretanto, orientada a objetos, para que através das bibliotecas [Socket][LinkSocket] para conexão, [Tkinter][LinkTkinter] para interface gráfica e [Threads][LinkThread] para a distribuição de tarefas em diversas threads, consiga desenvolver uma aplicação de conexão remota para envio de mensagens através de IP e Porta.

<details> <summary>

### Testes

</summary>

Uma das propostas do trabalho era a de haver testes entre diversas implementações de uma aplicação. Aplicação essa, que desenvolvida seguindo um conjunto de padrões pré-estabelecidos, viria a superar a questão apontada da [heterogeneidade][LinkHeterogeneidade]. Afirmação essa que foi compravada com os testes descritos abaixo.

Os testes iniciais de uma forma geral envolviam utilizar, em um mesmo dispositivo, um cliente enviando mensagens para o servidor. Com o sucesso, diversas instâncias de clientes passaram a ser executadas para que houvesse a interação entre eles. Após os testes próprios, testes entre aplicações distintas foram realizados se encontram descritos abaixo.

Testes que foram realizados, mas que, até o presente momento não se mostraram bem sucedidos, envolvem o envio e recebimento de dados através da rede à distância. A não ser quando algum emulador de rede local como o [Hamachi][LinkHamachi] ou o [Radmin][LinkRadmin] eram utilizados. \[Necessita verificação\]

#### [João Dias][GitHubJVFD] ↔ [Daniel Brito][GitHubDani]

Embora ambas as aplicações tenham sido feitas por integrantes de um mesmo grupo, ainda assim foram desenvolvidas com paradigmas diferentes, o que poderia vir a se tornar uma problemática para a interação entre elas, problemática esta que não ocorreu, visto que a comunicação ocorrida foi bem sucedida.

Apenas em testes iniciais que essa comunicação não teve sucesso, entretanto, esse fato se deu pela tentativa de conexão através de um roteador da instituição que aparentemente restringia a conexão.

#### [João Dias][GitHubJVFD] ↔ [José Lucio][GitHubJose]

Agora sim sendo feita o teste entre grupos diferentes, a [aplicação][RepositorioJose] do [José Lucio][GitHubJose], também desenvolvida em [Python][LinkPython] conseguiu se comunicar com a do [João Dias][GitHubJVFD], entretanto um comportamento inesperado foi percebido em relação ao retorno do servidor desenvolvido pelo [José Lucio][GitHubJose]: seu servidor, ao retornar a listagem das mensagens armazenadas, acabava enviando com um par extra de colchetes, comportamento esse não esperado segundo as normas estabelecidas em sala de aula. Entretanto, não aparenta ser uma questão crítica e se mostra contornável.

</details>

</details>

<details>
<summary>

## **Conclusão**

</summary>

Mais importante: mais relevante do que aprendeu e aplicou. Limitações do programa. Aplicabilidade dos conceitos. Como melhorar o programa? Desafios?

Embora envolto de diversos contratempos e problemas ao longo do desenvolvimento, a finalização do trabalho se mostrou bem sucedida com alguns apontamentos mais específicos a serem comentados com mais detalhes.

### Aprendizados

Como aprendizado geral, foi possível visualizar na prática diversas formas possíveis de se estabelecer conexões remotas entre vários dispositivos, bem como os problemas encontrados neste processo e como os solucionar. Houve maior aprofundamento em conceitos de conexão remota, gestão de transferência de mensagens entre dispositivos e em como essa relação pode ser feita através da chamada remota de procedimentos.

### Limitações

Uma das maiores limitações encontradas no desenvolvimento foi a incerteza quando a causa de alguns problemas que surgiram durante os testes, não ficando bem especificado se estava ocorrendo por questão de hardware (envolvendo os roteadores, por exemplo), ou se havia ocorrido uma falha na implementação.

Atualmente, não ocorre de forma simples a conexão remota entre diferentes redes através da internet, o que se mostrou uma limitação considerável, visto que idealmente essa funcionalidade teria sido alcançada.

### Aprimoramentos

Como aprimoramentos para as aplicações apontadas, vê-se a listagem do arquivo [ToDo.md][HiperLinkToDo], mas podendo ser ilustrados alguns aqui.

- [ ] Tentar trocar mensagens entre threads
- [ ] Tentar trocar mensagens entre redes distintas
- [ ] Definir ID único para cada cliente
- [ ] Direção da mensagem
  - [ ] Unicast
  - [ ] Multicast
  - [ ] Broadcast
- [ ] Definir timestamp para cada mensagem
- [ ] Criar sistema de status online
- [ ] Armazenar os as mensagens recebidas pelo servidor de forma permanente
- [ ] Tentar reenviar mensagens perdidas
- [ ] Realizar filtragem de mensagens duplicadas
- [ ] Reenvio de mensagem em caso de perda

</details>

<!-- # Introdução -->
[GitHubProf]: https://github.com/jlalmeidaf
[GitHubJVFD]: https://github.com/jvfd3
[GitHubDani]: https://github.com/dbs-97
[GitHubJVVP]: https://github.com/jvvp2000
<!-- ## Linguagem -->
[LinkPython]: https://www.python.org/downloads/
<!-- ## Bibliotecas -->
[LinkRedis]: https://docs.redis.com/latest/rs/references/client_references/client_python/
[LinkRedisrpc]: https://github.com/nfarring/redisrpc
[LinkPyro3]: https://pypi.org/project/Pyro/
[LinkRPyC]: https://rpyc.readthedocs.io/en/latest/
[LinkXMLRPC]: https://docs.python.org/3/library/xmlrpc.html
[LinkSocket]: https://docs.python.org/3/library/socket.html
[LinkVSCode]: https://code.visualstudio.com/
[LinkGitHub]: https://github.com
<!-- ## Resultados -->
[LinkJson]: https://www.json.org/json-pt.html
[LinkPython2]: https://www.python.org/download/releases/2.0/
[GitHubP2P]: https://github.com/sdht0/P2P-chat-application
[LinkTkinter]: https://docs.python.org/3/library/tkinter.html
[LinkThread]: https://docs.python.org/3/library/threading.html
[LinkHeterogeneidade]: https://sites.google.com/site/proffdesiqsistemasdistribuidos/aulas/caracterizacao-de-sistemas-distribuidos#:~:text=que%20podem%20ser-,heterog%C3%AAneos,-%2C%20com%20diferentes%20sistemas
[GitHubJose]: https://github.com/zehlu
[LinkHamachi]: https://www.vpn.net/
[LinkRadmin]: https://www.radmin-vpn.com/
[RepositorioJose]: https://github.com/Zehlu/Trabalho_de_distribuidos
<!-- ## Conclusão -->
<!--  -->
[HiperLinkToDo]: https://github.com/