import message
import channel
import user
import server

class Client:
    token=""
    sessiontype=""
    
    def __init__(self,token, sessiontype):
        self.token=token
        self.sessiontype=sessiontype
    
    async def sendmessage(self,channelID,data):
        await message.sendmessage(channelID,data,self.token,self.sessiontype)
    
    def fetchchannel(self,channelID):
        return channel.Channel(channelID,self.token,self.sessiontype)
    
    def fetchuser(self, userID):
        return user.User(userID,self.token, self.sessiontype)
    
    def fetchserver(self, serverID):
        return server.Server(serverID,self.token,self.sessiontype)