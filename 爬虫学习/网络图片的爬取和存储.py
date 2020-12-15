import requests
import os
url='http://img0.dili360.com//ga/M02/49/A2/wKgBy1nPEYaAVlPHAABPhIqUzPA708.jpg'
#pachong 后面一定加\\，不然就是存储在图片目录下
root='G:\\图片\\pachong\\'
path=root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r=requests.get(url)
        print(r.status_code)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功过')
    else:
        print('文件已保存')
except:
    print('爬取失败')