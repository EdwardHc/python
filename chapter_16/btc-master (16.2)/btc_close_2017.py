from __future__ import (absolute_import,division,print_function,unicode_literals)
from itertools import groupby
try:
	#python 2.x 版本
	from urllib2 import urlopen
except ImportError:
	#python 3.x 版本
	from urllib.request import urlopen
import json,pygal,math
#将数据加载到一个列表
def draw_line(x_data,y_data,title,y_legend):
	xy_map=[]
	for x,y in groupby(sorted(zip(x_data,y_data)),key=lambda _:_[0]):
		y_list=[v for _,v in y]
		xy_map.append([x,sum(y_list)/len(y_list)])
	x_unique,y_mean=[*zip(*xy_map)]
	line_chart=pygal.Line()
	line_chart.title=title
	line_chart.x_labels=x_unique
	line_chart.add(y_legend, y_mean)
	line_chart.render_to_file(title+'.svg')
	return line_chart
filename='btc_close_2017.json'
with open(filename) as f:
	btc_data=json.load(f)
#每一天的信息
dates,months,weeks,weekdays,close=[],[],[],[],[]
for btc_dict in btc_data:
	dates.append(btc_dict['date'])
	months.append(int(btc_dict['month']))
	weeks.append(int(btc_dict['week']))
	weekdays.append(btc_dict['weekday'])
	close.append(int(float(btc_dict['close'])))
idx_month=dates.index('2017-12-01')
#print(idx_month)
line_chart_month=draw_line(months[:idx_month],close[:idx_month],'收盘价月日均值（¥）','月日均值')
line_chart_month
# line_chart=pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
# line_chart.title='收盘价对数变换（¥）'
# line_chart.x_labels=dates
# N=20 #X轴坐标每隔20天显示一次
# line_chart.x_labels_major=dates[::N]
# close_log=[math.log10(_) for _ in close]
# line_chart.add('收盘价',close)
# line_chart.render_to_file('收盘价折线图（¥）.svg')
	#print("{} is month {} week {}, {}, the close price is {} RMB".format(date,month,week,weekday,close))
# ~ import requests
# ~ json_url='https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# ~ req=requests.get(json_url)
# ~ #将数据写入文件
# ~ with open('btc_close_2017_request.json','w') as f:
	# ~ f.write(req.text)
# ~ #加载json格式
# ~ file_request=req.json()

