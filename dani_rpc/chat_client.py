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


if __name__ == "__main__":
    test_routine() 



