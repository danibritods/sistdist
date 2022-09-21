import logging
import threading
import time
import socket 

IP =  "127.0.0.1" #socket.gethostname()
PORT = 1234


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

def server(name):
    logging.info("Thread %s: starting server", name)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind((IP, PORT))
    s.listen(5)

    while True:
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established!")
        clientsocket.send(bytes("Welcome to the server!","utf-8"))
        clientsocket.close()

def client(name):
    logging.info("Thread %s: starting client", name)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP,PORT))

    msg = s.recv(1024)
    print(msg.decode("utf-8"))

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    s = threading.Thread(target=server, args=(2,))
    c = threading.Thread(target=client, args=(3,))
    logging.info("Main    : before running thread")
    x.start()
    s.start()
    c1.start()
    c2.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")