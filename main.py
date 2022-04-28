import client 
import asyncio
token="token"
sessiontype='bot'
bot=client.Client(token, sessiontype)

async def onMessage(message):
  print(f'{bot.fetchuser(message["author"]).username}:{message["content"]}')
  if(not message["author"]==bot.user.id):
    await bot.sendmessage(message["channel"],"REPLY")
async def onLogin():
  print(f'Logged in as {bot.user.username}')

async def main():
    bot.addEventListener("message",onMessage)
    bot.addEventListener("login", onLogin)
    await bot.connect()
    #past this you'll have to use your intellisense

asyncio.run(main())