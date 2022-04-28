import requests
import processresponse

class User:
    id=str
    token=str
    session=str

    username=str
    status=str
    bot=bool
    owner=str

    avatar=dict
    relations=list

    relationship=str

    def __init__(self, userID, token, sessiontype):
        self.token = token
        self.id = userID
        if sessiontype=='bot':
            self.session="x-bot-token"
        else:
            self.session='x-session-token'
        response=requests.get(f'https://api.revolt.chat/users/{self.id}',headers={self.session:self.token})
        data=processresponse.processresponse(response)
        self.token=token
        self.id=data["_id"]
        self.username=data["username"]
        self.status=data["status"]
        self.avatar=data["avatar"]
        if("relations" in data and "relationship" in data):
          self.relations=data["relations"]
          self.relationship=data["relationship"]
    #Todo: fetch user bio