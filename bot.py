'''
MIT License
Copyright (c) 2017 Aarrow7
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import discord
import os
from discord.ext import commands


bot = commands.Bot(command_prefix='-', description="A fortnite server bot made by Aarrow7")
bot.remove_command("help")

@bot.event
async def on_ready():
  print("I'm ready to play Fortnite")
  await bot.change_presence(game=discord.Game(name='Fortnite: Battle Royale'))
  
  
@bot.command()
async def serverinfo(ctx):
  await ctx.send("Fortnite Battle Arena is a server for discussing stuff about Fortnite: Battle Royale, a game created by Epic Games. We here, will give you the information regarding the game, updates and much more! You can even view your fortnite stats using this bot! Great to have you here, enjoy!")
  
bot.run(os.environ.get("TOKEN"))
