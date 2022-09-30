import chat
import xmlrpc_wapper as rpc

def test_routine():
    rpc = rpc.Client()
    daniel = chat.Client("Daniel",rpc.connection)
    joao = chat.Client("Joao",rpc.connection)
    doris = chat.Client("Doris",rpc.connection)

    daniel.send_msg("Doris","Oi")
    daniel.send_msg("Doris","tudo bem?")
    joao.send_msg("Daniel","Te pago amanhã")
    print(doris.check_msg())

def client_interface():
    rpc_client = rpc.Client()
    client_id = input("Write your client ID: ")
    client = chat.Client(client_id, rpc_client.connection)
    message = ""

    while message != "q!":
        receiver_id = input("receiver_id: ")
        message = input("message: ")

        client.send_msg(receiver_id, message)

        print(f"{10*'-·-'} \n {client.check_msg()} \n {15*'-·'}")

if __name__ == "__main__":
    client_interface() 



