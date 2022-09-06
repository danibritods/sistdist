''' João Vítor Fernandes Dias - 28/08/2022
    Distributed systems class: Example program for RMI/RPC
'''
from xmlrpc.server import SimpleXMLRPCServer

message_log = ''
index = 1

def get_message ():
    '''aaa'''
    global message_log
    global index
    message = f'{index})\tget_message\n'
    message_log += message
    index += 1
    # print(message_log)
    return message_log

def send_message (msg='placeholder'):
    '''aaa'''
    global message_log
    global index
    message = f'{index})\tsend_message\t"{msg}"\n'
    message_log += message
    index += 1
    print(message)

def get_address(default_address = 'no'):
    '''getting address'''
    messages = {
        'input_message': 'Do you want to manually input your address?',
        'options': '\n1) Yes\nElse) No\n> ',
        'line': 18*'= ',
        'manual_input_message': '\n Please type your ',
    }

    option = 0
    if default_address == 'no':
        print(messages['line'])
        option = input (messages['input_message'] + messages['options'])

    has_manual_input = option == '1'

    if has_manual_input:
        address_ip = input(messages['manual_input_message']+'ip:\n> ')
        address_port = input(messages['manual_input_message']+'port:\n> ')
        used_address = {
            'ip': address_ip,
            'port': address_port
        }
    else:
        used_address = {
            'ip': '127.0.0.1',
            'port': '8080'
        }
    print(messages['line'])
    return used_address

def configure_server ():
    '''configuring server'''
    server_address = get_address()
    messages = {
        'first_message': 'SERVER CONNECTED AT ',
        'await_message': 'Waiting for clients . . .'
    }
    ip = server_address['ip']
    port = server_address['port']
    address = ip + ':' + port
    message = messages['first_message'] + address
    print(message)
    server = SimpleXMLRPCServer((ip, int(port)), allow_none=True)
    server.register_function(get_message, 'get_message')
    server.register_function(send_message, 'send_message')
    print(messages['await_message'])
    server.serve_forever()

def main ():
    '''main Server code'''
    configure_server ()

main()
