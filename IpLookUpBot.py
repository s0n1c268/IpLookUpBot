#=================Sonic the Cyber Warrior============================
#Made for Educational Purposes, not responsible for your actions!!!!

import discord
from discord.ext import commands
import socket
import pygeoip
import requests

#===================Sonic the Cyber Warrior======================

bot = commands.Bot(command_prefix='?')
bot.remove_command('help')
token = ''

#======================Sonic the Cyber Warrior====================

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Ip LookUp | use prefix: ?"))
    print('Bot is ready.')

gip = pygeoip.GeoIP(str('GeoLiteCity.dat'))

array1 = []

class iplookup():
    async def lookup_class(self, *, arg):
        dang.clear()
        x = str(input())
        y = array1.append(x)
        return '{}'.format(y,arg)

@bot.command()
async def lookup(ctx, *, lol=str(iplookup)):
    res = gip.record_by_addr(lol)
    for key,val in res.items():
        await ctx.send('%s : %s' % (key,val))

@bot.command()
async def ip(ctx, *, question):
    b = socket.gethostbyname(question)
    await ctx.send(f'{question} ip address: {b}')

#=======================Sonic the Cyber Warrior=====================

bot.run(token)