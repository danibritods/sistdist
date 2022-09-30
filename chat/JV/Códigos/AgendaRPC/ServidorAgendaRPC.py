from xmlrpc.server import SimpleXMLRPCServer
# https://github.com/MarcosAndre5/SistemasDistribuidos
print('\tSERVIDOR')

IP = '127.0.0.1'
PORTA = 8080

def agenda(nome):
    if nome == 'marcos':
        return '(84) 9 9644-9431'
    elif nome == 'andre':
        return '(84) 9 9914-4420'
    elif nome == 'azevedo':
        return '(84) 9 9431-9644'
    elif nome == 'assis':
        return '(84) 9 1234-4567'
    elif nome == 'sair':
        return '0'
    else:
        return '1'

print('\nAVISO: O Não escrever no servidor.')

print('\nEsperando por clientes: ')

servidor = SimpleXMLRPCServer((IP, PORTA))

servidor.register_function(agenda, "agenda")

servidor.serve_forever()