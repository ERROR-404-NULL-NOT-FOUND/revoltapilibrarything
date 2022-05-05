import json
import aiohttp
import asyncio
from typing import Callable

import message

class Connection:
  _token: str
  onMessage: Callable=None #:Function for on message
  onLogin: Callable=None #:Function for on login
  onMessageDelete: Callable=None #:Function for on message delete

  def __init__(self,token):
    self._token=token

  async def eventProcessor(self,socket):
    async for msg in socket:
      msg=json.loads(str(msg.data))
      if(msg["type"]=="Message" and self.onMessage!=None):
        asyncio.create_task(self.onMessage(message.Message(json.dumps(msg))))
      elif(msg["type"]=="Authenticated" and self.onLogin!=None):
        asyncio.create_task(self.onLogin())
      elif(msg["type"]=="MessageDelete" and self.onMessageDelete!=None):
        asyncio.create_task(self.onMessageDelete(msg))

  async def connect(self):
    "Establish websocket connection"
    async with aiohttp.ClientSession() as session:
      async with session.ws_connect("wss://ws.revolt.chat") as socket:
        await socket.send_str(json.dumps({
          "type":"Authenticate",
          "token":self._token
        }))
        await self.eventProcessor(socket)


  def addEventListener(self, type: str, function: Callable):
    """Add a function to run when an event is received
    Available values for 'type':
    "message"
    "messagedelete"
    "login"
    """
    if(type=="message"): self.onMessage=function
    elif(type=="login"): self.onLogin=function
    elif(type=="messagedelete"): self.onMessageDelete=function
