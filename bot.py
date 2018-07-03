from chatterbot import ChatBot
import logging
import discord
from discord.ext.commands import Bot
import random

# Enter your bot's token obtained from discord.
TOKEN = ' YOUR TOKEN HERE '

client = discord.Client()

chatbot = ChatBot(
    "Iris",
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
    #readonly = True, <-- This stops the bot learning from your conversations 
)
'''
You can train your bot with your own .yml file

chatbot.train(
    'chatterbot.corpus.custom.myown'
)
'''
# Enable info level logging
logging.basicConfig(level=logging.INFO)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    elif message.content.startswith("!8ball"):
        possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
        ]
        await client.send_message(message.channel, random.choice(possible_responses) + ", " + message.author.mention)


    else:
        response = chatbot.get_response(message.content)
        print(response)
        await client.send_message(message.channel, response)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
