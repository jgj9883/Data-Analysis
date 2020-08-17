import  pandas as pd
import json

path = "전국어린이보호데이터filed.json"
records = [json.loads(line) for line in open(path, encoding='utf-8')]
df = pd.DataFrame(records)

print()

