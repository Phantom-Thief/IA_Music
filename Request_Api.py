import requests
import certifi
import urllib3
from pandas import DataFrame
urllib3.disable_warnings()

class Requests_Api():

    def __init__(self, p_request = "https://127.0.0.1:2999/liveclientdata/allgamedata", p_AllData = None):
        self.a_request = p_request
        self.a_AllData = requests.get(self.a_request, verify = False).json()
        self.a_query = None
        self.List_AllData = []

    def select(self):
        """
        select an object in ['activePlayer', 'events', 'gameData', 'allPlayers']
        activePlayer is a dictionnary with keys : ['abilities', 'championStats', 'currentGold', 'fullRunes', 'level', 'summonerName']
        events is a list of events with their id, name, EventTime
        gameData is a dictionnary with keys ['gameMode', 'gameTime', 'mapName', 'mapNumber', 'mapTerrain']
        allPlayers is a list with each player and their info (notable : isDead(bool),dict of player's items, team)
        """
        a_query = self.a_AllData
        return a_query

    def sortie(self):
        """Select dans scores les 'kills' et 'assists' de la personne current
        """
        self.List_AllData.append(a_query['scores']['kills'])
        self.List_AllData.append(a_query['scores']['assists'])

        """Select dans championStats la 'currentHealth'
        """
        self.List_AllData.append(a_query['championStats']['currentHealth'])

        """Select dans event le dernier event
        """
        self.List_AllData.append(a_query['events']['Events'])

    def remiseZero(self):
        self.List_AllData[:] = []

    def update(self):
        self.a_AllData = requests.get(self.a_request, verify = False).json()


# test = Requests_Api()
# print(test.start())