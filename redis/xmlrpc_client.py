import xmlrpc.client as x_client
import config
IP = config.IP
PORT = config.PORT

class XML_client:
    def __init__(self) -> None:
        x_server = x_client.ServerProxy(f"http://{IP}:{PORT}")
        self.server = x_server
        return x_server