import matplotlib.pyplot as plt
x_values=list(range(1,5001))
y_values=[x**3 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=40)
plt.title("Cubic Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Cubic of Value",fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)
#plt.axis([0,5500,0,1100000])
#plt.show()
plt.savefig('Cubic_plot.png',bbox_inches='tight')
