import client 
import asyncio
async def main():
    
    token="S9WfSsrJ9s4J0hqpLFy63HBO2gDTVKXRCbPbnJ4WNKBZohgSDgsrpTVzh0q5JdkF"
    sessiontype='bot'
    bot=client.Client(token, sessiontype)
    channelid="01FH65V408XWSB0VKR5GZYQ9K7"
    channel=bot.fetchchannel(channelid)
    await channel.sendmessage('{"content":"test"}')
    await bot.sendmessage(channelid,'{"content":"test"}')
asyncio.run(main())