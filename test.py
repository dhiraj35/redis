from redisClass  import *

redisCon = Redis()
redisCursor = redisCon.connect('fin')
# r.hset('user-session:123', mapping={
#     'name': 'John',
#     "surname": 'Smith',
#     "company": 'Redis',
#     "age": 29
# })
allData = redisCursor.hgetall('user-session:123')
print(allData['name'])

