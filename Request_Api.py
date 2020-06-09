import requests
import certifi
import urllib3
from pandas import DataFrame
urllib3.disable_warnings()

class Requests_Api():

    def __init__(self, p_request = "https://127.0.0.1:2999/liveclientdata/allgamedata", p_AllData = None):
        self.a_request = p_request
        self.a_AllData = p_AllData
        self.a_df = None

    def start(self):
        self.a_AllData = """ """ + requests.get(self.a_request, verify = False).json()
        df = DataFrame(self.a_AllData)
        return df
