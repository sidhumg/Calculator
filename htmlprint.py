import requests,json

url_value = 'https://api.github.com/repos/pandas-dev/pandas/issues'

request = requests.get(url_value)

url_data = list(request.json())
store_data =[]

for i in range(0,len(url_data)):
    store_data.append(url_data[i]['html_url'])
    store_data.append(url_data[i]['user']['html_url'])

with open('stored.json',mode='w') as file:
    json.dump(list(store_data),file)
