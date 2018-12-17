import pygal
from die import Die
#创建一个D6
die=Die()
#掷几次骰子把结果存在一个列表
results=[]
for roll_number in range(1000):
	result=die.roll()
	results.append(result)
#results=[results.append(die.roll()) for roll_number in range(1000)]
#分析结果
frequencies=[]
for value in range(1,die.num_sides+1):
	fenquency=results.count(value)
	frequencies.append(fenquency)

#frequencies=[frequencies.append(results.count(value)) for value in range(1,die.num_sides+1)]
#对结果进行可视化
hist=pygal.Bar()
hist.title="Results of rolling one D6 1000 times."
hist.x_labels=['1','2','3','4','5','6']#[Str(i) for i in range(1,7)]
hist.x_title="Result"
hist.y_title="Frequency of Result"

hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')
