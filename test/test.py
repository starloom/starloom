import redis
connection_pool = redis.ConnectionPool(host='localhost', port=9062, password='astroAIC27VNu2GO4Gixx0nG', db=0)
redis_client = redis.StrictRedis(connection_pool=connection_pool)
connection_pool2 = redis.ConnectionPool(host='localhost', port=9061, password='astroAIC27VNu2GO4Gixx0nG', db=0)
redis_client2 = redis.StrictRedis(connection_pool=connection_pool2)
def get_smxs_xing_luo_xz_redis ():
    _keys = redis_client.keys('XING_ZUO_SHANG_SHENG*')
    print(len(_keys))
    for _key in _keys:
        _key2 = _key.decode('UTF-8')
        _data = redis_client2.get(_key2)
        if _data:
            print()
        else:
            _local_data = redis_client.get(_key2).decode('UTF-8')
            redis_client2.set(_key2, _local_data)
get_smxs_xing_luo_xz_redis()