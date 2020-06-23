import Request_Api as api
import time

while(1):
    time.sleep(1)
    print("try")
    try : 
        g_getApi = api.Requests_Api()
        break
    except:
        pass

print("fini")
