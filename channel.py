import message
import requests
import json

class Channel:
    "Channel class"
    id: str #:The channel's ID
    _token: str
    _session: str

    def __init__(self,id,token,sessiontype):
        self.id=id
        self._token=token
        if sessiontype=='bot':
            self._session='x-bot-token'
        else:
            self._session='x-session-token'

    async def sendmessage(self,data):
        "Send a message"
        await message.sendmessage(self.id,data,self._token,self._sessiontype)

    async def fetchmessages(self,limit:int):
        "Fetches messages"
        return await message.fetchmessages(self.id,self._token,self._sessiontype,limit)

    async def fetchdata(self):
        "Fetches channel data"
        response=""
        response=requests.get(f'https://api.revolt.chat/channels/{self.id}',headers={self._session:self._token})
        if response.status_code==200:
            return json.loads(response.content)
        elif response.status_code==403:
            print("Permission denied")
        elif response.status_code==404:
            print("Channel not found")
