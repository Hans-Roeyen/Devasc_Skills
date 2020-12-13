import json
import requests
requests.packages.urllib3.disable_warnings()

api_url ="https://192.168.41.129:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity"

headers = {"Accept":"application/yang-data+json",
           "Content-Type":"application/yang-data+json"
          }
basicauth = ("cisco", "cisco123!")

resp = requests.delete(api_url, auth=basicauth,headers=headers,verify=False)
response_json = resp.json()
print(resp)
