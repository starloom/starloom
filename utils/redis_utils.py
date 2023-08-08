import redis
# 13.212.220.175
connection_pool = redis.ConnectionPool(host='13.212.220.175', port=9061, password='astroAIC27VNu2GO4Gixx0nG', db=0)
# connection_pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
redis_client = redis.StrictRedis(connection_pool=connection_pool)