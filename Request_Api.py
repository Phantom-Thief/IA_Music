import requests
import urllib3
from Dictionnaire import pyApi
urllib3.disable_warnings()

class Requests_Api():

    def __init__(self, p_request = "https://127.0.0.1:2999/liveclientdata/allgamedata", p_AllData = None):
        """The builder of the 'Requests_Api' class.

        This class makes an 'allgamedata' request to the server of a Lol game (the game must be launched). 
        The response returns all the data on the current game stored in 'a_query'/
        The chosen objects will be stored in 'a_str_AllData'.
        
        """
        self.a_team = {}
        self.a_str_AllData = ""
        self.a_request = p_request
        self.a_AllData = requests.get(self.a_request, verify = False).json()
        self.a_AllData_bis = requests.get(self.a_request, verify = False).json()
        self.a_summonerName = self.a_AllData['activePlayer']['summonerName']
        self.a_query = 'https://127.0.0.1:2999/liveclientdata/playerscores?summonerName='+str(self.a_summonerName)
        self.a_score = requests.get(self.a_query,verify=False).json()
        self.a_score_bis = requests.get(self.a_query,verify=False).json()
        self.a_champ = ""
        self.team()

    def output_event(self):
        """Select an object in ['events'].
        
        'events' is a list of events with their id, name, EventTime.
        We retrieve the name of the event and thanks to the dictionary we transform it into a positive integer.
        If the element does not interest us -1 is returned.

        """
        event = self.a_AllData['events']['Events'][-1]
        if abs( event['EventTime'] - self.a_AllData['gameData']['gameTime'] ) <= 1:
            if event['EventName'] == 'Ace':
                team = str(event['AcingTeam'])
                if team == self.a_team[self.a_summonerName]:
                    return event['EventName'] + 'ally'
                else:
                    return event['EventName'] + 'enemy'
            else :
                try:
                    name = str(event['KillerName'])
                    team = str(self.a_team[name])

                    if event['EventName'] in pyApi.keys(): return event['EventName']+team
                except:
                    return -1
        else:
            return -1
        
    def team(self):
        allyTeam = str()
        try:
            for summoner in self.a_AllData['allPlayers']:
                name = summoner['summonerName']
                team = summoner['team']
                if name == self.a_summonerName:
                    allyTeam = team
                    self.a_champ = summoner['championName']
            for summoner in self.a_AllData['allPlayers']:
                name = summoner['summonerName']
                team = summoner['team']
                if team == allyTeam:
                    self.a_team[name]='ally'
                else:
                    self.a_team[name]='ennemy'

        except:
            return -1
    
    
    def reset_event(self):
        """Empty the string 'a_str_AllData'."""
        self.a_str_AllData = ""
      
    def event_kill_life(self):
        """Catch in a array 'event' if the player gets a kill or loses life points.

        If event[0] = 0 then the player gets no kill.
        If event[1] = 0 then the player didn't lose life points.
        If event[1] > 0 then the player lost life points.
        If event[1] < 0 then the player gained life points.
        If event[2] is True then the player is dead.

        """
        kill_init = self.a_score_bis['kills']
        life_init = self.a_AllData_bis['activePlayer']['championStats']['currentHealth']
        event = []

        kill_update = self.a_score['kills']
        life_update = self.a_AllData['activePlayer']['championStats']['currentHealth']

        kill_count = kill_update - kill_init
        event.append(kill_count)

        life_change = (life_update - life_init)/self.a_AllData['activePlayer']['championStats']['maxHealth']
        event.append(life_change)
      
        event.append(self.a_AllData['activePlayer']['championStats']['currentHealth']==0)

        
        return event  # event = [delta kills, delta HP, is dead]
        
    def update(self):
        """Restart the 'allData' and 'allData_bis query."""
        self.a_AllData_bis = self.a_AllData
        self.a_AllData = requests.get(self.a_request, verify = False).json()
        self.a_score_bis=self.a_score
        self.a_score = requests.get(self.a_query,verify=False).json()
