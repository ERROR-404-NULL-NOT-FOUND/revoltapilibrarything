import requests
async def sendmessage(channelID,data,token,sessiontype):
    if sessiontype=='bot':
        session='x-bot-token'
    else:
        session='x-session-token'
    response=requests.post(f'https://api.revolt.chat/channels/{channelID}/messages',headers={session:token}, data=data)
    if response.status_code==404:
        print("Invalid channel")
    elif response.status_code==403:
        print("Permission denied")
    elif response.status_code==200:
        print("Message sent")
    else:
        print("There was an error sending the message, possibly a lack of an internet connection")
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