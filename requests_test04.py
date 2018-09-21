import requests
import json

response=requests.get("http://httpbin.org/get")
print(type(response.text))
print(response.json())
print(json.loads(response.text))
print(type(response.json()))
#在上面提到了response.content，这样获取的数据是二进制数据，同样的这个方法也可以用于下载图片以及
#视频资源
