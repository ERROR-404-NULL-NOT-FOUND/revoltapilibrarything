import client 
import asyncio
async def main():
    
    token="token"
    sessiontype='bot'
    bot=client.Client(token, sessiontype)
    serverid="server id"
    channelid="channel id"
    userid="userid"
    server=bot.fetchserver(serverid)
    channel=bot.fetchchannel(channelid)
    user=bot.fetchchannel(userid)
    print(await server.fetchdata())
    print(await channel.fetchdata())
    print(await user.fetchdata())
asyncio.run(main())