import redis
class Redis:
    def __init__(self):
        pass 
    def connect(self, conn):

        global conn_Centralise      
        if (conn=='fin'):
            try:
                conn_Centralise = redis.Redis(host='localhost', port=6379, decode_responses=True)
                return conn_Centralise
            except Exception as error:
                print(error)
                exit()
