import logging
import socket
import threading
import time
IP =  "127.0.0.1" 
PORT = 1234
RECV_SIZE = 1024


class Socket:
    def _stablish_socket(self):
        logging.info("Stablishing socket!")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s
    
    def _client_socket(self):
        s_client = self._stablish_socket()
        s_client.connect((IP, PORT))
        logging.info("client stablished!")

        return s_client
    
    def _server_socket(self):
        s_server = self._stablish_socket()
        s_server.bind((IP, PORT))
        s_server.listen(5)
        logging.info("server stablished!")
        return s_server

    def _send_msg(self, message, remote_socket):
        remote_socket.send(bytes(message,"utf-8"))
        logging.info(f"{self} sent message: {message}")
    
    def _receive_msg(self, remote_socket):
        message = remote_socket.recv(RECV_SIZE).decode("utf-8")
        logging.info(f"{self} received message: {message}")
        return message

class Client(Socket):
    def __init__(self, id) -> None:
        self.id = id
        self.socket = self._client_socket()
        greeting = self._receive_msg(self.socket)
        print(greeting)


    def Send_msg(self,receiver_id, message_body):
        message_header = f"<{self.id}#{receiver_id}>"
        message = message_header + message_body
        request = f'Send_msg("{message}")'
        
        self._send_msg(request, self.socket)
    
    def Check_msg(self): #-> str:
        messages = self._server_fetch_msg()
        logging.info(f"The messages are: {messages}")
        return messages

    def _server_fetch_msg(self):
        request = f'Check_msg({self.id})'
        self._send_msg(request, self.socket)
        messages = []
        msg = "  "
        # while msg != "":
        msg = self._receive_msg(self.socket)
        messages.append(msg)

        return messages

class Server(Socket):
    def __init__(self) -> None:
        self.pending_msg = {}
        # self.clients = []
        # self.conection_ids = []
        # conversation = ()
        self.socket = self._server_socket()
        listening = threading.Thread(target=self._accept_conections)
        listening.start()

    def _accept_conections(self):
        while True:
            client_socket, address = self.socket.accept()
            print(f"Connection from {address} has been established!")
            self._send_msg("Welcome to the server!", client_socket)

            # msg = self._receive_msg(clientsocket)
            # self.clients.append(client_socket)
            handler_thread = threading.Thread(target=self._handle_connection, args=(client_socket,))
            handler_thread.start()

    def _handle_connection(self, client_sock):
        while True:
            try:
                message = self._receive_msg(client_sock)
                self._handle_msg(message, client_sock)
            except:
                logging.error("some error!")
                client_sock.close()
                break
    
    def _handle_msg(self, message, client_sock):
        # handle = {
        #     "Check_msg" : self._fetch_msg,
        #     "Send_msg" : self._receive_chat
        # }

        logging.info(f"message to handle: {message}")
        request, body = message[:-1].split("(")
        # handle[request](body)

        if "Check_msg" in request:
            # logging.error(f"ERROR in Check_msg. Request: {request}, body: {body}")
            receiver_id = body #body.split("#")[1].split(">")[0]
            self._fetch_msg(receiver_id, client_sock)
        
        elif "Send_msg" in request:
            self._receive_chat(body)

    def _fetch_msg(self,receiver_id, client_sock):
        chat_keys = list(filter(lambda chat_id: (chat_id.split("#")[1] == receiver_id)
                ,self.pending_msg.keys()))
        logging.info(f"chat_keys: {chat_keys}")

        chats = list(map(lambda chat_key :self._return_fetched_msg(chat_key)
             ,chat_keys))        
        logging.info(f"chats {receiver_id}: {chats}")
        
        # (list(map(lambda chat: self._send_msg(chat, client_sock)
        #         ,chats)))
        for chat in chats:
            logging.info(f"sending chat: {chat}")
            self._send_msg(chat,client_sock)

    def _return_fetched_msg(self, chat_key):
        chat = self.pending_msg[chat_key]
        self.pending_msg[chat_key] = []
        return f"<{chat_key}>\n{chat}"
            
    def _receive_chat(self, message):
        split_message = message.split(">")
        chat_id = split_message[0].split("<")[1]
        message_body = split_message[1]
        
        self.pending_msg.setdefault(chat_id, []).append(message_body)
        logging.info(f"pending msg: {self.pending_msg}")

    def Receive_msg(self, sender_ID, receiver_ID):
        pass

    def Fetch_msg(self,receiver_ID):
        pass

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.ERROR,
                        datefmt="%H:%M:%S")
    s = Server()
    c1 = Client("1")
    c2 = Client("2")
    c1.Send_msg("2","hello c2")
    c2.Send_msg("1","hello c1!")
    time.sleep(2)
    print(10 * "--")
    print(c1.Check_msg())
    print("22")
    print(c2.Check_msg())
    print(10 * "--")

    # while True:
    #     new_message = input("Write message C1: ")
    #     c1.Send_msg("2", new_message)
    #     new_message = input("Write message C2: ")
    #     c2.Send_msg("1", new_message)

    #     print(10 * "--")
    #     c1.Check_msg()
    #     print()
    #     c2.Check_msg()

"""
TODO
- [ ] Add broadcast option so that everyone in the same room can receive the messages
- [ ] Make the basic chat work. It seems that like the receive message creates a inifinite loop, maybe just assint it to a thread

"""