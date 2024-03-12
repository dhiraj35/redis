from redisClass  import *

redisCon = Redis()
redisCursor = redisCon.connect('fin')
allData = redisCursor.hgetall('user-session:123')
print(allData['name'])

