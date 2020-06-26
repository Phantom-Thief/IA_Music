import requests
import urllib3
import json
import time

import requests, zipfile, io



start_time = time.time()
urllib3.disable_warnings()
# GET /repos/:owner/:repo/releases

release_tag = requests.get('http://api.github.com/repos/Phantom-Thief/IA_Music/releases/latest', verify = False).json()['tag_name'].strip()

current_tag = None
with open('version.txt','r') as f:
    current_tag = f.read().strip()

print(release_tag)
print(current_tag)
print(release_tag==current_tag)


print("Durée d'exécution : {}s".format(time.time()-start_time))



query = requests.get('http://api.github.com/repos/Phantom-Thief/IA_Music/releases/latest', verify = False).json()



print([i for i in query])

requests.get(query['tarball_url'])