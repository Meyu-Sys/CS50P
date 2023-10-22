import requests
import json
resp = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
print(resp)
# print(json.dump(resp, indent=2))