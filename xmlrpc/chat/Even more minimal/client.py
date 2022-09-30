''' João Vítor Fernandes Dias - 28/08/2022
    Distributed systems class: Example program for RMI/RPC
'''
import xmlrpc.client

IP= '26.26.5.240'
# IP_original= '127.0.0.1'
# IP_radmin= '26.26.5.240'
# IP_JV= '192.168.100.11'
PORT= '8080'

def connect_to_address ():
    '''Connecting to address'''
    global IP
    global PORT
    address = IP+':'+PORT
    server_url = 'http://'+address+'/'
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
    connected_server = connect_to_address()
    contact_server(connected_server)

main()
