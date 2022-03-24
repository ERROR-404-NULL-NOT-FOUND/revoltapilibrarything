import message
import requests
import json

class Channel:
    id=""
    token=""
    sessiontype=""
    session=""
    
    def __init__(self,id,token,sessiontype):
        self.id=id
        self.token=token
        self.sessiontype=sessiontype
        if sessiontype=='bot':
            self.session='x-bot-token'
        else:
            self.session='x-session-token'
    
    async def sendmessage(self,data):
        await message.sendmessage(self.id,data,self.token,self.sessiontype)
    
    async def fetchmessages(self,limit:int):
       return await message.fetchmessages(self.id,self.token,self.sessiontype,limit)
    
    async def fetchdata(self):
        response=""
        response=requests.get(f'https://api.revolt.chat/channels/{self.id}',headers={self.session:self.token})
        if response.status_code==200:
            return json.loads(response.content)
        elif response.status_code==403:
            print("Permission denied")
        elif response.status_code==404:
            print("Channel not found")
