import requests
import certifi
import urllib3
from Dictionnaire import pyApi
from pandas import DataFrame
urllib3.disable_warnings()

class Requests_Api():

    def __init__(self, p_request = "https://127.0.0.1:2999/liveclientdata/allgamedata", p_AllData = None):
        """The builder of the 'Requests_Api' class.

        This class makes an 'allgamedata' request to the server of a Lol game (the game must be launched). 
        The response returns all the data on the current game stored in 'a_query'/
        The chosen objects will be stored in 'a_str_AllData'.
        
        """
        self.a_str_AllData = ""
        self.a_request = p_request
        self.a_AllData = requests.get(self.a_request, verify = False).json()
        self.a_AllData_bis = requests.get(self.a_request, verify = False).json()
        self.a_summonerName = self.a_AllData['activePlayer']['summonerName']
        self.a_query = 'https://127.0.0.1:2999/liveclientdata/playerscores?summonerName='+str(self.a_summonerName)
        self.a_score = requests.get(self.a_query,verify=False).json()
        self.a_score_bis = requests.get(self.a_query,verify=False).json()
        
        

    def output_event(self):
        """Select an object in ['events'].
        
        'events' is a list of events with their id, name, EventTime.
        We retrieve the name of the event and thanks to the dictionary we transform it into an interger.
        If the element does not interest us -1 is returned.

        """
        self.a_str_AllData = self.a_AllData['events']['Events'][-1]['EventName']
        try:
            return pyApi[self.a_list_AllData]
        except:
            return -1
        

    def reset_event(self):
        """Empty the string 'a_str_AllData'."""
        self.a_str_AllData = ""
        pass
      
    def Event_kill_life(self):
        """Catch in a array 'event' if the player gets a kill or loses life points.

        If event[0] = 0 then the player gets no kill.
        If event[1] = 0 then the player didn't lose life points.
        If event[1] > 0 then the player lost life points.
        If event[1] < 0 then the player gained life points.

        """
        kill_init = self.a_score_bis['kills']
        life_init = self.a_AllData_bis['activePlayer']['championStats']['currentHealth']
        event = []

        kill_update = self.a_score['kills']
        life_update = self.a_AllData['activePlayer']['championStats']['currentHealth']

        kill_count = kill_update - kill_init
        event.append(kill_count)

        life_change = life_update - life_init
        event.append(life_change)
      
        event.append(self.a_AllData['activePlayer']['championStats']['currentHealth']==0)

        event.append(self.a_AllData['gameData']['gameTime'])

        return event
        

    def update(self):
        """Restart the 'allData' and 'allData_bis query."""
        self.a_AllData_bis = self.a_AllData
        self.a_AllData = requests.get(self.a_request, verify = False).json()
        self.a_score_bis=self.a_score
        self.a_score = requests.get(self.a_query,verify=False).json()