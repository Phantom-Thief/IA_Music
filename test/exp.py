from github import Github
import github

g = Github('','')

repo = g.get_repo(full_name_or_id='https://github.com/Phantom-Thief/IA_Music')