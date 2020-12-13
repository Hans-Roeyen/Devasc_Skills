import requests
import json

access_token = 'NzkzN2I3ZDAtMTM5My00MTg1LTkwYzEtNTk1NWY3OWNiNGM5ZjcyMjZiM2EtNzll_PF84_e4d4112d-2548-4a47-810e-04fe45ea181f' 
room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vMjhkYWRiYjAtM2QyOC0xMWViLWE3YjQtOTUwMjNmZDUwODNh"
person_email = 'yvan.rooseleer@biasc.be'
url = 'https://webexapis.com/v1/memberships'

headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

params = {'roomId': room_id, 'personEmail': person_email}
res = requests.post(url, headers=headers, json=params)
print(json.dumps(res.json(), indent=4))