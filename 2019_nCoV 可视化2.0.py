# # %%
#
# import time, json, requests
# from datetime import datetime
# import matplotlib
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
# from matplotlib.font_manager import FontProperties
# from mpl_toolkits.basemap import Basemap
# from matplotlib.patches import Polygon
# import numpy as np
#
# from pyquery import PyQuery as pq
# from bs4 import BeautifulSoup
# import datetime
# import re
#
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
#
# # %%
#
# # 获取福建省疾病预防控制中心官网疫情通告列表
# session = requests.session()
# crawl_timestamp = int(datetime.datetime.timestamp(datetime.datetime.now()) * 1000)
# keyword = {'txtkeyword': '福建省新增新型冠状病毒感染的肺炎疫情情况'}
# html = ''
# while True:
#     try:
#         rsp = session.get('http://www.fjcdc.com.cn/search', params=keyword)
#     except requests.exceptions.ChunkedEncodingError:
#         continue
#
#     rsp.raise_for_status()  # 非200则抛出异常（rsp.status_code != 200）
#     html = rsp.content
#     # soup = BeautifulSoup(rsp.content, 'lxml')
#     # print(soup)
#     break
#
# # %%
#
# # 获取最新一期的疫情通告链接地址
# doc = pq(html)
# # 方法一：第一条数据，doc('.list li a').attr.href即可得到所要链接
# # 方法二：指定日期, doc('.list li:contains("2020-02-02") a').attr.href
# # 但是这里咱们多写点，练习嘛,乱写
# news = doc('.list li').items()
# dates = []
# for item in news:
#     date_str = item('span').text().strip()
#     date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
#     dates.append(date)
#
# temp = np.array(dates)
# latest_date = temp.max()
# latest_date_str = latest_date.strftime('%Y-%m-%d')
# latest_date_url = doc('.list li:contains("{0}") a'.format(latest_date_str)).attr.href
# latest_date_url = 'http://www.fjcdc.com.cn' + latest_date_url
# print(latest_date_url)
#
# # %%
#
# # 解析网页，获取确诊和疑似病例数据文本
# # 福州市47例（仓山区2例、晋安区6例、长乐区4例、闽侯县2例、连江县8例、罗源县1例、闽清县5例、永泰县2例、福清市14例、宁德市古田县1例、湖北省武汉市2例）；
# # 上面最后两条数据啥意思？
# soup = ''
# while True:
#     try:
#         rsp = session.get(latest_date_url)
#     except requests.exceptions.ChunkedEncodingError:
#         continue
#
#     rsp.raise_for_status()  # 非200则抛出异常（rsp.status_code != 200）
#
#     soup = BeautifulSoup(rsp.content, 'lxml')
#     # print(soup)
#     break
#
# reg = re.compile('.*福州市.*')
# soup = soup.find('div', class_='showCon')
# tag = soup.find_all(text=reg)
# if len(tag) != 4:
#     raise Exception('查找到值的次数必须等于 4. 实际值为: {}'.format(len(tag)))
#
# area_data = {}
# # area_data.update({'confirm_added':tag[0]})
# # area_data.update({'suspend_added':tag[1]})
# area_data.update({'confirm': tag[2]})
# area_data.update({'suspend': tag[3]})
# print(area_data)
#
# # %%
#
# # 解析各区县数据
# import re
#
# pattern = re.compile('(?<=、|（)\D+[市|县|区]\d+例')
# town_list = pattern.findall(area_data['confirm'])
# # town_list = area_data['confirm'].split('（|(')[1].split('）)')[0].split('、')
#
# town_data = {'福州市区': 0}
# for town in town_list:
#     match_num = re.search(r'\d+(?=例)', town)
#     match_town_name = re.search(r'\D+[市|县|区]', town)
#     if match_num and town:
#         match_num = int(match_num.group())
#         match_town_name = match_town_name.group()
#     else:
#         continue
#
#     if match_town_name == '长乐区':  # 地图中长乐为市
#         match_town_name = '长乐市'
#
#     town_data.update({match_town_name: match_num})
#
#     # 晋安、鼓楼、、马尾、仓山
#     if match_town_name[-1] == '区':  # 地图数据没有各个区的数据
#         town_data['福州市区'] += match_num
#
# print(town_data)
#
#
# # %%
#
# # 用Basemap画疫情图（这是从gadm下载地形数据，行政区域不准确）
#
# def get_color(town_data, town_name_zh):
#     color = '#7FFFAA'
#     if town_data[town_name_zh] == 0:
#         color = '#f0f0f0'
#     elif town_data[town_name_zh] <= 5:
#         color = '#ffaa85'
#     elif town_data[town_name_zh] <= 10:
#         color = '#ff7b69'
#     elif town_data[town_name_zh] <= 20:
#         color = '#bf2121'
#     else:
#         pass
#     return color
#
#
# # 绘制福建省福州市确诊分布图
# def plot_fz_dis_by_basemap():
#     # area_cfm_data = catch_fj_area_distribution()
#
#     # 标签颜色和文本
#     legend_handles = [
#         matplotlib.patches.Patch(color='#7FFFAA', alpha=1, linewidth=0),
#         matplotlib.patches.Patch(color='#ffaa85', alpha=1, linewidth=0),
#         matplotlib.patches.Patch(color='#ff7b69', alpha=1, linewidth=0),
#         matplotlib.patches.Patch(color='#bf2121', alpha=1, linewidth=0),
#         matplotlib.patches.Patch(color='#7f1818', alpha=1, linewidth=0)
#     ]
#     legend_labels = ['0人', '1-5人', '5-10人', '10-20人', '>20人']
#
#     fig = plt.figure(facecolor='#f4f4f4', figsize=(10, 8))
#     axes = fig.add_axes((0.1, 0.1, 0.8, 0.8))
#     axes.set_title('福州市新型冠状病毒疫情地图(不含平潭)', fontsize=14)
#     axes.legend(legend_handles, legend_labels, bbox_to_anchor=(0.5, -0.11), loc='lower center', ncol=5)
#
#     # 横轴墨卡托投影
#     china_map = Basemap(llcrnrlon=118.3, llcrnrlat=25.2, urcrnrlon=120.1, urcrnrlat=26.8,
#                         resolution='i', projection='tmerc',
#                         lat_0=26, lon_0=119,
#                         ax=axes)
#     # gadm36_CHN_1 省一级；gadm36_CHN_2 市一级；gadm36_CHN_3 县一级
#     '''
#     {'GID_0': 'CHN', 'NAME_0': 'China', 'GID_1': 'CHN.1_1', 'NAME_1': 'Anhui',
#     'NL_NAME_1': '安徽|安徽', 'GID_2': 'CHN.1.1_1',
#     'NAME_2': 'Anqing', 'NL_NAME_2': '安庆市', 'GID_3':
#      'CHN.1.1.1_1', 'NAME_3': 'Anqing', 'VARNAME_3': '',
#      'NL_NAME_3': '', 'TYPE_3': 'Xiànjíshì', 'ENGTYPE_3':
#      'County City', 'CC_3': '', 'HASC_3': '', 'RINGNUM': 1, 'SHAPENUM': 1}
#     '''
#     china_map.readshapefile('res/gadm36_CHN_shp/gadm36_CHN_3', 'states', drawbounds=True)
#     china_map.drawmapboundary(fill_color='aqua')
#     china_map.fillcontinents(color='white', lake_color='aqua')
#     china_map.drawcoastlines()
#
#     for info, shape in zip(china_map.states_info, china_map.states):
#         prov_name = info['NAME_1'].strip()
#         city_name = info['NAME_2'].strip()
#
#         if prov_name != 'Fujian' or city_name != 'Fuzhou':
#             continue
#
#         color = '#7FFFAA'
#         town_name_zh = info['NL_NAME_3'].strip()
#         town_name_py = info['NAME_3'].strip()
#         if town_name_zh in town_data.keys():
#             color = get_color(town_data, town_name_zh)
#         elif town_name_py == 'Fuzhou':  # 福州市区NAME_3_NL为空值
#             color = get_color(town_data, '福州市区')
#
#         # print(prov_name, city_name, town_name_zh, town_name_py)
#         poly = Polygon(shape, facecolor=color, edgecolor=color, linewidth=1)
#         axes.add_patch(poly)
#
#         # 绘制各区县的确诊数
#     # 将经纬度转换为笛卡尔坐标
#     town_loc_list = {'福州市区': china_map(119.3, 26.08),
#                      # '鼓楼区': china_map(119.3, 26.08),
#                      # '台江区': china_map(119.3, 26.07),
#                      # '仓山区': china_map(119.32, 26.05),
#                      # '马尾区': china_map(119.45, 26.0),
#                      # '晋安区': china_map(119.32, 26.08),
#                      '闽侯县': china_map(119.13 - 0.2, 26.15),
#                      '连江县': china_map(119.53 - 0.1, 26.20 + 0.02),
#                      '罗源县': china_map(119.55 - 0.2, 26.48),
#                      '闽清县': china_map(118.85 - 0.2, 26.22),
#                      '永泰县': china_map(118.93 - 0.2, 25.87),
#                      '福清市': china_map(119.38 - 0.2, 25.72),
#                      '长乐市': china_map(119.52, 25.97)}
#
#     for key in town_loc_list.keys():
#         plt.text(town_loc_list[key][0], town_loc_list[key][1],
#                  '{0}\n确诊{1}例'.format(key, town_data[key]), fontsize=12, fontweight='bold',
#                  ha='left', va='center', color='black')
#
#     plt.annotate('地图数据有错\n平潭不属福州|福清\n无数据不应着色', xy=china_map(119.78, 25.52),
#                  xycoords='data', arrowprops=dict(arrowstyle='->', color='black'),
#                  xytext=china_map(119.68, 25.80),  # 平潭经纬度
#                  fontsize=12, fontweight='bold',
#                  ha='left', va='center', color='black')
#
#
# plot_fz_dis_by_basemap()
#

