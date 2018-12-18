from itertools import groupby
x_data=[12,8,3]
y_data=[1200,845,210]
zipped=zip(x_data,y_data)
xy_map=[]
for x,y in groupby(sorted(zipped),key=lambda _:_[0]):
	#print(y)
	y_list=[v for n,v in y]
	#print(len(y_list))
	xy_map.append([x, sum(y_list) / len(y_list)])
print(xy_map)
x_unique,y_mean=[*zip(*xy_map)]
print(x_unique,y_mean)




