import message
import channel
import user
import server
import role
import websocket

class Client:
    token: str
    sessiontype: str
    connection: websocket.Connection
    user: user.User
    
    def __init__(self, token, sessiontype):
      self.token=token
      self.sessiontype=sessiontype
      self.connection=websocket.Connection(token)
      self.user=user.User('@me',token,sessiontype)

    async def connect(self):
      await self.connection.connect()

    def addEventListener(self,type,function):
      self.connection.addEventListener(type,function)
    
    async def sendmessage(self,channelID,data):
        await message.sendmessage(channelID,data,self.token,self.sessiontype)
    
    def fetchchannel(self,channelID):
        return channel.Channel(channelID,self.token,self.sessiontype)
    
    def fetchuser(self, userID):
        return user.User(userID,self.token, self.sessiontype)
    
    def fetchserver(self, serverID):
        return server.Server(serverID,self.token,self.sessiontype)
    
    def fetchmember(self, serverID, userID):
        return server.Member(serverID,userID,self.token, self.sessiontype)
    
    def fetchrole(self, serverID, roleID):
        return role.Role(roleID,serverID,self.token,self.sessiontype)