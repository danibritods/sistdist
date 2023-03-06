# **Relatório**

Este repositório apresenta o trabalho do grupo constituído por [Daniel Brito dos Santos][GitHubDani], [João Vítor Fernandes Dias][GitHubJVFD] e [João Víttor Vieira Pinto][GitHubJVVP] para a disciplina *Sistemas Distribuídos* ministrada pelo professor [João Luiz][GitHubProf].

<details>
<summary>

## **Introdução**

</summary>

A proposta da disciplina foi desenvolver um sistema de comunicação por mensagem utilizando das técnicas estudadas no contexto de sistemas distribuídos. A maior parte do desenvolvimento envolveu a implementação de um chat utilizando chamadas remotas de procedimento e o processo de fazer implementações heterogêneas funcionarem de forma transparente ao usuário. 

Como durante a parte inicial do desenvolvimento, ocorreram divergências quanto a estrutura, biblioteca utilizada e paradigma de programação, optamos por desenvolver de forma segmentada, mesmo que todos tenham utilizado Python como linguagem de programação.

O Repositório está organizado em diversas pastas associadas a diversas vertentes de modelos de desenvolvimento que foram pesquisados e analisados como alternativas. Entretanto, os dois que apresentam maior relevância são os "[dani_rpc][LinkDaniRpc]" e o "[jvfd_xmlrpc][LinkJvfdXmlRpc]" que utilizam da biblioteca XMLRPC.

</details>

<details>
<summary>

## **Metodologia utilizada**

</summary>

Abaixo estão listadas alguns pontos marcantes em relação às escolhas tidas pelos integrantes do grupo quanto a linguagem, paradigmas, bibliotecas, e outros parâmetros utilizados ao longo do trabalho.

### Linguagem: Python 3

A linguagem [Python][LinkPython] foi escolhida por ser uma linguagem de alto nível de fácil entendimento. E também por ser uma linguagem de conhecimento comum dos integrantes. Além disso, por apresentar vasta gama de bibliotecas e implementações, ela se mostrou uma linguagem apropriada para o trabalho. Especialmente porque permite o nível certo de abstração para a aprendizagem do conceito, sem sobrecarregar o desenvolvedor com seus detalhes de baixo nível. 

### Paradigma: Orientado a Objetos e Procedural

Inicialmente a proposta do trabalho seria desenvolver a aplicação utilizando a orientação a objetos. Entretanto, como forma de testar a heterogeneidade, uma dos problemas encontrados no desenvolvimento de sistemas distribuídos, optou-se por também ser desenvolvido uma aplicação utilizando o paradigma procedural.

### Bibliotecas: xmlrpc e socket

Diversas bibliotecas foram pesquisadas para cumprir com a proposta do trabalho, dentre elas [redis][LinkRedis], [redisrpc][LinkRedisrpc], [pyro 3][LinkPyro3], [RPyC][LinkRPyC], etc. Entretanto foram escolhidas as bibliotecas [xmlrpc][LinkXMLRPC] e [socket][LinkSocket]. A primeira por apresentar aplicações que aparentavam ser simples de entender e modificar, a segunda por permitir um contato mais direto entre o cliente e servidor, ambas sendo bibliotecas nativa do próprio Python.
Também utilizamos a biblioteca nativa de threads para executar paralelamente os serviços necessários ao funcionamento do programa de forma transparente ao usuário.

### IDE: [Visual Studio Code][LinkVSCode]

É a IDE mais comumente utilizada pelos integrantes do grupo.

### Versionamento: [GitHub][LinkGitHub]

Uma das ferramentas de versionamento mais amplamente utilizada pelos desenvolvedores.

### Modelo de aplicação: Cliente-Servidor e P2P

Foram os modelos de aplicação propostos pelo professor para o desenvolvimento do trabalho.
Sendo que o modelo p2p foi implementado a título de prova de conceito, enquanto o cliente-servidor pôde ser explorado com mais detalhes devido a disparidade de tempo e contexto disponíveis para cada um deles. 

</details>

<details>
<summary>

## **Resultados**

</summary>

Como foi implementado o sistema. Detalhes relevantes, como o programa tá estruturado, diagramas, testes realizados (metodologia) e resultados de fato

Como comentado previamente, diversas bibliotecas foram pesquisadas e também implementações respectivas, entretanto, essas empreitadas não se mostraram tão frutíferas. Abaixo seguem maiores informações quanto aos resultados alcançados.

### [Daniel Brito][GitHubDani]

<!-- Deixar Daniel preencher com mais detalhes depois -->
[Daniel Brito][GitHubDani] inicialmente optou por implementar um sistema de comunicação, orientado a objetos no modelo cliente-servidor, utilizando a biblioteca socket. Uma abordagem de mais baixo nível para estabelescer a transmissão de mensagens entre cliente e servidor. O código está contido no arquivo [sock_chat.py](./socket/sock_chat.py) que apresenta desde a implementação do servidor e cliente por meio do envio de mensagens através do socket tipo TCP até um teste rápido e uma interface simples to tipo CLI. 

