'''ToDo'''
import chat
import xmlrpc_wrapper as rpc

if __name__ == "__main__":
    chat_server = chat.Server()

    server_functions = {chat_server.get_msg: "get_msg",
                        chat_server.receive_msg: "receive_msg"}

    rpc_server = rpc.Server(server_functions)
