'''Chat using sockets'''
import logging
import socket
import threading
IP = "127.0.0.1"
PORT = 1234
RECV_SIZE = 1024


class Socket:
    '''ToDo'''

    def _stablish_socket(self):
        '''ToDo'''
        logging.info("Stablishing socket!")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s

    def _client_socket(self):
        '''ToDo'''
        s_client = self._stablish_socket()
        s_client.connect((IP, PORT))
        logging.info("client stablished!")
        return s_client

    def _server_socket(self):
        '''ToDo'''
        s_server = self._stablish_socket()
        s_server.bind((IP, PORT))
        s_server.listen(5)
        logging.info("server stablished!")
        return s_server

    def _send_msg(self, message, remote_socket):
        '''ToDo'''
        remote_socket.send(bytes(message, "utf-8"))
        logging.info(f"{self} sent message: {message}")

    def _receive_msg(self, remote_socket):
        '''ToDo'''
        message = remote_socket.recv(RECV_SIZE).decode("utf-8")
        logging.info(f"{self} received message: {message}")
        return message


class Client(Socket):
    '''ToDo'''

    def __init__(self, id) -> None:
        self.id = id
        self.socket = self._client_socket()

    def Send_msg(self, remote_id, message_body):
        '''ToDo'''
        message_header = f"<{self.id}#{remote_id}>"
        message = message_header + message_body

        self._send_msg(message, self.socket)

    def Check_msg(self):  # -> str:
        '''ToDo'''
        messages = self._server_fetch_msg(self.id)
        logging.info(messages)


class Server(Socket):
    '''ToDo'''

    def __init__(self) -> None:
        self.pending_msg = {}
        self.conections = []
        self.conection_ids = []
        conversation = ()
        self.socket = self._server_socket()
        listening = threading.Thread(target=self._accept_conections)
        listening.start()

    def _accept_conections(self):
        '''ToDo'''
        while True:
            client_socket, address = self.socket.accept()
            print(f"Connection from {address} has been established!")
            self._send_msg("Welcome to the server!", client_socket)

            # msg = self._receive_msg(clientsocket)
            self.conections.append(client_socket)
            handler_thread = threading.Thread(
                target=self._handle_connection, args=(client_socket,))
            handler_thread.start()

    def _handle_connection(self, client_sock):
        '''ToDo'''
        while True:
            try:
                message = self._receive_msg(client_sock)
                message_split = message.split(">")
                chat_id = message_split.split("<")[1]
                message_body = message_split[1]

                self.pending_msg.setdefault(chat_id, []).append(message_body)
            except:
                logging.info("some error!")
                client_sock.close()
                break


if __name__ == "__main__":
    formatting = "%(asctime)s: %(message)s"
    logging.basicConfig(format=formatting, level=logging.INFO,
                        datefmt="%H:%M:%S")
    s = Server()
    c1 = Client("1")
    c2 = Client("2")
    c1.Send_msg("2", "hello c2")
    c2.Send_msg("1", "hello c1!")
    while True:
        new_message = input("Write message C1: ")
        c1.Send_msg("2", new_message)
        new_message = input("Write message C2: ")
        c2.Send_msg("1", new_message)

    def Receive_msg(self, sender_ID, receiver_ID):
        pass

    def Fetch_msg(self, receiver_ID):
        pass
