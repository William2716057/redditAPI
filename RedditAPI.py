import json
import time
import httpx
import pandas as pd

#change to user input
baseURL = 'https://www.reddit.com'
endpoint = '/r/' + input("Enter endpoint (eg. python/): ")
category = input("Enter category (eg. hot/): ")

url = baseURL + endpoint + category + ".json"
afterPostID = None
dataset = []

for _ in range(5):
    params ={
    'limit': 100,
    't': 'year', #time unit
    'after': afterPostID
    }
    
response = httpx.get(url, params=params)
print(f'fetching "{response.url}"....')
if response.status_code !=200:
    raise Exception('Failed to fetch data')

json_data = response.json()

dataset.extend([rec['data'] for rec in json_data['data']['children']])

afterPostID = json_data['data']['after']
time.sleep(0.5)

df = pd.DataFrame(dataset)
df.to_csv('results.csv', index=False)
