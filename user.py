import requests
import json

class User:
    id=""
    token=""
    session=""
    def __init__(self, userID, token, sessiontype):
        if sessiontype=='bot':
            self.session="x-bot-token"
        else:
            self.session='x-session-token'
        self.token=token
        self.id=userID
    
    async def fetchdata(self):
        data=""
        response=requests.get(f'https://api.revolt.chat/users/{self.id}',headers={self.session:self.token})
        if response.status_code==200:
            return json.loads(response.content)
        elif response.status_code==403:
            print("Permission denied")
        elif response.status_code==404:
            print("User not found")