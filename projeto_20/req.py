import requests
import json

url = "http://tempook.com.br/DATABASE/UND_inmet_202002130700.txt"
r = requests.get(url).text
d = dict()
for l in r.splitlines():
    s = l.split()
    d[s[0]] = {
        "latitude": s[1],
        "longitude": s[2],
        "altitude": s[3]
    }
print(json.dumps(d, indent=2))
