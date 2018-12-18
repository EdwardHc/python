from datetime import datetime
from matplotlib import pyplot as plt
from date_temperature_file import GetDateTem
# Get dates, high, and low temperatures from file.
filename1 = 'sitka_weather_2014.csv'
filename2 = 'death_valley_2014.csv'
a1=GetDateTem()
a1.getTemperatureFromFile(filename1)
a2=GetDateTem()
a2.getTemperatureFromFile(filename2)
#根据数据绘制图形
fig=plt.figure(dpi=100,figsize=(10,6))

plt.plot(a1.dates,a1.highs,c='red',alpha=0.5)
plt.plot(a1.dates,a1.lows,c='blue',alpha=0.5)
plt.fill_between(a1.dates,a1.highs,a1.lows,facecolor='blue',alpha=0.1)

plt.plot(a2.dates,a2.highs,c='red',alpha=0.5)
plt.plot(a2.dates,a2.lows,c='blue',alpha=0.5)
plt.fill_between(a2.dates,a2.highs,a2.lows,facecolor='blue',alpha=0.1)
#设置图形的格式
plt.title('Daily high temperature, - 2014',fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.show()


