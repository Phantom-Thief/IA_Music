import requests
import urllib3
import json
import zipfile
import os
import shutil

urllib3.disable_warnings()

# https://sookocheff.com/post/tools/downloading-directories-of-code-from-github-using-the-github-api/

from github import Github
import base64

def get_sha_for_tag(repository, tag):
    """
    Returns a commit PyGithub object for the specified repository and tag.
    """
    branches = repository.get_branches()
    matched_branches = [match for match in branches if match.name == tag]
    if matched_branches:
        return matched_branches[0].commit.sha

    tags = repository.get_tags()
    matched_tags = [match for match in tags if match.name == tag]
    if not matched_tags:
        raise ValueError('No Tag or Branch exists with that name')
    return matched_tags[0].commit.sha

def download_directory(repository, sha, server_path):
    """
    Download all contents at server_path with commit tag sha in
    the repository.
    """
    contents = repository.get_dir_contents(server_path, ref=sha)

    for content in contents:
        print ("Processing %s" % content.path)
        if content.type == 'dir':
            download_directory(repository, sha, content.path)
        else:
            path = content.path
            file_content = repository.get_contents(path, ref=sha)
            file_data = base64.b64decode(file_content.content)
            file_out = open(content.name, "wb")
            file_out.write(file_data)
            file_out.close()


def download_directory_from_git(tag,directory):
    g = Github()

    repository = g.get_repo(full_name_or_id='Phantom-Thief/IA_Music')
    
    branch_or_tag_to_download = str(tag)
    sha = get_sha_for_tag(repository, branch_or_tag_to_download)

    directory_to_download = str(directory)
    download_directory(repository, sha, directory_to_download)

def updater():
    release_tag = requests.get(
        'http://api.github.com/repos/Phantom-Thief/IA_Music/releases/latest', verify = False
        ).json()['tag_name'].strip()

    current_tag = None
    with open('version.txt','r') as f:
        current_tag = f.read().strip()

    if current_tag == release_tag: return

    print('Launching update')

    path = os.getcwd()
    print ("The current working directory is %s" % path)
    os.mkdir(release_tag)

    
updater()
