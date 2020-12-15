# .contents 子节点的列表，将tag的所有儿子节点存入列表
# .children 子节点的迭代类型
# 。descendants 子孙的迭代类型

import lxml
from bs4 import BeautifulSoup
import requests
kv={"user-agent":"Mozilla/5.0"}
r=requests.get('https://python123.io/ws/demo.html',headers=kv)
#print(r.text)
demo=r.text
soup=BeautifulSoup(demo,'html.parser')
# print(soup.head)
#
# print(soup.head.contents)
#
# for child in soup.body.children:
#     print(child)

print(soup.prettify())