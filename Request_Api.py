import requests
import certifi
import urllib3
from pandas import DataFrame
urllib3.disable_warnings()

class Requests_Api():

    def __init__(self, p_request = "https://127.0.0.1:2999/liveclientdata/allgamedata", p_AllData = None):
        self.a_request = p_request
        self.a_AllData = requests.get(self.a_request, verify = False).json()

    def select(self,obj='activePlayer'):
        """
        select an object in ['activePlayer', 'events', 'gameData', 'allPlayers']
        activePlayer is a dictionnary with keys : ['abilities', 'championStats', 'currentGold', 'fullRunes', 'level', 'summonerName']
        events is a list of events with their id, name, EventTime
        gameData is a dictionnary with keys ['gameMode', 'gameTime', 'mapName', 'mapNumber', 'mapTerrain']
        allPlayers is a list with each player and their info (notable : isDead(bool),dict of player's items, team)
        """
        query = self.a_AllData[obj] 
        return query

    def update(self):
        self.a_AllData = requests.get(self.a_request, verify = False).json()


# test = Requests_Api()
# print(test.start())