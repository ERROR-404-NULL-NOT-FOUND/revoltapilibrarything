import message
import channel
import user
import server
import role
import websocket

class Client:
    _token: str
    _sessiontype: str
    connection: websocket.Connection #:Websocket connection
    user: user.User #:User agent

    def __init__(self, token, sessiontype):
      self._token=token
      self._sessiontype=sessiontype
      self.connection=websocket.Connection(token)
      self.user=user.User('@me',token,sessiontype)

    async def connect(self):
      "Connect to the websocket"
      await self.connection.connect()

    def addEventListener(self,type,function):
      """Adds a function to run on the event.
      Available values for 'type':
      "message"
      "messagedelete"
      "login"
      """
      self.connection.addEventListener(type,function)

    async def sendmessage(self,channelID,data):
      "Sends a message in the supplied channel"
      await message.sendmessage(channelID,data,self._token,self._sessiontype)

    def fetchchannel(self,channelID):
        "Fetches a channel from ID"
        return channel.Channel(channelID,self._token,self._sessiontype)

    def fetchuser(self, userID):
        "Fetches a user using the given ID"
        return user.User(userID,self._token, self._sessiontype)

    def fetchserver(self, serverID):
        "Fetches a server using the given ID"
        return server.Server(serverID,self._token,self._sessiontype)

    def fetchmember(self, serverID, userID):
        "Fetches member data using the supplied server ID and user ID"
        return server.Member(serverID,userID,self._token, self._sessiontype)

    def fetchrole(self, serverID, roleID):
        "Fetches role data using the supplied server ID and role ID"
        return role.Role(roleID,serverID,self._token,self._sessiontype)