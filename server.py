import requests
import json

class Server:
    def __init__(self,serverID,token,sessiontype):
        self.id=serverID
        self.token=token
        if sessiontype=='bot':
            self.session='x-bot-token'
        else:
            self.session='x-session-token'
    
    async def fetchdata(self):
        data=""
        response=requests.get(f'https://api.revolt.chat/servers/{self.id}',headers={self.session:self.token})
        if response.status_code==200:
            return json.loads(response.content)
        elif response.status_code==403:
            print("Permission denied")
        elif response.status_code==404:
            print("Server not found")
    
    async def fetchmembers(self):
        data=""
        response=requests.get(f'https://api.revolt.chat/servers/{self.id}/members',headers={self.session:self.token})
        if response.status_code==200:
            data=json.loads(response.content)
        elif response.status_code==403:
            print("Permission denied")
        elif response.status_code==404:
            print("Server not found")
        print(data)

#class member: