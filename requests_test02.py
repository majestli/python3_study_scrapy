import requests

#requests.post("http://httpbin.org/post")
#requests.put("http://httpbin.org/post")
#requests.delete("http://httpbin.org/post")
#requests.head("http://httpbin.org/post")
#requests.options("http://httpbin.org/post")

response=requests.get('http://www.baidu.com')
response.encoding="utf-8"
print(response.text)
print(response.content.decode('utf-8'))
