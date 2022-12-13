'''ToDo'''


class Server:
    '''ToDo'''

    def __init__(self) -> None:
        self.pending_messages = {}

    def get_msg(self, remote_id):
        '''ToDo'''
        chats = {chat_id.split("#")[0]: messages
                 for chat_id, messages in self.pending_messages.items()
                 if f"#{remote_id}" in chat_id}
        return chats

    def receive_msg(self, sender_id, receiver_id, msg):
        '''ToDo'''
        chat_id = f"{sender_id}#{receiver_id}"
        self.pending_messages.setdefault(chat_id, []).append(msg)


class Client:
    '''ToDo'''

    def __init__(self, client_id, server) -> None:
        self.id = client_id
        self.server = server

    def send_msg(self, remote_id, msg):
        '''ToDo'''
        self.server.receive_msg(self.id, remote_id, msg)

    def check_msg(self):
        '''ToDo'''
        return self.server.get_msg(self.id)


if __name__ == "__main__":
    s = Server()
    daniel = Client("Daniel", s)
    joao = Client("Joao", s)
    doris = Client("Doris", s)

    daniel.send_msg("Doris", "Oi")
    daniel.send_msg("Doris", "tudo bem?")
    joao.send_msg("Daniel", "Te pago amanhã")
    doris.check_msg()
