import json
import redis
redis = redis.Redis(host='127.0.0.1', port=6379)
content=redis.get("findList").decode("utf-8")
print(content)
data=json.loads(content)
print(data)