import requests
import json

access_token = 'NzkzN2I3ZDAtMTM5My00MTg1LTkwYzEtNTk1NWY3OWNiNGM5ZjcyMjZiM2EtNzll_PF84_e4d4112d-2548-4a47-810e-04fe45ea181f' 
url = 'https://webexapis.com/v1/people/me'

headers = {
    'Authorization': 'Bearer {}'.format(access_token)
    }
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))