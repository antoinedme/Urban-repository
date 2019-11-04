
import pandas as pd
import numpy as np
import json
from datetime import datetime
from datetime import timedelta
import pytz
import dateutil.parser
import statistics


AQIDict = {
    "data" : [
        {
            "sourceType" : 'ext',
            "sourceCodeName" : 'Barcelona',
            "cityCode" : 'BAR',
            "sourceData": [
                {
                    "variableName": 'c6h6',
                    "measuredUnit": 'μg/㎥',
                    "meanvalues":[]

                },
                {
                    "variableName": 'o3',
                    "measuredUnit": 'μg/㎥',
                    "meanvalues":[]
                },
                {
                    "variableName": 'co',
                    "measuredUnit": 'mg/㎥',
                    "meanvalues":[]
                },
                {
                    "variableName": 'h2s',
                    "measuredUnit": 'μg/㎥',
                    "meanvalues":[]
                },
                {
                    "variableName": 'nox',
                    "measuredUnit": 'μg/㎥',
                    "meanvalues":[]
                },
                {
                    "variableName": 'no2',
                    "measuredUnit": 'μg/㎥',
                    "meanvalues":[]
                },
                {
                    "variableName": 'no',
                    "measuredUnit": 'μg/㎥',
                    "meanvalues":[]
                },
            ]
        }
    ]
}


with open("/Users/mariaaliciabermudez/Documents/Internship2019/Urban Data Dashboards copy/jsonfiles/AQIBarcelona.json") as datafile:
    dataBar = json.load(datafile)
count=0
for item in dataBar['data'][0]['sourceData']:
    list2017=[]
    list2018=[]
    list2019=[]
    tempsum=0
    for l in range(len(item['values'])):
        if '2017' in  item['values'][l]['timestamp']:
            list2017.append(item['values'][l]['value'])
        elif '2018' in  item['values'][l]['timestamp']:
            list2018.append(item['values'][l]['value'])
        elif '2019' in  item['values'][l]['timestamp']:
            list2019.append(item['values'][l]['value'])
    means={
            "2017":statistics.mean(list2017),
            "2018":statistics.mean(list2018),
            "2019":statistics.mean(list2019)
    }
    print(list2017,list2018,list2019)
    print(statistics.mean(list2017))
    AQIDict['data'][0]['sourceData'][count]['meanvalues'].append(means)
    count=count+1




with open("./build/js/AQI_Bar.js", 'w') as file:
    file.write("var aqibarcelona = ")
    file.write(str(AQIDict))
