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
        self.a_query = self.a_AllData
        return self.a_query

    def output(self):
        """Select in scores the 'kills' and 'assists' of the current person.
        """
        self.List_AllData.append(self.a_AllData['scores']['kills'])
        self.List_AllData.append(self.a_AllData['scores']['assists'])

        """Select in championStats the 'currentHealth'
        """
        self.List_AllData.append(self.a_AllData['championStats']['currentHealth'])

        """Select in event the last event
        """
        self.List_AllData.append(self.a_AllData['events']['Events'][-1])

    """
    Empty the list 'List_AllData'.
    """
    def reset(self):
        self.List_AllData[:] = []

    """
    restart the 'allData' query
    """
    def update(self):
        self.a_AllData = requests.get(self.a_request, verify = False).json()
