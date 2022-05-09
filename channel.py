import message
import requests
import json
import processresponse

class Channel:
    "Channel class"

    id: str #:The channel's ID

    _token: str
    _session: str

    server: str #:The channel's server's id
    name: str #:The channel's name
    description: str #:The channel's description
    icon: dict #:Data about the channel's icon

    default_permissions: dict #:The channel's default permissions
    role_permissions: dict #:The channel's role permissions
    nsfw: bool #:Whether or not the channel is nsfw

    def __init__(self,id,token,sessiontype):
        self.id=id
        self._token=token
        if sessiontype=='bot':
            self._session='x-bot-token'
        else:
            self._session='x-session-token'
        response=""
        response=requests.get(f'https://api.revolt.chat/channels/{self.id}',headers={self._session:self._token})
        data=processresponse.processresponse(response)
        self.server=data["server"]
        self.name=data["name"]
        self.default_permissions=data["default_permissions"]
        self.role_permissions=data["role_permissions"]
        self.nsfw=data["nsfw"]

        if("description" in data): self.description=data["description"]
        if("icon" in data): self.icon=data["icon"]


    async def sendmessage(self,data):
        "Send a message"
        await message.sendmessage(self.id,data,self._token,self._sessiontype)

    async def fetchmessages(self,limit:int):
        "Fetches messages"
        return await message.fetchmessages(self.id,self._token,self._sessiontype,limit)