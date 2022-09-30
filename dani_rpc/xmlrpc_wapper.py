from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client as rpc_client
import config
IP = config.IP
PORT = config.PORT

class Server():
    def __init__(self, functions) -> None:
        x_server = SimpleXMLRPCServer((IP, PORT), allow_none=True)
        x_server.allow_reuse_address = True
        for func, func_name in functions.items():
            x_server.register_function(func, func_name)
        x_server.serve_forever()

class Client:
    def __init__(self) -> None:
        rpc_conection = rpc_client.ServerProxy(f"http://{IP}:{PORT}/")
        self.connection = rpc_conection


