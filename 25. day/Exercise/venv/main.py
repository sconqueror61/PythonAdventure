"""with open("weather_data.csv") as data_file:
	data= data_file.readlines()
	print(data)"""

"""import csv
with open("weather_data.csv") as data_file:
	data=csv.reader(data_file)
	temperatures=[]
	for row in data:
		if row[1]!= "temp":
			temperatures.append(row[1])
	print(temperatures)"""

import pandas

data=pandas.read_csv("weather_data.csv")
#print(type(data))
#print(data["temp"])
temp_list=data_dict=data.to_dict
print(temp_list)

print(data["temp"].mean())
print(data["temp"].max())

#Get data in Culıums
print(data["condition"])
print(data.condition)

#Get Data in Row
print(data[data.day=="Monday"])
print(data[data.temp==data.temp.max()])

moday= data[data.day=="Monday"]
monday_temp=monday.temp[0]
monday_temp_F=monday_temp*9/5+32
print(monday_temp_F)

#Create a data frame scratch
data_dict={
	"student":["Amy","James","Seyfullah"],
	"scores":[76,56,65]
}
data=pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")