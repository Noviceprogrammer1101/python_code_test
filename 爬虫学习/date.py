import requests as rq
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.options import InitOpts
from pandas import DataFrame
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
url = 'https://c.m.163.com/ug/api/wuhan/app/data/list-total'

def open(url):

    '''打开网页返回网页文件'''
    resp = rq.get(url, headers=headers)
    return resp.json()['data']


def get_content(html):

    '''分析网页，获取需要的数据并保存返回'''
    data = []
    confirm = []
    suspect = []
    total_confirm =[]
    total_heal = []
    total_dead = []
    total_input = []

    #以下是获取中国近一个月确诊以及疑似人数数据
    for each in html['chinaDayList'][-30:]:
        data.append(each['date'])
        confirm.append(each['today']['confirm'])
        suspect.append(each['today']['suspect'])

    #以下是获取全国疫情数据
    total_confirm.append(html['chinaTotal']['total']['confirm'])
    total_heal.append(html['chinaTotal']['total']['heal'])
    total_dead.append(html['chinaTotal']['total']['dead'])
    total_input.append(html['chinaTotal']['total']['input'])
    result =[]

    # 以下是获取全国各省确诊数据
    for area in html['areaTree'][2]['children']:
        result.append((area['name'], area['total']['confirm']))

    # 以下是获取全国各省详细的实时及总计疫情数据
    china_now = {'省份':[], '确诊':[], '治愈':[], '死亡':[]}
    china_total = {'省份':[], '确诊':[], '治愈':[], '死亡':[]}

    for date in html['areaTree'][2]['children']:
        china_now['省份'].append(date['name'])
        china_now['确诊'].append(date['today']['confirm'])
        china_now['治愈'].append(date['today']['heal'])
        china_now['死亡'].append(date['today']['dead'])
        china_total['省份'].append(date['name'])
        china_total['确诊'].append(date['total']['confirm'])
        china_total['治愈'].append(date['total']['heal'])
        china_total['死亡'].append(date['total']['dead'])

    #以下是获取全球确诊数据
    world = {}
    for num in html['areaTree']:
        world[num['name']] = num['total']['confirm']
    world = sorted(world.items(),key=lambda k:k[1], reverse=True)[:10]

    return [data, confirm, suspect], [total_confirm, total_heal, total_dead, total_input],\
           result, [china_now, china_total], world

def get_line(line):

    '''绘制线形图'''
    data = line[0]
    confirm = line[1]
    suspect = line[2]
    chinaline = Line()
    chinaline.add_xaxis(data)
    chinaline.add_yaxis('确诊人数', confirm)
    chinaline.add_yaxis('疑似人数', suspect)
    chinaline.set_global_opts(title_opts=opts.TitleOpts(title="近一个月全国确诊人数及疑似人数变化趋势图"))
    chinaline.render('近一个月全国确诊人数及疑似人数变化趋势图.html')

def get_pie(pie):

    '''绘制饼状图'''
    confirm = pie[0]
    heal = pie[1]
    dead = pie[2]
    input = pie[3]
    data_pair = [('确诊人数', confirm),('治愈人数', heal),('死亡人数', dead),('境外输入', input)]
    chinapie = Pie(init_opts=InitOpts(page_title='本年度全国疫情数据分析图'))
    chinapie.set_global_opts(title_opts=opts.TitleOpts(title='本年度全国疫情数据分析图'))
    chinapie.add(series_name="本年度全国疫情数据分析图",data_pair=data_pair, radius=['30%', '70%'])
    chinapie.render('本年度全国疫情数据分析图.html')

def get_map(result):

    '''绘制地图'''
    china_map = Map()
    china_map.add('', result, 'china').set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    #设置地图显示相关的参数
    china_map.set_global_opts(title_opts=opts.TitleOpts(title="中国确诊疫情分布图"),
                              tooltip_opts=opts.TooltipOpts(formatter='{b}: {c}'),
                              visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
    pieces=[{'min': 20001, 'label': '>10000', "color": "#893448"},
            {'min': 1000, 'max': 10000, 'label': '1000-10000',"color": "#ff585e"},
    {'min': 500, 'max': 999, 'label': '500-999', "color": "#ffb248"},
            {'min': 100, 'max': 499, 'label': '100-499', "color": "#ffb248"},
            {'min': 1, 'max': 99, 'label': '1-99', "color": "#fff2d1"}]),)
    china_map.render('中国确诊疫情分布图.html')

def get_bar(world):

    '''绘制柱状图'''
    name = [i[0] for i in world]
    count = [i[1] for i in world]
    worldbar = Bar()
    worldbar.set_global_opts(title_opts=opts.TitleOpts(title='全球疫情确诊TOP10'))
    worldbar.add_xaxis(name)
    worldbar.add_yaxis('确诊数量', count)
    worldbar.render('全球疫情确诊TOP10.html')


if __name__ == '__main__':
    html = open(url)
    line, pie, result, china, world = get_content(html)
    #生成线形图
    get_line(line)
    #生成饼状图
    get_pie(pie)
    #生成地图
    get_map(result)
    #生成柱状图
    get_bar(world)
    '''以下是将数据保存至EXCL'''
    data1 = DataFrame(china[0])
    DataFrame(data1).to_excel('中国实时数据.xlsx', index=False)
    data2 = DataFrame(china[1])
    DataFrame(data2).to_excel('中国总计数据.xlsx', index=False)


