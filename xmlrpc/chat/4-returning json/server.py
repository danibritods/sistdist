''' João Vítor Fernandes Dias - 28/08/2022
    Distributed systems class: Example program for RMI/RPC
'''
from xmlrpc.server import SimpleXMLRPCServer

index = 1
message_log_v1 = ''
message_log_v2 = {}
# {"Daniel" : ["oi", "tudo bem?"] , "Joao Vitor" : ["Te pago amanha"]}


def global_log_1(id_sender, id_receiver='', msg=''):
    '''logging'''
    global message_log_v1
    global index
    send_capsule = f'"{id_sender}" = ({msg}) => "{id_receiver}"\n'
    message = f'{index})\tsend_message:\t {send_capsule}\n'
    message_log_v1 += message
    index += 1
    print('\n', message)


def global_log_2(id_sender, id_receiver, msg):
    '''Storing all the server messages in a json format
    '''
    global message_log_v2
    local_message_log = message_log_v2
    is_first_receiver_user = id_receiver not in local_message_log
    if is_first_receiver_user:
        local_message_log.setdefault(id_receiver, {id_sender: [msg]})
    else:
        is_first_sender_user = id_sender not in local_message_log[id_receiver]
        if is_first_sender_user:
            local_message_log[id_receiver].setdefault(
                id_sender, [msg])
        else:
            local_message_log[id_receiver][id_sender].append(msg)
    print(local_message_log, '\n')
    message_log_v2 = local_message_log


def getMessage(id_sender):
    '''gets message from the server'''
    global message_log_v1
    global index
    message = f'{index})\tget_message: \t "{id_sender}"\n'
    message_log_v1 += message
    index += 1
    print(message)
    global message_log_v2

    local_message_log = message_log_v2
    msg_to_send_back = {}
    has_messages = id_sender in local_message_log
    if has_messages:
        msg_to_send_back = message_log_v2[id_sender]
    return msg_to_send_back


def receiveMessage(client_id, id_receiver, msg='placeholder'):
    '''the client sends a message to someone and it is stored'''
    global_log_1(client_id, id_receiver, msg)
    global_log_2(client_id, id_receiver, msg)


def configure_server():
    '''configuring server'''

    def get_address(ip_option=0, port_option=0):
        '''returning address'''
        IPS = {
            0: '127.0.0.1',  # localhost (?)
            1: '26.41.56.188',  # Smartphone JVFD (ou radmin)
            2: '26.12.16.183',  # IP_radmin_JVVP
            3: '192.168.43.141',  # DaniBrito
            4: '192.168.0.110',  # DaniBrito novo
            5: '192.168.43.141/24',  # DaniBrito
            6: '192.168.0.107',  # JVFD
            7: '26.41.56.188',  # JVFD  Radmin
            8: '192.168.1.238',  # ZehLu
        }
        PORTs = {
            0: '8080',  # JV
            1: '9003',  # Dani Brito
            2: '8085',  # ZehLu
        }
        IP = IPS[ip_option]
        PORT = PORTs[port_option]
        return (IP, int(PORT))

    prompts = {
        'configuring': '\nStarting server configuration...',
        'ready': 'Server is ready to handle calls.\n'
    }
    print(prompts['configuring'])
    server = SimpleXMLRPCServer(get_address(), allow_none=True)
    server_functions = {
        getMessage: 'getMessage',
        receiveMessage: 'receiveMessage'
    }
    for func, func_name in server_functions.items():
        server.register_function(func, func_name)
    print(prompts['ready'])
    server.serve_forever()


def main():
    '''main Server code'''
    configure_server()


main()
