'''string'''
import redisrpc

class ChatClient ():
    '''aaa'''
    def func1(self):
        '''aaa'''
    def func2(self):
        '''aaa'''


def main():
    '''string'''
    # instanced_object = New
    # redis_server = redis.Redis()
    redis_server = redisrpc.redis()
    message_queue = 'calc'
    calculator = redisrpc.Client(redis_server, message_queue)
    calculator.clr()
    calculator.add(5)
    calculator.sub(3)
    calculator.mul(4)
    calculator.div(2)
    assert calculator.val() == 4

main()