# str1='pythonhello'
# print('.'.join(str1))
# str2='my heart will go on'
# s=str2.split()
# print(type(s))
# print(s)
# print(':'.join(s))
#
# # 分切成两次，就是三个数，如果最后一个是多个单词的，就是一堆在一起
# s3=str2.split(' ',2)
# print(s3)

# reverse是列表的一个方法，只能是列表又，其他数据结构如果要反转，要使用revered,而不能使用reverse()
# reversed 是一个类返回的是一个迭代器
# mystring='my heart will go on'
# print(' '.join(reversed(mystring.split())))

# print('{:*<10}'.format('python'))

# total=56
# print('total is {:*<6d}'.format(total))
# PI=3.14159
# print('{:.2f}'.format(PI))
# x=3
# print(eval("x+2"))

# s='haPPy BirThDay to U'
# print(s.replace('U','you').strip().lower())

# list=[512,'p',(3,9),[3,9],'PY']
# print(list[3])

# list3=[1,2,3,4,5,6,7,8,9]
# print(list3[3:7])
# print(list3[2:-2:2])
# print(list3[:])

# tuple3 = ('p','y','t','h','o','n')
# print(tuple3[1:5:3])
# print(tuple3[4:2:-1])
# list4 = [1,6,2,3,4,2,5,6,6]
# print(list4.index(6))
# print(list4.count(9))

