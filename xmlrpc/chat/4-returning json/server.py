''' João Vítor Fernandes Dias - 28/08/2022
    Distributed systems class: Example program for RMI/RPC
'''
from xmlrpc.server import SimpleXMLRPCServer

index = 1
message_log_v1 = ''
message_log_v2 = {}
# {"Daniel" : ["oi", "tudo bem?"] , "Joao Vitor" : ["Te pago amanha"]}


def get_address():
    '''returning address'''
    selection = ['IP_original', 'IP_radmin_JVFD', 'IP_radmin_JVVP']
    IPS= {
        selection[0]: '127.0.0.1',
        selection[1]: '26.41.56.188',
        selection[2]: '26.12.16.183',
    }
    IP= IPS[selection[1]]
    PORT= '8080'
    return (IP, int(PORT))


'''
id_receiver = input(messages['get_receiver'])

# Adicionando valor de chave aninhada ao dicionário
Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'Geeks'}}
print("\nAdding a Nested Key: ")
print(Dict)

dict_message[id_receiver]={id_sender : message}

SERVER{
    B:{
        {
            "A": "oipudim"
        }
    }
    C:{
        {"A":["tchaupudim", "oidnv"]
        "B":["gato"]}
      }
}

CLIENT{A}
    B:oipudim
    C:tchaupudim
    C:oidnv
    getmsg
    <- {}
CLIENT{B}
    C:gato
    getmsg
    <- {"A": ["oipudim"]}
CLIENT{C}
    getmsg
    <- {"A": ["tchaupudim", "oidnv"], "B": ["gato"]}
'''


def global_log_1(id_sender, id_receiver='', msg=''):
    '''logging'''
    global message_log_v1
    global message_log_v2
    global index
    send_capsule = f'"{id_sender}" = ({msg}) => "{id_receiver}"\n'
    message = f'{index})\tsend_message:\t {send_capsule}\n'
    message_log_v1 += message
    index += 1
    print(message)

def global_log_2(id_sender, id_receiver,msg):
    '''abc
    '''
    global message_log_v2
    if message_log_v2[id_receiver][id_sender] == {} :
        message_log_v2[id_receiver][id_sender] = [msg]
    to_insert = message_log_v2[id_receiver][id_sender]
    to_insert.append(msg)
    message_log_v2[id_receiver][id_sender] = to_insert


def get_message ():
    '''gets message from the server'''
    global message_log_v1
    global index
    message = f'{index})\tget_message\n'
    message_log_v1 += message
    index += 1
    # print(message_log)
    return message_log_v1

def send_message(client_id, id_receiver, msg='placeholder'):
    '''the client sends a message to someone and it is stored'''
    global_log_1(client_id, id_receiver, msg)
    global_log_2(client_id, id_receiver, msg)

def configure_server ():
    '''configuring server'''
    server = SimpleXMLRPCServer(get_address(), allow_none=True)
    server.register_function(get_message, 'get_message')
    server.register_function(send_message, 'send_message')
    server.serve_forever()

def main():
    '''main Server code'''
    configure_server()

main()
