import  requests

headers={

    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"

}

response=requests.get("https://www.zhihu.com",headers=headers)
print(response.text)
