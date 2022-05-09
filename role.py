from concurrent.futures import process
import requests
import json
import processresponse
class Role:
    roleID: str #:The role's id
    _token: str
    _session: str
    name: str #:The role's name
    serverID: str #:The role's server ID
    def __init__(self,roleID,serverID,token,session):
        self.roleID=roleID
        self.serverID=serverID
        self._token=token
        self._session=session
        response=requests.get(f'https://api.revolt.chat/servers/{serverID}',headers={session:token})
        data=processresponse.processresponse(response)
        if(data):
            self.name=data["roles"][roleID]["name"]

    async def fetchinfo(self):
        """Fetches info about the role"""
        response=requests.get(f'https://api.revolt.chat/servers/{self.serverID}',headers={self._session:self._token})
        data=processresponse.processresponse(response)
        if(data ): return data["roles"][self.roleID]