Em um segundo momento, visando a interconectividade com outras implementações, o aluno implementou uma segunda versão do chat, agora mais completa em funcionalidades, utilizando da biblioteca xmlrpc. Seu código é constituído por 4 arquivos principais:

- [chat.py](./dani_rpc/chat.py)
  - Implementa o mecanismo de funcionamento do chat. Nele estão as funções definidas em aula, bem como todo o seu mecanismo. 
- [xmlrpc_wrapper.py](./dani_rpc/xmlrpc_wrapper.py)
  - Agrupa as funções necessárias para encapsular o modelo cliente-servidor da biblioteca xmlrpc 
- [chat_server.py](dani_rpc/chat_server.py)
  - Encapsula o servidor implementado no módulo chat com o servidor-rpc da biblioteca xmlrpc.
- [chat_client.py](dani_rpc/chat_client.py)
  - Faz a interface entre a implementação do cliente do módulo chat com o cliente da biblioteca xmlrpc

### [João Dias][GitHubJVFD]

O aluno [João Dias][GitHubJVFD] optou por implementar o modelo cliente-servidor também utilizando a biblioteca [xmlrpc][LinkXMLRPC], entretanto, não utilizando do paradigma orientado a objetos. Sua implementação conta com dois arquivos:

- client.py
  - Conta com a conexão do cliente com o serviddor, sua interface e implementação das funções a serem executadas.
- server.py
  - Configura o servidor e define as funções que poderão ser chamadas pelos clientes.

Essa implementação, passou por algumas iterações que estão divididas em pastas, indo (mais ou menos) desde o mais simples ao mais avançado. Finalizando com uma aplicação que permite o envio de mensagem entre clientes e um servidor através de envios de mensagens de texto em formato de [json][LinkJson], para que possam ser processadas de forma padrão entre as aplicações dos alunos.

### [João Pinto][GitHubJVVP]

[João Pinto][GitHubJVVP] utilizou da implementação em [Python 2][LinkPython2] disponibilizada pelo Siddhartha Sahu para recriar um aplicativo similar em Peer-to-Peer que utiliza de Sockets como principal meio de comunicação. O aplicativo sofreu alterações para, principalmente, adaptar o código para o Python 3. Sobre a arquitetura desse: 
- chatApp.py
    - que apresenta uma estrutura simples e monolítica, entretanto, orientada a objetos, para que através das bibliotecas [Socket][LinkSocket] para conexão, [Tkinter][LinkTkinter] para interface gráfica e [Threads][LinkThread] para a distribuição de tarefas em diversas threads (como o funcionamento do servidor e cliente ao mesmo tempo).  

O objetivo principal desse arquivo é o desenvolvimento uma aplicação de conexão remota para envio de mensagens através de IP e Porta, que possui uma como principal característica ser Peer-to-Peer. Essa arquitetura (P2P) é um sistema para compartilhamento de informações sem a necessidade de um servidor central, ou seja, cada um tem o seu servidor que conecta com o cliente em que você quer falar. 

<details> <summary>

### Testes

</summary>

Uma das propostas do trabalho era a de haver testes entre diversas implementações de uma aplicação. Aplicação essa, que desenvolvida seguindo um conjunto de padrões pré-estabelecidos, viria a superar a questão apontada da [heterogeneidade][LinkHeterogeneidade]. O que de fato foi comprovado com os testes descritos abaixo.

Os testes iniciais de uma forma geral envolviam utilizar, em um mesmo dispositivo, um cliente enviando mensagens para o servidor. Com o sucesso, diversas instâncias de clientes passaram a ser executadas para que houvesse a interação entre eles. Após os testes próprios, testes entre aplicações distintas foram realizados se encontram descritos abaixo.

Testes que foram realizados, mas que, até o presente momento não se mostraram bem sucedidos, envolvem o envio e recebimento de dados através da rede à distância. A não ser quando algum emulador de rede local como o [Hamachi][LinkHamachi] ou o [Radmin][LinkRadmin] eram utilizados. Isso ocorre em função da própria organização da rede mundial de computadores, visto que os endereços de ip de cada computador são uma abstração do endereço real do provedor, e portanto, sem um servidor com ip externo próprio não nos é possível conectar fora de nosso roteador em comum, a não ser que utilizemos uma "rede local" fictícia sobre a rede real, como um vpn por exemplo. 

#### [João Dias][GitHubJVFD] ↔ [Daniel Brito][GitHubDani]

Embora ambas as aplicações tenham sido feitas por integrantes de um mesmo grupo, ainda assim foram desenvolvidas com paradigmas diferentes, com mecanismos internos diferentes, o que poderia vir a se tornar uma problemática para a interação entre elas, problemática esta que não ocorreu, visto que a comunicação ocorrida foi bem sucedida.

