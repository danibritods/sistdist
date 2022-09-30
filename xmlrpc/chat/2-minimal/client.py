''' João Vítor Fernandes Dias - 28/08/2022
    Distributed systems class: Example program for RMI/RPC
'''
import xmlrpc.client

def get_address (default_address = 'no'):
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

def connect_to_address (server_address):
    '''Connecting to address'''
    first_message = 'Establishing server connection to '
    address = server_address['ip']+':'+server_address['port']
    server_url = 'http://'+address+'/'
    message = first_message + server_url
    print(message)
    server = xmlrpc.client.ServerProxy(server_url)
    return server

def contact_server (server):
    '''doing stuff with the server'''
    name = ''
    messages = {
        'input_message': "\n Type:\n",
        'options': "\
\t - 'exit' to quit the program\n\
\t - 'send' to send messages\n\
\t - 'get ' to get all messages\n",
        'error_message': '\n No match for this name',
        'exit_message': '\n Exiting program \n',
        'send_message': '\n Type "quit" to stop sending messages',
        'pre_send_message': '\n What do you want to send?\n',
        'skip_input': '> ',
        'get_message': '\n Getting... \n',
        'line': 18*'= '
    }

    while name != 'exit':
        name = input(messages['input_message'] + messages['options']).lower()

        if name == 'exit':
            print(messages['exit_message'])
            continue
        if name == 'send':
            msg = ''
            print(messages['send_message'])
            print(messages['pre_send_message'])
            while msg != 'quit':
                msg = input(messages['skip_input'])
                server.send_message(msg)
        if name == 'get':
            print(messages['get_message'])
            received_log = server.get_message()
            print(received_log)


        print (messages['line'])

def main ():
    '''main code'''
    address = get_address()
    connected_server = connect_to_address(address)
    contact_server(connected_server)

main()
