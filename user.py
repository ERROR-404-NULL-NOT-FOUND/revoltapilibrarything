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
        
        if sessiontype=='bot':
            self.session="x-bot-token"
        else:
            self.session='x-session-token'
        data=""
        response=requests.get(f'https://api.revolt.chat/users/{self.id}',headers={self.session:self.token})
        data=processresponse.processresponse(response) 

        self.token=token
        self.id=userID
        self.username=data["username"]
        self.status=data["status"]
        self.avatar=data["avatar"]
        self.relations=data["relations"]
        self.relationship=data["relationship"]
    #Todo: fetch user bio