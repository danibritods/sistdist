'''assas'''
import redisrpc as redis
redis_server = redis.Redis()
message_queue = 'calc'
local_object = calc.Calculator()
server = redisrpc.Server(redis_server, message_queue, local_object)
server.run()
