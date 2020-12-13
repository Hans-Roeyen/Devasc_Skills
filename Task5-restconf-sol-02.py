import json
import requests
requests.packages.urllib3.disable_warnings()

api_url ="https://192.168.41.129:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor"

headers = {"Accept":"application/yang-data+json",
           "Content-Type":"application/yang-data+json"
          }
basicauth = ("cisco", "cisco123!")

yangConfig = {
    "Cisco-IOS-XE-native:monitor": {
        "severity": "warnings"
            }
        }

resp = requests.post(api_url, data=json.dumps(yangConfig), auth=basicauth,headers=headers,verify=False)

print(resp)