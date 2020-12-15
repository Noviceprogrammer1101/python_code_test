from bs4 import BeautifulSoup
# //这里竟然编码报错
soup = BeautifulSoup(open('scenery.html'),'lxml')
# print(soup.prettify())

#只会获取第一次出现的ul
# Tag1=soup.ul
# print(Tag1)

# 说好的把ul全部找出来的
# soup.ul
print(soup.find_all('ul'))