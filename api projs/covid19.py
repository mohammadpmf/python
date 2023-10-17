import requests
import json
response = requests.get("https://one-api.ir/corona/?token=258252:647f0bae10f6c")
print("\n\n\n\t\t-----The Information of Covid in the world-----\n")
print(f"{'country':45}{'cases':16}{'deaths':16}{'recovered':16}")
print('-'*100)
for item in json.loads(response.content)['result']['entries']:
    try:
        country = item['country']
        cases = item['cases']
        deaths = item['deaths']
        recovered = item['recovered']
        if country!="":
            print(f"{country:45}{cases:16}{deaths:16}{recovered:16}")
            print('-'*100)
    except:
        pass