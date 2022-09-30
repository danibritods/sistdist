'''RedirRPC Client'''
import redisrpc
import redis

''' How it works:
Each library implementation uses the same client and server example based off of a mutable calculator object. The clients and servers from different languages are interoperable.

1. The client issues an RPC Request by using the Redis RPUSH command to push an RPC Request message into a Redis list called calc.
2. The server retrieves the RPC Request message by using the Redis BLPOP command.
3. The server dispatches the RPC Request to a local object, which in this case is a Calculator object.
4. The server accepts the return value (or exception) from the Calculator object.
5. The server issues an RPC Response by using the Redis RPUSH command to push an RPC Response message into a Redis list called calc:rpc:<RAND_STRING>, which was chosen by the client.
6. The client retrieves the RPC Response message by using the Redis BLPOP command.
'''

redis_server = redis.Redis()
message_queue = 'calc'
calculator = redisrpc.Client(redis_server, message_queue)
calculator.clr()
calculator.add(5)
calculator.sub(3)
calculator.mul(4)
calculator.div(2)
assert calculator.val() == 4
