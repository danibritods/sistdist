class Client:
    def __init__(self, id) -> None:
        self.id = id
    
    def Check_msg(self): #-> str:
        pass

    def Send_msg(self,remote_id, message):
        pass

class Server:
    def __init__(self) -> None:
        self.pending_msg = {}

    def Receive_msg(self, sender_ID, receiver_ID):
        pass

    def Fetch_msg(self,receiver_ID):
        pass