Apenas em testes iniciais que essa comunicação não teve sucesso, entretanto, esse fato se deu pela tentativa de conexão através de um roteador da instituição que aparentemente restringia a conexão.

#### [João Dias][GitHubJVFD] ↔ [José Lucio][GitHubJose]

Agora sim sendo feita o teste entre grupos diferentes, a [aplicação][RepositorioJose] do [José Lucio][GitHubJose], também desenvolvida em [Python][LinkPython] conseguiu se comunicar com a do [João Dias][GitHubJVFD], entretanto um comportamento inesperado foi percebido em relação ao retorno do servidor desenvolvido pelo [José Lucio][GitHubJose]: seu servidor, ao retornar a listagem das mensagens armazenadas, acabava enviando com um par extra de colchetes, comportamento esse não esperado segundo as normas estabelecidas em sala de aula. Entretanto, não aparenta ser uma questão crítica e se mostra contornável.

#### [Daniel Brito][GitHubDani] ↔ [José Lucio][GitHubJose]

As aplicações desses dois alunos se mostraram completamente compatíveis. Qualquer um dos servidores foi capaz de servir clientes simultaneos das duas implementações.

#### Conclusões

A partir dos testes realizados, ficou claro que nossas implementações são plenamente compatíveis com quaisquer outras que sigam as mesmas diretrizes de interface. Mesmo que não tenhamos conseguido testar com todos os grupos ficou claro que os resultados seriam os mesmos. 
Uma vez que a chamada remota de método efetua toda a abstração necessária para funcionar como a execução local de uma função. 



</details>

</details>

<details>
<summary>

## **Conclusão**

</summary>

Mais importante: mais relevante do que aprendeu e aplicou. Limitações do programa. Aplicabilidade dos conceitos. Como melhorar o programa? Desafios?

Embora envolto de diversos contratempos e problemas ao longo do desenvolvimento, a finalização do trabalho se mostrou bem sucedida com alguns apontamentos mais específicos a serem comentados com mais detalhes.

### Aprendizados

Como aprendizado geral, foi possível visualizar na prática diversas formas possíveis de se estabelecer conexões remotas entre vários dispositivos, bem como os problemas encontrados neste processo e como os solucionar. Houve maior aprofundamento em conceitos de conexão remota, uso de sockets na prática, threading,  gestão de transferência de mensagens entre dispositivos e em como essa relação pode ser feita através da chamada remota de procedimentos e sockets.  

Também aprendemos questões mais intagíveis como a maturidade de desenvolvimento no que tange todos os processos necessários para "trazer a vida" um sistema. Praticamos comunicação e cooperação, deliberação empreendedora, análise de software. Adquirimos maior experiência na resolução de problemas, e uma visão mais precisa e embasado de sistemas distribuídos como campo de conhecimento.

### Limitações

Uma das maiores limitações encontradas no desenvolvimento foi a incerteza quando a causa de alguns problemas que surgiram durante os testes, não ficando bem especificado se estava ocorrendo por questão de hardware (envolvendo os roteadores, por exemplo), ou se havia ocorrido uma falha na implementação. Mas eventualmente todos foram contornados ou compreendidos. 

Atualmente, não ocorre de forma simples a conexão remota entre diferentes redes através da internet, o que se mostrou uma limitação considerável, visto que idealmente essa funcionalidade teria sido alcançada. Mas entendemos que é uma limitação da própria arquitetura de redes, e em um desenvolvimento futuro podemos solucionar utilizando servidores remotos. 

### Aprimoramentos

Como aprimoramentos para as aplicações apontadas, vê-se a listagem do arquivo [ToDo.md][HiperLinkToDo], mas podendo ser ilustrados alguns aqui.

- [ ] Tentar trocar mensagens entre redes distintas
- [ ] Definir timestamp para cada mensagem
- [ ] Definir ID único para cada cliente de forma generativa. 
- [ ] Implementar criptografia
- [ ] Permitir envios personalizados como multicast e broadcast
- [ ] Criar sistema de status online
- [ ] Armazenar os as mensagens recebidas pelo servidor de forma permanente
- [ ] Tentar reenviar mensagens perdidas
- [ ] Realizar filtragem de mensagens duplicadas
- [ ] Reenvio de mensagem em caso de perda
- [ ] Implementar todas as funcionalidades em uma arquitetura p2p
- [ ] Mapa topológico da rede para maior eficiência
- [ ] Ter um servidor externo para que os peers se encontrem

</details>

<!-- # Introdução -->
[GitHubProf]: https://github.com/jlalmeidaf
[GitHubJVFD]: https://github.com/jvfd3
[GitHubDani]: https://github.com/danibritods
<!-- [GitHubJVVP]: https://github.com/jvvp2000 -->
[GitHubJVVP]: https://github.com/vittorpinto
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
[HiperLinkToDo]: https://github.com/dbs-97/sistdist/blob/main/TODO.md#todo
[LinkDaniRpc]: ./dani_rpc/
[LinkJvfdXmlRpc]: ./jvfd_xmlrpc/
