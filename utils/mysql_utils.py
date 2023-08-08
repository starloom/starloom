import mysql.connector.pooling
config = {
    "host": "13.212.220.175",
    "port": 3619,
    "user": "astro_read",
    "password": "astroGLxu8xk2uGV9x2kx9G2",
    "database": "astro_ai",
    "pool_name": "mypool",  # 连接池的名称
    "pool_size": 15  # 连接池中的连接数量
}
# config = {
#     "host": "localhost",
#     "port": 3306,
#     "user": "root",
#     "password": "",
#     "database": "astro_ai",
#     "pool_name": "mypool",  # 连接池的名称
#     "pool_size": 15  # 连接池中的连接数量
# }
connection_pool = mysql.connector.pooling.MySQLConnectionPool(**config)
