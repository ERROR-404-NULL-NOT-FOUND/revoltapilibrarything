import requests

async def sendmessage(channelID,data,token,sessiontype,raw=False):
    if sessiontype=='bot':
        session='x-bot-token'
    else:
        session='x-session-token'
    if raw:
        response=requests.post(f'https://api.revolt.chat/channels/{channelID}/messages',headers={session:token}, data=data)
    else:
        response=requests.post(f'https://api.revolt.chat/channels/{channelID}/messages',headers={session:token}, data='{'+f'"content":"{data}"'+'}')
    if response.status_code==404:
        return 404
    elif response.status_code==403:
        return 403
    elif response.status_code==200:
        return 0
    else:
        print(f'Unknown status code, "{response.status_code}"')


async def fetchmessages(channelID,token,sessiontype,limit:int):
        if sessiontype=='bot':
            session='x-bot-token'
        else:
            session='x-session-token'
        data=""
        data=requests.get(f'https://api.revolt.chat/channels/{channelID}/messages',headers={session:token})
        if data.status_code==200:
            return data
        elif data.status_code==403:
            print("Permission denied")
        elif data.status_code==404:
            print("Invalid channel")
        else:
            print(f'Unknown status code, "{data.status_code}"')

import json

class Message:
  id: str
  content: str
  author: str
  channel: str
  replies: list
  embeds: list
  masquerade: dict

  def __init__(self, message):
    message = json.loads(message)
    self.id = message["_id"]
    self.author = message["author"]
    self.content = message["content"]
    self.channel = message["channel"]
    if("replies" in message): self.replies = message["replies"]
    if("embeds" in message): self.embeds = message["embeds"]
    if("masquerade" in message): self.masquerade = message["masquerade"]