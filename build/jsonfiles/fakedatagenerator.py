import pandas as pd
import numpy as np
import json
import pytz
import dateutil.parser

import random
valuesPActivity=['Never','One to three times','Four or More']
AQIDict ={}
AQIDict['data']=[]
AQIDict['data'].append({
    "sourceType" : 'ext',
    "sourceCodeName" : 'Pavia',
    "cityCode" : 'PAV',
    "sourceData":[]
})
AQIDict['data'][0]["sourceData"].append({
    "variableName": 'Age',
    "measuredUnit": 'years',
    "values":[]
})
AQIDict['data'][0]["sourceData"].append({
    "variableName": 'PhysicalActivity',
    "measuredUnit": 'Times/Week',
    "values":[]
})



temp={}
listAges=[]
listActivity=[]

for i in range(0,300000):
    count=0
    for item in AQIDict['data'][0]['sourceData']:
        if count==0:
            val={
                "Id": i,
                "value": random.randint(5,100)
            }
        if count==1:
            val={
                "Id": i,
                "value": random.choice(valuesPActivity)
            }
        count=count+1
        item['values'].append(val)





with open("./FakeData_Demo.json", 'w') as file:
    json.dump(AQIDict,file, indent=4)
