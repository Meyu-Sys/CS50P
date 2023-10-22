import requests
import system
try:
    n = float(sys.argv[1])

resp = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
rate = ((resp.json()["bpi"])["USD"])["rate"]
rt1,rt2 = rate.split(",")
rate = float(rt1 + rt2)