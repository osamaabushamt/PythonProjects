
#    content = data_file.readlines()
#
#
#data = []
#
#for w in content:
#    data.append(w.rstrip())
#    print(data)
#


#import csv
#
#with open("./weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temp = []
#    for row in data:
#        if row[1] != "temp":
#            temp.append(int(row[1]))
#    print(temp)

import pandas

data = pandas.read_csv("./weather_data.csv")
temp_data = data["temp"]
print(temp_data.max())


