import requests
import processresponse

async def sendmessage(channelID,data,token,sessiontype,raw=False):
    "Sends a message in the supplied channel"
    if sessiontype=='bot':
        session='x-bot-token'
    else:
        session='x-session-token'
    if raw:
        response=requests.post(f'https://api.revolt.chat/channels/{channelID}/messages',headers={session:token}, data=data)
    else:
        response=requests.post(f'https://api.revolt.chat/channels/{channelID}/messages',headers={session:token}, data='{'+f'"content":"{data}"'+'}')
    return processresponse.processresponse(response)


async def fetchmessages(channelID,token,sessiontype,limit:int):
        "Fetches messages from the supplied channel"
        if sessiontype=='bot':
            session='x-bot-token'
        else:
            session='x-session-token'
        data=""
        data=requests.get(f'https://api.revolt.chat/channels/{channelID}/messages',headers={session:token})
        return processresponse.processresponse(data)

import json

class Message:
  id: str #:Message ID
  content: str #:Message content
  author: str #:Message author ID
  channel: str #:Message channel
  replies: list #:Message replies
  embeds: list #:Message embeds
  masquerade: dict #:Message masquerade
  attachments: list #:Message attachments

  def __init__(self, message):
    message = json.loads(message)
    self.id = message["_id"]
    self.channel = message["channel"]
    self.author = message["author"]
    if("content" in message): self.content = message["content"]
    if("replies" in message): self.replies = message["replies"]
    if("embeds" in message): self.embeds = message["embeds"]
    if("masquerade" in message): self.masquerade = message["masquerade"]
    if("attachments" in message): self.attachments = message["attachments"]