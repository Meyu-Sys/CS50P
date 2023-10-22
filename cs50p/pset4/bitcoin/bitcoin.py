import requests
import json
resp = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
print(json.dump(resp.json(), indent=2))