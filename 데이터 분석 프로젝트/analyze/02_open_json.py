import pandas as pd
import json

path = "전국어린이보호데이터.json"
records = [json.loads(line) for line in open(path, encoding='utf-8')]
df = pd.DataFrame(records)
#print(df)

filed = df['fields']
print(filed)

count =0
filedItem =[]
for filedList in filed :
    count = count + len(filedList)
    filedItem = filedItem + filedList

file = open("./전국어린이보호데이터filed.json","w+")
file.write(json.dumps(filedItem))





