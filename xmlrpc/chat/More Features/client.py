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

def fill_with_spaces (str_name, size_to_reach):
    '''aesthetics'''
    return ' '*(size_to_reach-len(str_name))

def append_borders (str_name):
    '''aesthetics'''
    return '| ' + str_name + ' |\n'

def contacts_capsule (contact_list):
    '''Just prints the capsule with the messages'''
    header = 'Contact names'
    all_lines = []
    all_lines.append(header)
    all_lines.append(contact_list)
    max_size = max(list(map(len, all_lines)))
    line = '-'*(max_size)
    ab_line = append_borders(line)
    ab_header = append_borders(header)
    message = ab_line + ab_header + ab_line

    for elem in contact_list:
        message += append_borders(elem + fill_with_spaces(elem, max_size))
    message += ab_line + '\n'

    print(message)

def contact_capsule (name, phone_number):
    '''just a pretty box for the found phone number'''
    header = 'Phone of ' + name.upper()
    lines = [header, phone_number]
    max_size = max(list(map(len, lines)))
    line = '-'*max_size
    filled_header = header + fill_with_spaces(header, max_size)
    ab_header = append_borders(filled_header)
    filled_phone_number = phone_number + fill_with_spaces(phone_number, max_size)
    ab_phone_number = append_borders(filled_phone_number)


    ab_line = append_borders(line)
    message =  ab_line + ab_header
    message += ab_line + ab_phone_number
    message += ab_line + '\n'
    print(message)

def contact_server (server):
    '''doing stuff with the server'''
    name = ''
    messages = {
        'input_message': "\n Type:\n",
        'options': "\t - A person's name\n\
    \t - 'get names' to see all names\n\
    \t - 'exit' to quit the program\n",
        'error_message': '\n No match for this name',
        'exit_message': '\n Exiting program \n',
        'line': 18*'= '
    }

    while name != 'exit':
        name = ''
        name = input(messages['input_message'] + messages['options']).lower()

        if name == 'get names':
            contacts_capsule(list(server.get_db().keys()))
            continue
        if name == 'exit':
            print(messages['exit_message'])
            continue

        phone_number = server.agenda(name)
        if phone_number == 'not found':
            print(messages['error_message'])
        else:
            contact_capsule(name, phone_number)
        print (messages['line'])

def main ():
    '''main code'''
    address = get_address()
    connected_server = connect_to_address(address)
    contact_server(connected_server)

main()
