''' João Vítor Fernandes Dias - 28/08/2022
    Distributed systems class: Example program for RMI/RPC
'''
from xmlrpc.server import SimpleXMLRPCServer

message_log = ''
message_log_v2 = {}
index = 1
IP= '26.41.56.188'
# IP_original= '127.0.0.1'
# IP_radmin= '26.41.56.188'
# IP_JV= '192.168.100.11'
PORT= '8080'
# {"Daniel" : ["oi", "tudo bem?"] , "Joao Vitor" : ["Te pago amanha"]}
'''
SERVER{
    B:["A": "oipudim"]
    C:[
        "A":["tchaupudim", "oidnv"]
        "B":["gato"]
      ]
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

def configure_server ():
    '''configuring server'''
    global IP
    global PORT
    server = SimpleXMLRPCServer((IP, int(PORT)), allow_none=True)
    server.register_function(get_message, 'get_message')
    server.register_function(send_message, 'send_message')
    server.serve_forever()

def main ():
    '''main Server code'''
    configure_server ()

main()
