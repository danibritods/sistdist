''' João Vítor Fernandes Dias - 28/08/2022
    Distributed systems class: Example program for RMI/RPC
'''
import xmlrpc.client
import random
from datetime import datetime

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

def connect_to_address ():
    '''Connecting to address'''
    address = get_address()
    str_address = address[0]+':'+str(address[1])
    server_url = 'http://'+str_address+'/'
    server = xmlrpc.client.ServerProxy(server_url)
    return server

def get_random_id(): # unused
    '''getting a name for the client'''
    br_states = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', \
        'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']
    number_of_names = len(br_states)
    random.seed(datetime.now())
    rand_index = random.randint(0, number_of_names-1)
    return br_states[rand_index]

def get_manual_id():
    '''returning a manual id'''
    line = '\n'+14*' = '+'\n'
    print(line)
    client_id = input('Type your name id:\n> ')
    print(line)
    return client_id

def sending_message(server, client_id):
    '''function for sending message'''
    messages = {
        'send_message': '\n Type "quit" to stop sending messages',
        'pre_send_message': '\n What do you want to send?\n',
        'get_receiver_message': 'Who do you want to send a message to?\n',
        'terminal_sign': '> ',
        'sending_sign': ' < ',
    }
    msg = ''
    line = '\n'+14*' = '+'\n'
    print(line)
    id_receiver = input(messages['get_receiver_message'] + messages['terminal_sign'])
    print(line)
    print(messages['send_message'])
    print(messages['pre_send_message'])
    while msg != 'quit':
        msg = input(id_receiver + messages['sending_sign'])
        server.send_message(client_id, id_receiver, msg)
    print(line)

def getting_message(server):
    '''receives pending messages'''
    messages = {
        'get_message': '\n Getting... \n',
    }
    print(messages['get_message'])
    received_log = server.get_message()
    print(received_log)

def get_menu_options ():
    '''just some menu layout and option'''
    messages = {
        'input_message': "\n Type:\n",
        'options': "\
\t - 'send' to send messages\n\
\t - 'get ' to get all messages\n\
\t - 'exit' to quit the program\n",
        'terminal_sign': '> ',
    }
    input_message = messages['input_message'] + messages['options'] + messages['terminal_sign']
    name = input(input_message).lower()
    return name

def contact_server_menu (server):
    '''doing stuff with the server'''
    messages = {
        'error_message': '\n No match for this name',
        'exit_message': '\n Exiting program \n',
        'line': 18*'= '
    }
    name = ''

    # client_id = get_random_id()
    client_id = get_manual_id()
    while name != 'exit':
        name = get_menu_options()
        if name == 'send':
            sending_message(server, client_id)
        if name == 'get':
            getting_message(server)
        if name == 'exit':
            print(messages['exit_message'])
        print (messages['line'])

def main ():
    '''main code'''
    connected_server = connect_to_address()
    contact_server_menu(connected_server)

main()
