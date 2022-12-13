''' João Vítor Fernandes Dias - 28/08/2022 ~~ 22/10/2022
    Distributed systems class: Example program for RMI/RPC
'''
import xmlrpc.client


def server_connection():
    '''abstraction for server connection. Should return a connected server object'''

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

    def connect_to_address(address):
        '''Connecting to address'''
        str_address = address[0]+':'+str(address[1])
        server_url = 'http://'+str_address+'/'
        server = xmlrpc.client.ServerProxy(server_url)
        return server

    return connect_to_address(get_address())


def sending_message(server, client_id):
    '''function for sending message.
    ToDo: The "switch" msg menu has room for improvements. Refactor it
    '''

    def messages_gui(prompts):
        '''user friendly interface'''
        print(prompts['line'])
        id_receiver = input(
            prompts['get_receiver_message'] + prompts['terminal_sign'])
        print(prompts['line'])
        print(prompts['input_message']+prompts['options'])
        print(prompts['send_message'])
        return id_receiver

    prompts = {
        'get_receiver_message': 'Who do you want to send messages to?\n',
        'terminal_sign': '> ',
        'input_message': "\n Type:\n",
        'options': "\
    \t - 'chng' to change receiver user's id\n\
    \t - 'quit' to stop sending messages\n",
        'send_message': '\n What do you want to send?\n',
        'sending_sign': ' < ',
        'line': '\n'+14*' = '+'\n'
    }
    id_receiver = messages_gui(prompts)
    msg = input(id_receiver + prompts['sending_sign'])
    while msg != 'quit':
        if msg == 'quit':
            continue
        if msg == 'chng':
            id_receiver = messages_gui(prompts)
            msg = input(id_receiver + prompts['sending_sign'])
        server.receiveMessage(client_id, id_receiver, msg)
        msg = input(id_receiver + prompts['sending_sign'])
    print(prompts['line'])


def getting_message(server, client_id):
    '''receives pending messages'''
    prompts = {
        'get_message': '\n Getting messages... \n',
    }
    print(prompts['get_message'])
    received_log = server.getMessage(client_id)
    print(received_log)


def contact_server_menu(server):
    '''Menu to communicate with the server'''

    def get_menu_options():
        '''just some menu layout and option'''
        prompts = {
            'input_message': "\n Type:\n",
            'options': "\
    \t - 'get'  to get all messages\n\
    \t - 'send' to send messages\n\
    \t - 'chng' to change sender user's id\n\
    \t - 'exit' to quit the program\n",
            'terminal_sign': '> ',
        }
        input_message = prompts['input_message'] + \
            prompts['options'] + prompts['terminal_sign']
        name = input(input_message).lower()
        return name

    def get_id():
        '''returns an string id for the user'''
        line = '\n'+14*' = '+'\n'
        print(line)
        client_id = input('Type your name id:\n> ')
        print(line)
        return client_id

    prompts = {
        'error_message': '\n No match for this name',
        'exit_message': '\n Exiting program \n',
        'line': 18*'= '
    }
    name = ''
    client_id = get_id()
    while name != 'exit':
        name = get_menu_options()
        if name == 'get':
            getting_message(server, client_id)
        if name == 'send':
            sending_message(server, client_id)
        if name == 'chng':
            client_id = get_id()
        if name == 'exit':
            print(prompts['exit_message'])
        print(prompts['line'])


def main():
    '''main code'''
    connected_server = server_connection()
    contact_server_menu(connected_server)


main()
