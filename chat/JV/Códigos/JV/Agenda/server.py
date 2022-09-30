''' João Vítor Fernandes Dias - 28/08/2022
    Distributed systems class: Example program for RMI/RPC
'''
from xmlrpc.server import SimpleXMLRPCServer

def get_db ():
    '''returns a dictionary simulating a database'''
    db_agenda = {
        'agda': '(11) 9 9911-1111',
        'beto': '(22) 9 9922-2222',
        'ciro': '(33) 9 9933-3333',
        'deni': '(44) 9 9944-4444'
    }
    return db_agenda

def agenda(name):
    '''Programa base'''
    agenda_db = get_db()
    if name in agenda_db:
        return agenda_db[name]
    return 'not found'

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

    address = server_address['ip']+':'+server_address['port']
    message = messages['first_message'] + address
    print(message)
    server = SimpleXMLRPCServer((server_address['ip'], int(server_address['port'])))
    server.register_function(agenda, 'agenda')
    server.register_function(get_db, 'get_db')
    print(messages['await_message'])
    server.serve_forever()


def main ():
    '''main Server code'''
    configure_server ()

main()
