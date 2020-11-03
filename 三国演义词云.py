# import jieba
# import wordcloud
# import numpy as np
# from PIL import Image
# mask = np.array(Image.open('OIP1.png'))
# fb = open("2020政府工作报告.txt", "r", encoding="gbk")
# t = fb.read()
# fb.close()
# ls = jieba.lcut(t)
# txt = " ".join(ls)
# w = wordcloud.WordCloud(font_path = "msyhbd.ttc",
#  mask = mask,
#  collocations = False,
#  width = 1000,
#  height = 700,
#  background_color = "white")
# w.generate(txt)
# w.to_file("heart.jpg")

alist=[(3,'B',9),(5,'A',6),(2,'C',4)]
alist.sort(key=lambda e:e[1])
print(alist)