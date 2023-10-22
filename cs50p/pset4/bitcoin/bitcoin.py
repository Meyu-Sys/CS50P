import requests
import sys

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

resp = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
rate = ((resp.json()["bpi"])["USD"])["rate"]
rt1,rt2 = rate.split(",")
rate = float(rt1 + rt2)
price = n * rate
print(f"${price:,.4f}")