from riotwatcher import LolWatcher, ApiError
import pandas as pd
import requests
import time

# golbal variables
api_key = 'RGAPI-fd76932d-f467-436f-a1dc-3ae6b8650fdc'
watcher = LolWatcher(api_key)
my_region = 'euw1'

me = watcher.summoner.by_name(my_region, '1NainCapable')
print(me)
print()
# Return the rank status
my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
print(my_ranked_stats)

my_matches = watcher.match.matchlist_by_account(my_region, me['accountId'])

# fetch last match detail
last_match = my_matches['matches'][2]
match_detail = watcher.match.by_id(my_region, last_match['gameId'])

print()

participants = []
for row in match_detail['participants']:
    participants_row = {}
    participants_row['champion'] = row['championId']
    participants_row['spell1'] = row['spell1Id']
    participants_row['spell2'] = row['spell2Id']
    participants_row['win'] = row['stats']['win']
    participants_row['kills'] = row['stats']['kills']
    participants_row['deaths'] = row['stats']['deaths']
    participants_row['assists'] = row['stats']['assists']
    participants_row['totalDamageDealt'] = row['stats']['totalDamageDealt']
    participants_row['goldEarned'] = row['stats']['goldEarned']
    participants_row['champLevel'] = row['stats']['champLevel']
    participants_row['totalMinionsKilled'] = row['stats']['totalMinionsKilled']
    participants_row['item0'] = row['stats']['item0']
    participants_row['item1'] = row['stats']['item1']
    participants.append(participants_row)
df = pd.DataFrame(participants)
print(df)

time.sleep(5)

swagger = requests.get("https://127.0.0.1:2999/swagger/v2/swagger.json", verify=False)
openapi = requests.get("https://127.0.0.1:2999/swagger/v3/openapi.json", verify=False)