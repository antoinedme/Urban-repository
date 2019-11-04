import json


with open("/Users/mariaaliciabermudez/Documents/Internship2019/Urban Data Dashboards copy/data.json") as datafile:
    data = json.load(datafile)

#data['data'] # example
print(data)
print(type(data))
datastr=str(data)
print(type(datastr))
with open("./js/test2.js", 'w') as file:
    file.write("var testi = ")
    file.write(datastr)
