import json
import requests

with open('config.json') as config:
    cfg = json.loads(config.read())

response = requests.get(cfg["lmf"]["historical_url"], headers=cfg["lmf"]["headers"], params=cfg["lmf"]["querystring"])
status_code = response.status_code

if status_code == 200:
    data = json.loads(response.text)
    with open('historical_nav.json','w') as current:
        json.dump(data, current, indent=4)
else:
    print(status_code)

