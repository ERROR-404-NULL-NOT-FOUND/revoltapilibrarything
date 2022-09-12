# This is an example program to show some of the functionality of the library


import client # imports from client.py
import asyncio 

token = "TOKEN HERE" 
sessiontype = 'bot'
bot = client.Client(token, sessiontype) # Initiates the client

async def onMessage(message):
    print(f'[{bot.fetchuser(message.author).username}]: {message.content}') # Logs a message 

    if message.content == "hello": # When the user sends 'hello' in a channel, the bot will reply with 'Hey, (User)'
        await bot.sendmessage(message.channel, f"Hello, {message.author.username}.")

    if message.content == "bye": 
        await bot.sendmessage(message.channel, f"Bye, {message.author.username}.")

async def onMessageDelete(message): # If a message is deleted, log it in the console with the message ID
    print(f'[{message["id"]}]: DELETED')

async def onLogin(): # When the bot logs in, post an alert in the onsole
    print(f'Logged in as {bot.user.username}')

async def main():
    bot.addEventListener("messagedelete", onMessageDelete) # A listener for when a message is deleted
    bot.addEventListener("message", onMessage) # A listener for when a message is sent
    bot.addEventListener("login", onLogin) # A listener for when the bot comes online / logs in
    await bot.connect()

asyncio.run(main()) 