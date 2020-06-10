import requests
import certifi
import urllib3
from pandas import DataFrame
urllib3.disable_warnings()

class Requests_Api():

    def __init__(self, p_request = "https://127.0.0.1:2999/liveclientdata/allgamedata", p_AllData = None):
        """The builder of the 'Requests_Api' class.

        This class makes an 'allgamedata' request to the server of a Lol game (the game must be launched). 
        The response returns all the data on the current game stored in 'a_query'/
        The chosen objects will be stored in 'a_list_AllData'.
        To make this request it is necessary to have a key API linked to your Lol account.
        
        """
        self.a_request = p_request
        self.a_AllData = requests.get(self.a_request, verify = False).json()
        self.a_list_AllData = []

    def output(self):
        """Select an object in ['activePlayer', 'events', 'gameData', 'allPlayers'].
        
        'activePlayer' is a dictionnary with keys : ['abilities', 'championStats', 'currentGold', 'fullRunes', 'level', 'summonerName'].
        'events' is a list of events with their id, name, EventTime.
        'gameData' is a dictionnary with keys ['gameMode', 'gameTime', 'mapName', 'mapNumber', 'mapTerrain']
        'allPlayers' is a list with each player and their info (notable : isDead(bool),dict of player's items, team).
        We are storing the 'kills', 'assists', 'currentHealth of the current person and the last event in 'a_list_AllData'.

        """
        self.a_list_AllData.append(self.a_AllData['scores']['kills'])
        self.a_list_AllData.append(self.a_AllData['scores']['assists'])
        self.a_list_AllData.append(self.a_AllData['championStats']['currentHealth'])
        self.a_list_AllData.append(self.a_AllData['events']['Events'][-1])

    def reset(self):
        """Empty the list 'a_list_AllData'."""
        self.a_list_AllData[:] = []

    def update(self):
        """Restart the 'allData' query."""
        self.a_AllData = requests.get(self.a_request, verify = False).json()
