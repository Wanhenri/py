import requests
import json
from datetime import datetime, timedelta

inicio = datetime.now()
a = inicio - timedelta(hours=3)
dateInmet = a.strftime("%Y%m%d%H")

#dateInmet="2020021307"

def get_inmet(dateInmet):
    url = "http://tempook.com.br/DATABASE/UND_inmet_"+ str(dateInmet) +"00.txt"
    r = requests.get(url).text
    d = dict()
    for l in r.splitlines():
        s = l.split()
        d[s[0]] = {
            "Latitude": s[1],
            "Longitude": s[2],
            "Altitude": s[3],
            "Ano":s[4],
            "Mes":s[5], 
            "Dia":s[6],
            "Hora":s[7],                    
            "Temp":s[8], 
            "Tmax":s[9], 
            "Tmin":s[10], 
            "UR":s[11], 
            "URmax":s[12], 
            "URmin":s[13], 
            "Prec":s[24]
        }
    return json.dumps(d, indent=2)

application = get_inmet(dateInmet)
print(application)
print(a)
print(dateInmet)
