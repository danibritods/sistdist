'''aaa'''
#https://www.researchgate.net/publication/341271544_Remote_Method_Invocation_Using_Python
# import os
# import subprocess
import random
import datetime
import Pyro4

now=datetime.datetime.now()
print('date: '+now.strftime('%d-%m-%y')+' Time: '+now.strftime('%H:%M:%S'))
@Pyro4.expose

class Server(object):
    '''aaa'''
    def get_usid(self, name):
        '''aaa'''
        return f"Hello, {name}.\nYour Current User Session is {random.randint(0,1000)}:"
    def add(self, a, b):
        '''aaa'''
        return f"{a} + {b} = {a+b}"
    def subtract(self, a, b):
        '''aaa'''
        return f"{a} - {b} = {a-b}"
    def multiply(self, a, b):
        '''aaa'''
        return f"{a} * {b} = {a*b}"
    def division(self, a, b):
        '''aaa'''
        return f"{a} / {b} = {a/b}"
    def exp(self, a):
        '''aaa'''
        return f"{a} ** {a} = {a**a}"

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
url = daemon.register(Server)
ns.register("RMI.calculator", url)
print("The Server is now active., please request your calculations or start file transfer")
daemon.requestLoop()