# tuple3 = (1,2,2,4,2,5,6)
# print(max(tuple3))
# print(min(tuple3))
# print(len(tuple3))

# list5 = [1,3,5,7]
# list6 = [2,4,6]
# print(list5+list6
#
# )


# d = {'apple':'red','banana':'yellow'}
# l = list(d)
# print(l)


# list1 = []
# list1 = list(range(1,10,2))
# print(list1)


# list1 = [1,2,3]
# list1.append([4,5])
# print(list1)
# list1.extend([4,5])
# list1.insert(1,9)
# print(list1)
# print(list1.pop(0))
# print(list1)

# list1=[1,2,3,[7,8,9]]
# list2=list1.copy()
# list3=copy.deepcopy(list1)
# list2[1]=5
# print(list2)
# print(list1)
# list2=list1[:]
# print(list2)
# list2[3][0]=5
# list2[1]=6
# list3[3][0]=5
# list3[1]=6
# print(list1)
# print(list2)
# print(list3)

# 两个参数的时候就是从开始到结束
# 三个参数的时候就是从开始到结束，以什么的步长
# pstr=input()
# p=pstr[:-1]
# if pstr==pstr[len(pstr)::-1]:
#     print('true')
# else:
#     print('fa')
#
# print(p)
import  copy
# list1=[3,5,[7,9,11],'HelloGuet']
# list2=copy.deepcopy(list1)
# list2[2][1]=1
# list2[3]='helloguet'
# print(list1)

