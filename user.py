import requests
import processresponse

class User:
    id:str #:User ID
    _token:str #:Bot token, used internally
    _session:str #:Bot token type, also used internally

    username:str #:User's name
    status:str #:User's status
    online: bool #:Whether or not the user is online

    profile: dict #:User's profile
    badges: int #:Bitfield of user's badges
    flags: int #:Enum of user's flags

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
        if(data):
            self.id=data["_id"]
            self.username=data["username"]
            if("bot" in data): self.bot=True
            if("bot" in data): self.owner=data["bot"]["owner"]
            if("profile" in data): self.profile=data["profile"]
            if("badges" in data): self.badges=data["badges"]
            if("flags" in data): self.flags=data["flags"]
            if("status" in data): self.status=data["status"]
            if("avatar" in data): self.avatar=data["avatar"]
            if("relations" in data): self.relations=data["relations"]
            if("relationship" in data): self.relationship=data["relationship"]
    #Todo: fetch user bio