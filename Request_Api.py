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
        
        """
        self.a_list_AllData = []
        self.a_request = p_request
        self.a_AllData = requests.get(self.a_request, verify = False).json()
        self.a_AllData_bis = requests.get(self.a_request, verify = False).json()     
        
        

    def output(self):
        """Select an object in ['activePlayer', 'events', 'gameData', 'allPlayers'].
        
        'activePlayer' is a dictionnary with keys : ['abilities', 'championStats', 'currentGold', 'fullRunes', 'level', 'summonerName'].
        'events' is a list of events with their id, name, EventTime.
        'gameData' is a dictionnary with keys ['gameMode', 'gameTime', 'mapName', 'mapNumber', 'mapTerrain']
        'allPlayers' is a list with each player and their info (notable : isDead(bool),dict of player's items, team).
        We are storing the 'kills', 'assists', 'currentHealth of the current person and the last event in 'a_list_AllData'.

        """
        self.a_list_AllData.append(self.a_AllData['activePlayer']['championStats']['currentHealth'])
        self.a_list_AllData.append(self.a_AllData['allPlayers'][0]['scores']['assists'])
        self.a_list_AllData.append(self.a_AllData['allPlayers'][0]['scores']['kills'])
        # self.a_list_AllData.append(self.a_AllData['events']['Events'][-1])
        self.a_list_AllData.append(self.a_AllData['gameData']['gameTime'])
        return self.a_list_AllData

    def reset(self):
        """Empty the list 'a_list_AllData'."""
        self.a_list_AllData[:] = []
      
    def Event_kill_life(self):
        """Catch in a array 'event' if the player gets a kill or loses life points.

        If event[0] = 0 then the player gets no kill.
        If event[1] = 0 then the player didn't lose life points.
        If event[1] > 0 then the player lost life points.
        If event[1] < 0 then the player gained life points.

        """
        kill_init = self.a_AllData_bis['allPlayers'][0]['scores']['kills']
        life_init = self.a_AllData_bis['activePlayer']['championStats']['currentHealth']
        event = []

        kill_update = self.a_AllData['allPlayers'][0]['scores']['kills']
        life_update = self.a_AllData['activePlayer']['championStats']['currentHealth']

        kill_count = kill_update - kill_init
        event.append(kill_count)

        life_change = life_update - life_init
        event.append(life_change)

        event.append(self.a_AllData['gameData']['gameTime'])

        return event
        

    def update(self):
        """Restart the 'allData' and 'allData_bis query."""
        self.a_AllData_bis = self.a_AllData
        self.a_AllData = requests.get(self.a_request, verify = False).json()
