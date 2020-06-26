import requests
import urllib3
import json
import zipfile
import os
import shutil

urllib3.disable_warnings()

def updater():
    release_tag = requests.get(
        'http://api.github.com/repos/Phantom-Thief/IA_Music/releases/latest', verify = False
        ).json()['tag_name'].strip()

    current_tag = None
    with open('version.txt','r') as f:
        current_tag = f.read().strip()

    if current_tag == release_tag: return

    print('Launching update')

    zipurl = requests.get('http://api.github.com/repos/Phantom-Thief/IA_Music/releases/latest', verify = False).json()['zipball_url']

    resp = requests.get(zipurl)

    print('Update downloaded')

    zname = release_tag
    zfile = open(zname, 'wb')
    zfile.write(resp.content)
    zfile.close()

    with zipfile.ZipFile(release_tag, 'r') as zip_ref:
        zip_ref.extractall('tmp')

    shutil.rmtree('/'+current_tag, ignore_errors=True)
    with open('version.txt','w') as f:
        f.write(release_tag)

    print('Update installed')