import requests
import processresponse

class User:
    id:str #:User ID
    _token:str #:Bot token, used internally
    _session:str #:Bot token type, also used internally

    username:str #:User's name
    status:str #:User's status
    bot:bool #:Whether or not the user is a bot
    owner:str #:If user is a bot, the ID of the owner

    avatar:dict #:User avatar
    relations:list #:User relations

    relationship:str #:User relationship

    def __init__(self, userID, token, sessiontype):
        self._token = token
        self.id = userID
        if sessiontype=='bot':
            self._session="x-bot-token"
        else:
            self._session='x-session-token'
        response=requests.get(f'https://api.revolt.chat/users/{self.id}',headers={self._session:self._token})
        data=processresponse.processresponse(response)
        self._token=token
        self.id=data["_id"]
        self.username=data["username"]
        if("status" in data): self.status=data["status"]
        if("avatar" in data): self.avatar=data["avatar"]
        if("relations" in data and "relationship" in data):
          self.relations=data["relations"]
          self.relationship=data["relationship"]
    #Todo: fetch user bio