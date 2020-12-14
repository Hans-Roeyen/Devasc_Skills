import requests
import json

access_token = 'YjlhYmE2ZGYtNGQyZi00ZDZjLTk3MjAtZjMyODQyYzExNDI1YjQ5NDk5MTAtOGVh_PF84_e4d4112d-2548-4a47-810e-04fe45ea181f' 
room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vMjhkYWRiYjAtM2QyOC0xMWViLWE3YjQtOTUwMjNmZDUwODNh"
message = 'Here are my screenshots of netacad-devasc skills-based exam!'
url = 'https://webexapis.com/v1/messages'

headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(json.dumps(res.json(), indent=4))

