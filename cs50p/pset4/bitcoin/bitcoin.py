import requests
import json
resp = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
print(json.dumps(resp.json(), indent=2))