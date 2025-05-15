import requests
from fake_useragent import UserAgent

manufacturer = input("Which manufacturer?: ")
print("\n")
api_url = f"https://www.carwale.com/api/v4/autocomplete/?source=1%2C2%2C3%2C5%2C11%2C15%2C13%2C14%2C10%2C16%2C17%2C4%2C8%2C9%2C6%2C19%2C20%2C21%2C22%2C23%2C24%2C25%2C26%2C27%2C28%2C29&value={manufacturer}&size=20&applicationId=1&showNoResult=true&cityId=-1"

ua = UserAgent()

header ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
response = requests.get(api_url,headers=header,timeout=10)
data = response.json()
filter_data = []
for item in data:
    items = {
        "modelName": item["payload"].get("modelName"),
        "makeName" : item["payload"].get("makeName")
    }

    filter_data.append(items)

for modelname in filter_data:
    print(modelname)
