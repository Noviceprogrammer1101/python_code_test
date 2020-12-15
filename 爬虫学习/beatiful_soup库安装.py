from bs4 import BeautifulSoup
import requests
r=requests.get('https://python123.io/ws/demo.html')
#print(r.text)
demo=r.text
# 在这里我把html.parser打成了html,parser，所以这里第一次我打错了
# BeautifulSoup(数据，解析器)，这是函数的定义
soup=BeautifulSoup(demo,'html.parser')
print(soup.title)

# 这是一个标签
tag = soup.a
print(tag)

# 标签名字
print(soup.a.parent.name)
print(soup.a.parent.parent.name)

# //标签的属性
print(tag.attrs)