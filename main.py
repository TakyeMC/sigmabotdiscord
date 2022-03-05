import discord
import colorama
from colorama import Fore
import random
import os
from discord.ext import commands
import asyncio
client = commands.Bot(command_prefix='.')
token = 'BOT_TOKEN'



#Every code for bot commands here start with "@client.command()"
#basic commands
@client.command(help = 'idk... the bot just introduces itself')
async def introduction(ctx):
  await ctx.channel.send('I am sigma bot')

@client.command(help = 'imposter sus') 
async def sus(ctx):
  await ctx.channel.send('When the imposter is sus')

@client.command(help = 'I have been laughing to amogus since the incident')
async def amogus(ctx):
  await ctx.channel.send('I have been laughing to amogus since the incident')

#commands with 'random' properties and ability to copy a user's message
@client.command(name='8ball', help = 'Ask the magic 8ball about stuff... idk')
async def _8ball(ctx, *, question):
  responses = ['Maybe... Maybe',
               'Probably',
               'It is possible',
               'Sigma says yes B)',
               'Maybe nah',
               'Probably nah',
               'Sigma says no B)',
               'Fuck off',
               'Idk.. maybe?',]
  await ctx.channel.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command(help='tells puns')
async def puns(ctx):
  puns = ['The sus pasta could be an *impasta*',
  'Gonna go to Finland to *finnish* what i started',
  'Bees can sometimes *bee* annoying', 'a cute door is really *a-door-able*']
  await ctx.channel.send(f'pun: {random.choice(puns)}')

@client.command(help = 'Just imagine')
async def imagine(ctx, *, sentence):
  await ctx.channel.send(f'I cant even imagine {sentence}')

#experimental
@client.command(help='experimental')
async def calc(ctx, operation:str):
  await ctx.channel.send(eval(operation))

#bonus commands
@client.command(help = 'Tells the creator of this bot')
async def creator(ctx):
    try:
        user = await client.fetch_user(YOUR_ID)
        await ctx.send(f'Creator: {user.mention}')
    except:
        user = 'Takye#6969'
        await ctx.send(f'Creator: ***{user}***')

@client.command(help = "Tells the server details")
async def server(ctx):
    owner=str(ctx.guild.owner)
    region = str(ctx.guild.region)
    guild_id = str(ctx.guild.id)
    memberCount = str(ctx.guild.member_count)
    icon = str(ctx.guild.icon_url)
    desc=ctx.guild.description
    
    embed = discord.Embed(
        title=ctx.guild.name + " Server Information",
        description=desc,
        color=discord.Color.red()
        )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=guild_id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)

    await ctx.send(embed=embed)

    membera=[]
    async for member in ctx.guild.fetch_members(limit=150) :
        await ctx.send('Name : {}\t Status : {}\n Joined at {}'.format(member.display_name,str(member.status),str(member.joined_at)))

#console related stuff
@client.event
async def on_ready():
    print(Fore.BLUE + 'System is online')
    print(Fore.RED + 'Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(Fore.WHITE + '------')

 
    
client.run(token)