# lista=[123,'hello',["python","java"]]
# listb=copy.deepcopy(lista)
# listb.append([4,5,6])
# lista[2][0]='golang'
# lista[1]='world'
# print(lista)
# print(listb)

# list1=[1,2,3,[7,8,9]]
# list2=list1[:]
# list2[3][0]=5
# list2[1]=6
# print(list1)
# print(list2)
# print(id(list1[1]))
# print(id(list2[1]))
# print(id(list1[3][0]))
# print(id(list2[3][0]))

# mystring='my heart will go on'
# num=len(mystring.split(" "))
# print(num)
# stringlist=list(mystring.split(" "))
# print(stringlist)

# alist=list(range(0,9,2))
# print(alist)
# blist=list(range(1,10,2))
# print(blist)
# alist.extend(blist)
# print(alist)
# alist.sort()
# print(alist)
# alist.reverse()
# print(alist)
# print(alist.count(4))
# print(alist.index(6))
# alist.insert(2,100)
# alist.remove(100)
# print(alist)
# del alist[4]
# print(alist)

# d=dict([('spring',1),('summer',2),('winter',4)])
# l=sorted(list(d),reverse=True)
# print(l)

# dict3={}

# from time import time
# data=[None for k in range(1,110000)]
# def average_time(n):
#     start=time()
#     for k in range(n):
#         data.remove(None)
#         remove比pop高效
    # end=time()
    #
    # return (end-start)/n
#
# k=average_time(100000)
# print(k)

# basket=['orange','apple','pear','banana']
# color=['red','yellow','bule']
# for i,v in enumerate(basket):
#     print(i,v)

# for i,v in enumerate(basket,3):
#     print(i,v)

# list(enumerate(color,1))
# print(list)


# import random
#
# 产生0-100的随机数
# a=[]
# for i in range(0,100):
#     a.append(random.randint(0,100))
#
# print(a)

# 用字典类统计
# re={}
#
# for num in a:
#     if num in re.keys():
#         re[num]+=1
#     else:
#         re[num]=1
#
# print(re)
# 寻找最多次数的数字
# num_max=max(re.values())
# print(num_max)
# for item in re.items():
#     if item[1]==num_max:
#         print('shuziwei: %s cishuwei: %s'%(item[0],item[1]))


# alist=[(3,'B',9),(5,'A',6),(2,'C',4)]
# alist.sort(key=lambda e:e[1])
# print(alist)

# str='abcdaefagha'
# str.replace('a','b')
# print('abc'.len())

# print("{:.2f}".format(20-23+10/32*5))


# print(list(map(lambda x:len(x),['aaa','bb','c'])))

# book=['python','english','math']
# book.remove('python')
# book.pop(0)
# del book[0]
# book.clear()
# print(book)


# print('love'.join(["Everyday","Yourself","Python"]))

# import copy
# da=[1,2,3,[4,5,6]]
# print(da)
# fa=copy.deepcopy(da)
# fa[3][0]=5
# print(da)

