import discord
import os
from discord.ext import commands
from flask import Flask

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)
app = Flask(__name__)

@app.route('/')
def home():
    return '<pre>' + bot_output + '</pre>'

@bot.event
async def on_ready():
    global bot_output
    bot_output = f'Logged in as {bot.user.name}'
    print(bot_output)

@bot.event
async def on_message(message):
    if message.channel.name == 'introduction':
        if message.author.bot:
            return
        emoji = '<:ownboon:1112740466786566235>'
        await message.add_reaction(emoji)

my_secret = os.environ['TOKEN']
bot_output = ''

import threading
def run_flask():
    app.run(host='0.0.0.0', port=8080)

flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

bot.run(my_secret)
