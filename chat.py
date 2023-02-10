import discord
import random
import copy
import sys
import requests
from time import sleep

TOKEN = 'OTUzOTQzNjQyMTY5NTQwNjU4.YjL7Pw.YjP3hMMHpmI64b0qcjsr5wlwrSY'
SUB = 'https://www.reddit.com/r/worldnews/comments/'




client = discord.Client()


# The on_ready function prints a message to the console indicating that the bot has started, 
# and the on_message function is triggered every time a message is sent in the Discord server. 
# The function processes the incoming message and based on the content, it either sends a response back to the General channel or
# posts news links from r/worldnews. 

@client.event
async def on_ready():
    print('Started {0.user}'.format(client))
   



@client.event
async def on_message(message):

    temp = 0
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username} : {user_message} ({channel})')


    if message.author == client.user:
        return

    if message.channel.name == 'general':
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'bye {username}')
            return
        
#         The !random command returns a random number to the user
        elif user_message.lower() == '!random':
            response = f'This is your random number :{random.randrange(1000000)}'
            await message.channel.send(response)
            return

#         !anywhere command can be used from any channel in the Discord server
    if user_message.lower() == '!anywhere':
        await message.channel.send('This can be used anywhere')
        return
    
#     using the requests library to get the latest posts from the subreddit, 
#     and checking if the post link is different from the previous one before posting it to the Discord channel.
    if user_message.lower() == '!news':
         while(1):
            sleep(10)
            subreddit = 'worldnews'
            limit = 1
            timeframe = 'hour' #hour, day, week, month, year, all
            listing = 'new' # controversial, best, hot, new, random, rising, top
            
            def get_reddit(subreddit,listing,limit,timeframe):
                try:
                    base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}'
                    request = requests.get(base_url, headers = {'User-agent': 'yourbot'})
                except:
                    print('An Error Occured')
                return request.json()
            # TEMP = ''
            r = get_reddit(subreddit,listing,limit,timeframe)
            post = r['data']['children']
            x = post[0]['data']['name'].split('_')[1]
            new = SUB+x
            print(f'new = {new}')
            print(f'temp = {temp}')
            if ( new != temp ):
                await message.channel.send(new)
                temp = new
    return

# @Client.event
# async def get_new()
 
    



client.run(TOKEN)
