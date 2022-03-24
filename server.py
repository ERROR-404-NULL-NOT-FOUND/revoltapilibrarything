import requests
import json
import processresponse
import role

class Server:

    session=str
    token=str
    
    id=str
    
    owner=str

    channels=list
    catagories=dict
    
    roles=dict
    defaultperms=list
    
    icon=str
    banner=dict
    
    name=str
    description=str
    
    def __init__(self,serverID,token,sessiontype):
        
        self.id=serverID
        self.token=token
        
        if sessiontype=='bot':
            self.session='x-bot-token'
        else:
            self.session='x-session-token'
        
        response=requests.get(f'https://api.revolt.chat/servers/{self.id}',headers={self.session:self.token})
        data=processresponse.processresponse(response)
        
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
        data=""
        response=requests.get(f'https://api.revolt.chat/servers/{self.id}/members',headers={self.session:self.token})
        return processresponse.processresponse(response)
    async def fetchroles(self):
        data=""
        response=requests.get(f'https://api.revolt.chat/servers/{self.id}',headers={self.session:self.token})
        data=processresponse.processresponse(response)
        return data["roles"]
    async def fetchrole(self,roleID):
        return role.Role(roleID,self.id,self.token,self.session)

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
        self.token=token
        if sessiontype=='bot':
            self.session='x-bot-token'
        else:
            self.session='x-session-token'
        response=requests.get(f'https://api.revolt.chat/servers/{self.server}/members/{self.user}',headers={self.session:self.token})
        data=processresponse.processresponse(response) 
        self.roles=data["roles"]
        self.nickname=data["nickname"]
        self.avatar=data["avatar"]
    
    async def edit(self,roles=None,nickname=None,avatar=None):
        response=""
        if roles:
            response=requests.patch(f'https://api.revolt.chat/servers/{self.server}/members/{self.user}',data={'roles':roles},headers={self.session:self.token})
        elif nickname:
            response=requests.patch(f'https://api.revolt.chat/servers/{self.server}/members/{self.user}',data='{"nickname":"{}"}'.format(nickname),headers={self.session:self.token})
        if response:
            return processresponse.processresponse(response)