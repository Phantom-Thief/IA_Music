import requests
import urllib3
import json

urllib3.disable_warnings()
# GET /repos/:owner/:repo/releases

query = requests.get('http://api.github.com/repos/Phantom-Thief/IA_Music/releases/latest', verify = False).json()

print(
    query['tag_name']
)