# question=['name','sex','favorite color']
# answers=['zrx','female','bule']
# zipped=zip(question,answers)
# for q,a in zip(question,answers):
#     print(q,a)

# dict3={'广东':"广州","河南":"郑州","广西":"南宁","河北":"石家庄"}
# for k,v in dict3.items():
#     print(k,v)
#
# for item in dict3.items():
#
#     for key in dict3:
#         print(key,dict3[key])


# import string
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
#



# def fun(x):
#     return pow(x,2)
#
# L=map(fun,[1,2,3,4,5])
# print(list(L))
#
# print(next(L))

# fp=open(dizhi,'打开的方式')
# ch=fp.read()全部读完
# alist=[]


# import multiprocessing
# import os,time
#
# def fun(num):
#     mysum=0
#     for i in range(num):
#         mysum+=1
#
#     return mysum
# if __name__=="__main__":
#     with multiprocessing.Pool(4) as pool:
#         results=pool.map(fun,(3,6,9))
#         for item in results:
#             print(item)


# import threading
import time

# def func(x,y):
#     for i in range(x,y):
#         print(i)
#
# t1=threading.Thread(target=func,name='thread1',args=(1,10))
# t1.start()
# t1.join()
# t2=threading.Thread(target=func,name="thread2",args=(10,16))
# t2.start()
#
# t2.join()
# print(t1.name,'is',t1.is_alive())
# print(t2.name,'is',t2.is_alive())


# from multiprocessing import Process
# from time import sleep
# counter=0
#
# def sub_task(string):
#     global counter
#     while counter<10:
#         print(string,end='',flush=True)
#         counter+=1
#         sleep(0.01)
#
# def main():
#     Process(target=sub_task,args=('PIng', )).start()
#     Process(target=sub_task,args=('pong', )).start()
#
# if __name__=='__main__':
#     main()

# import threading,time
# class Producer(threading.Thread):
#     def __init__(self,threadname):
#         threading.Thread.__init__(self,name=threadname)
#
#     def run(self):
#         global count
#         while True:
#             if con.acquire():
#                 if count>100:
#                     con.wait()
#
#                 else:
#                     count=count+50
#                     print(self.name+" produce 50,count="+str(count))
#                     con.notify()
#
#                 con.release()
#
# class Consumer(threading.Thread):
#     def __init__(self,threadname):
#         threading.Thread.__init__(self,name=threadname)
#
#     def run(self):
#         global count
#         while True:
#
#             if con.acquire():
#                 if count<100:
#                     con.wait()
#                 else:
#                     count-=25
#                     print(self.name+"cousume 25,count="+str(count))
#                     con.notify()
#                 con.release()
#                 time.sleep(1)
# count=200
# con=threading.Condition()
#
# if __name__=="__main__":
#     for i in range(2):
#         p=Producer('Producer')
#         p.start()
#
#     for i in range(2):
#         c=Consumer('consumer')
#         c.start()
#

#
# import threading,time
# from concurrent.futures import ThreadPoolExecutor
#
# local_data=threading.local()
# def fun(n):
#     for i in range(n):
#         try:
#             local_data.num+=i
#         except:
#             local_data.num=i
#
#         print('\n%s local_data is: %s'%(threading.current_thread().name,local_data.num))
#
#     pool=ThreadPoolExecutor(max_worker=2)
#     task1=pool.submit(fun,5)
#     task2=pool.submit(fun,10)
#     time.sleep(3)
#     print('task1:',task1.done())
#     print('task2:',task2.done())
#     pool.shutdown()

# import threading
from time import sleep
# counter=0
#
# def subtask(string):
#     global counter
#     while counter<5:
#         print(string,end='',flush=True)
#         counter+=1
#         sleep(0.01)





# if __name__=='__main__':
#     p1=threading.Thread(target=subtask,args=('Ping',))
#     p2=threading.Thread(target=subtask,args=('Pong',))
#     p1.start()
#     p2.start()
#
#     p1.join()
#     p2.join()


