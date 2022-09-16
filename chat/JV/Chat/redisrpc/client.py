redis_server = redis.Redis()
message_queue = 'calc'
calculator = redisrpc.Client(redis_server, message_queue)
calculator.clr()
calculator.add(5)
calculator.sub(3)
calculator.mul(4)
calcaultor.div(2)
assert calculator.val() == 4