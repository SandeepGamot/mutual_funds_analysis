import json
import requests

with open('config.json') as config:
    cfg = json.loads(config.read())

response = requests.get(cfg["bse"]["url"], headers=cfg["bse"]["headers"])
status_code = response.status_code

if status_code == 200:
    data = json.loads(response.text)
    print(json.dumps(data, indent=4, sort_keys=True))
else:
    print(status_code)
