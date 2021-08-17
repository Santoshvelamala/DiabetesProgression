import requests
import json

url = 'http://localhost:8002/predict/'
#['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']
#data = [[22, 1, 115, 120, 10, 10, 15, 22, 5, 33.0]]
data = [{'age':22,'sex':1,'bmi':115,'bp':120,'s1':10,'s2':10,'s3':15,'s4':22,'s5':5,'s6':33.0}]
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)