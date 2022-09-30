from xmlrpc.server import SimpleXMLRPCServer
IP = '127.0.0.0'
PORT = 9003

class XML_server():
    def __init__(self, functions) -> None:
        self.ip = IP
        self.port = PORT
    
        x_server = SimpleXMLRPCServer((IP, PORT), allow_none=True, bind_and_activate=False)
        for func, func_name in functions.items():
            x_server.register_function(func, func_name)
        x_server.serve_forever()


# s = Server()
# f = {s.get_msg:"get_msg",
#      s.receive_msg: "receive_msg"} 
# xs = XML_server(f)