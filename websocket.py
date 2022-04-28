import json
import aiohttp

class Connection:
  token: str
  onMessage=None
  onLogin=None
  onMessageDelete=None
  
  def __init__(self,token):
    self.token=token
    
  async def eventProcessor(self,socket):
    async for msg in socket:
      msg=json.loads(str(msg.data))
      if(msg["type"]=="Message" and self.onMessage!=None):
        await self.onMessage(msg)
      elif(msg["type"]=="Authenticated" and self.onLogin!=None):
        await self.onLogin()
      elif(msg["type"]=="MessageDelete" and self.onMessageDelete!=None):
        await self.onMessageDelete(msg)

  async def connect(self):
    async with aiohttp.ClientSession() as session:
      async with session.ws_connect("wss://ws.revolt.chat") as socket:
        await socket.send_str(json.dumps({
          "type":"Authenticate",
          "token":self.token
        }))
        await self.eventProcessor(socket)


  def addEventListener(self, type: str, function):
    if(type=="message"): self.onMessage=function
    elif(type=="login"): self.onLogin=function
    elif(type=="messagedelete"): self.onMessageDelete=function
    