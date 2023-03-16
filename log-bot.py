import discord
import asyncio
from discord.ext import commands
from datetime import datetime
import math
from config import *

bot = commands.Bot(command_prefix=PREFIX, intents= discord.Intents.all())
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="you"))
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))
    
async def check_user_presence():
    user_id = int(USER_ID)
    guild_id = int(GUILD_ID)
    guild = bot.get_guild(guild_id)
    user = guild.get_member(user_id)
    counter_offline = 0
    counter_online_time = 0
    check_being_online = False
    check_online = False
    while True:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        if user.status == discord.Status.online or user.status == discord.Status.do_not_disturb or user.status == discord.Status.idle:
            if check_being_online == False:
                print(f"{user.display_name} is online right now. | {dt_string}")
                check_being_online = True
            counter_online_time += 1
            check_online = True
        else:
            check_being_online = False
            if check_online == True:
                if counter_online_time > 3599:
                    hours = math.floor(counter_online_time / 3600)
                    counter_online_time = counter_online_time - hours
                    minutes = math.floor(counter_online_time / 60)
                    counter_online_time = counter_online_time - minutes
                    seconds = counter_online_time
                    print(f"{user.display_name} was online for {hours} hours, {minutes} minutes and {seconds} seconds.")
                elif counter_online_time > 59:
                    minutes = math.floor(counter_online_time / 60)
                    counter_online_time = counter_online_time - minutes
                    seconds = counter_online_time
                    print(f"{user.display_name} was online for {minutes} minutes and {seconds} seconds.")
                else:
                    print(f"{user.display_name} was online for {counter_online_time} seconds.")
                check_online = False
            if counter_offline == 0:
                print(f"{user.display_name} is offline.")
                counter_offline = 60
            counter_offline -= 1
            counter_online_time = 0
        await asyncio.sleep(1) # Wait for 1 seconds before checking again

@bot.command()
async def s(ctx):
    bot.loop.create_task(check_user_presence())

bot.run(TOKEN)