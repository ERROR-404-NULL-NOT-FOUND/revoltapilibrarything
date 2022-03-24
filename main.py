import client 
import asyncio
async def main():
    
    token="token"
    sessiontype='bot'
    
    bot=client.Client(token, sessiontype)
    #past this you'll have to use your intellisense

asyncio.run(main())