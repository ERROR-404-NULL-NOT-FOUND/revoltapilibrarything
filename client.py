import message
import channel

class Client:
    token=""
    sessiontype=""
    
    def __init__(self,token, sessiontype):
        self.token=token
        self.sessiontype=sessiontype
    
    async def sendmessage(self,channelID,data):
        await message.sendmessage(channelID,data,self.token,self.sessiontype)
    
    def fetchchannel(self,channelID):
        return channel.Channel(channelID,self.sessiontype,self.token)