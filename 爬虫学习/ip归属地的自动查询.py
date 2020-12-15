import requests
kv={"user-agent":"Mozilla/5.0"}
url='http://m.ip138.com/ip.asp?ip='

#在这里，如果不加上header的话，马上不给你通过
r=requests.get(url+'180.101.49.42',headers=kv)
#print(r.status_code)
#print(r.text[0:1000])
print(r.request.url)