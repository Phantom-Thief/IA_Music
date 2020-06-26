import requests
import urllib3
import json
import time
import pickle

import requests




start_time = time.time()
urllib3.disable_warnings()
# GET /repos/:owner/:repo/releases

release_tag = requests.get(
    'http://api.github.com/repos/Phantom-Thief/IA_Music/releases/latest', verify = False
    ).json()['tag_name'].strip()

current_tag = None
with open('version.txt','r') as f:
    current_tag = f.read().strip()

print(release_tag)
print(current_tag)
print(release_tag==current_tag)


print("Durée d'exécution : {}s".format(time.time()-start_time))



import zipfile



query = requests.get('http://api.github.com/repos/Phantom-Thief/IA_Music/releases/latest', verify = False).json()


# zipurl = query['zipball_url']
# resp = requests.get(zipurl)

# zname = "github.zip"
# zfile = open(zname, 'wb')
# zfile.write(resp.content)
# zfile.close()


with zipfile.ZipFile('github.zip', 'r') as zip_ref:
    zip_ref.extractall('tmp')