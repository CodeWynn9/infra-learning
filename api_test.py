import httpx

response = httpx.get("https://api.github.com")

print("状态码：", response.status_code)
print("数据类型：", type(response.json()))
print("数据：", response.json())
print("原始内容：", response.text)
