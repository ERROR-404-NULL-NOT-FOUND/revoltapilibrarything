import message

class Channel:
    id=""
    token=""
    sessiontype=""
    info={}
    
    def __init__(self,id,token,sessiontype):
        self.id=id
        self.token=token
        self.sessiontype=sessiontype
    
    async def sendmessage(self,data):
        await message.sendmessage(channelID,data,self.token,self.sessiontype)
    
    async def fetchmessages(self,limit:int):
       return await message.fetchmessages(self.id,self.token,self.sessiontype,limit)