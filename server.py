import requests
import json
import processresponse
import role

class Server:

    _session: str
    _token: str

    id: str #:Server id

    owner: str #:Server owner ID

    channels: list #:Server channels
    catagories: dict #:Server catagories

    roles: dict #:Server roles
    defaultperms: list #:Server default permissions

    icon: str #:Server icon
    banner: dict #:Server banner

    name: str #:Server name
    description: str #:Server description

    def __init__(self,serverID,token,sessiontype):

        self.id=serverID
        self._token=token

        if sessiontype=='bot':
            self._session='x-bot-token'
        else:
            self._session='x-session-token'

        response=requests.get(f'https://api.revolt.chat/servers/{self.id}',headers={self._session:self._token})
        data=processresponse.processresponse(response)
        if(data ):
            self.owner=data["owner"]
            self.channels=data["channels"]
            self.categories=data["categories"]
            self.roles=data["roles"]
            self.defaultperms=data["default_permissions"]
            self.icon=data["icon"]
            self.banner=data["banner"]
            self.name=data["name"]
            self.description=data["description"]

    async def fetchmembers(self):
        "Fetches server members"
        data=""
        response=requests.get(f'https://api.revolt.chat/servers/{self.id}/members',headers={self._session:self._token})
        return processresponse.processresponse(response)

    async def fetchroles(self):
        "Fetches server roles"
        data=""
        response=requests.get(f'https://api.revolt.chat/servers/{self.id}',headers={self._session:self._token})
        data=processresponse.processresponse(response)
        if(data ): return data["roles"]
        else: return data

    async def fetchrole(self,roleID):
        return role.Role(roleID,self.id,self._token,self._session)

class Member:
    server=str
    user=str
    token=str

    roles=list
    nickname=""
    avatar=dict

    def __init__(self,serverID,userID,token,sessiontype):
        self.server=serverID
        self.user=userID
        self._token=token
        if sessiontype=='bot':
            self._session='x-bot-token'
        else:
            self._session='x-session-token'
        response=requests.get(f'https://api.revolt.chat/servers/{self.server}/members/{self.user}',headers={self._session:self._token})
        data=processresponse.processresponse(response)
        if(data ):
            self.roles=data["roles"]
            self.nickname=data["nickname"]
            self.avatar=data["avatar"]

    async def edit(self,roles=None,nickname=None,avatar=None):
        "Edits the server member with the supplied parameters"
        response=""
        if roles:
            response=requests.patch(f'https://api.revolt.chat/servers/{self.server}/members/{self.user}',data={'roles':roles},headers={self._session:self._token})
        elif nickname:
            response=requests.patch(f'https://api.revolt.chat/servers/{self.server}/members/{self.user}',data='{"nickname":"{}"}'.format(nickname),headers={self._session:self._token})
        if response:
            return processresponse.processresponse(response)