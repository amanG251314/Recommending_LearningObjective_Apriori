import json
import requests

url = 'http://127.0.0.1:8000/model'
input1 = [-6, 6, -1, -1, 2, 1, 0, 1, 0, 1, 35]
unit = 'Merge sort'
neighbours = 10
request_data = json.dumps({'input': input1, 'unit': unit, 'neighbours': neighbours})
response = requests.post(url, request_data)
print(response.text)
