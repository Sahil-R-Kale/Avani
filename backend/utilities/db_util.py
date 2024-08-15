import pymysql

def get_db_connection():
    timeout = 10
    connection = pymysql.connect(
        charset="utf8mb4",
        connect_timeout=timeout,
        cursorclass=pymysql.cursors.DictCursor,
        db="",
        host="",
        password="",
        read_timeout=timeout,
        port=27329,
        user="",
        write_timeout=timeout,
    )
    return connection