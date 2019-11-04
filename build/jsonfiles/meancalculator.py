
import pandas as pd
import numpy as np
import json
from datetime import datetime
from datetime import timedelta
import pytz
import dateutil.parser
import statistics

with open("./FakeData_Demo.json", 'r') as datafile:
    dataBar_temp =datafile.read()
    dataBar = json.loads(dataBar_temp)
listAges=[]
listPhysical=[]
for item in dataBar['data'][0]['sourceData']:
    for l in range(len(item['values'])):
        if item["variableName"]=='Age':
            listAges.append(item['values'][l]['value'])
        if item["variableName"]=='PhysicalActivity':
            listPhysical.append(item['values'][l]['value'])
listyoung=[]
listA=[]
listOA=[]
listO=[]
listNA=[]
for i in range(len(listAges)):
    if listAges[i]<=30 and listAges[i]>=18:
        listyoung.append(listAges[i])
    elif listAges[i]<=45 and listAges[i]>=31:
        listA.append(listAges[i])
    elif listAges[i]<=55 and listAges[i]>=46:
        listOA.append(listAges[i])
    elif listAges[i]>=55:
        listA.append(listAges[i])
    elif listAges[i]<=18:
        listNA.append(listAges[i])

countnever=listPhysical.count('Never')
count1=listPhysical.count('One to three times')
count4=listPhysical.count('Four or More')

young=len(listyoung)
adult=len(listA)
oadult=len(listOA)
old=len(listO)
na=len(listNA)

DemographicDict = {
    "data" : [
        {
            "sourceType" : 'ext',
            "sourceCodeName" : 'Pavia',
            "cityCode" : 'PAV',
            "sourceData": [
                {
                    'DataType':"Demographic",
                    'Younger Adults':young,
                    'Adults':adult,
                    'Older Adults':oadult,
                    'Older':old,
                    'N/A':na

                },
                {
                    'DataType':"Physical Activity",
                    'Never':countnever,
                    'One to three times':count1,
                    'Four or more':count4

                }


            ]
        }
    ]
}

with open("../js/testPavia.js", 'w') as file:
    file.write("var testpavia = ")
    file.write(str(DemographicDict))
