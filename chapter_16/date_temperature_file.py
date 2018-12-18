import csv
from datetime import datetime
class GetDateTem():
	def __init__(self):
		self.dates=[]
		self.highs=[]
		self.lows=[]
	
	def getTemperatureFromFile(self,filename):
		with open(filename) as f:
			reader = csv.reader(f)
			header_row = next(reader)
			for row in reader:
				try:
					current_date=datetime.strptime(row[0],"%Y-%m-%d")
					high=int(row[1])
					low=int(row[3])
				except ValueError:
					print(current_date,'missing data')
				else:
					self.dates.append(current_date)
					self.highs.append(int(row[1]))
					self.lows.append(int(row[3]))
