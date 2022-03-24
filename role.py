from concurrent.futures import process
import requests
import json
import processresponse
class Role:
    roleID=""
    token=""
    session=""
    name=""
    serverID=""
    def __init__(self,roleID,serverID,token,session):
        self.roleID=roleID
        self.serverID=serverID
        self.token=token
        self.session=session
        response=requests.get(f'https://api.revolt.chat/servers/{serverID}',headers={session:token})
        data=processresponse.processresponse(response)
        self.name=data["roles"][roleID]["name"]
    
    async def fetchinfo(self):
        response=requests.get(f'https://api.revolt.chat/servers/{self.serverID}',headers={self.session:self.token})
        data=processresponse.processresponse(response)
        return data["roles"][self.roleID]