from typing import Final
import os
from dotenv import load_dotenv
from discord import BotIntegration, Intents, Client, Message
from discord.ext import commands, tasks
from responses import get_response
import asyncio
from datetime import timedelta, time, datetime

gm_channel_id = 1211806140112052254

# LOAD TOKEN FROM OTHER FILE
TOKEN = 'TOKEN'

#set up bot client
intents: Intents = Intents.default()
intents.message_content = True 
client: Client = Client(intents=intents)





#handling the startup of the bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running')

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    

    print(f'[{channel}] {username}: "{user_message}"')
    lowered: str = user_message.lower()

    if username  == 'iceyical':
         await message.add_reaction('🇵🇭')

    if channel == 'schmevinator':
        schmevinator_input = lowered.split(' ')
        schmevinator_out = []
        for i in schmevinator_input:
            for j in range(len(i)):
                if i[j] == "a" or i[j] == "e" or i[j] == "i" or i[j] == "o" or i[j] == "u" or i[j] == "y":
                    schmevinator_out.append('schm' + i[j:])
                    break
                elif i[j] == "<":
                    user = message.guild.get_member(int(i[2:19]))
                    for k in user:
                        if k == "a" or k == "e" or k == "i" or k == "o" or k == "u" or k == "y":
                            schmevinator_out.append('schm' + i[j:])
                            break
                    break

        schmoutput = ' '.join(schmevinator_out)
        await message.channel.send(schmoutput)
    elif "hello" in lowered:
        await message.channel.send(f'hello {username}')
    elif "gm" in lowered or "good morning" in lowered:
        await message.channel.send(f'Good Morning {username}')
        if channel == 'tight':
            awake_role = message.guild.get_role(1213310424032747530)
            await message.author.add_roles(awake_role, reason='girish', atomic=True)
    elif "gn" in lowered or "good night" in lowered:
        await message.channel.send(f'Good Night {username}')
        if channel == 'tight':
            awake_role = message.guild.get_role(1213310424032747530)
            await message.author.remove_roles(awake_role, reason='girish', atomic=True)
    elif "girish" in lowered:
        await message.channel.send('Prabu')
    #elif '<@' in lowered:
    #    await message.channel.send('')
    elif "devin" in lowered or 'kevin' in lowered:
        await message.channel.send('Schmevin')
    elif "<@" in lowered:
        print(lowered)
        input = lowered.split(' ')
        out = []
        awake_role = message.guild.get_role(1213310424032747530)
        for i in input:
            if i[0] == "<": 
                user_id = int(i[2:19])  
                user = message.guild.get_member(user_id)
                if user:
                    if awake_role in user.roles:
                        out.append(i)
        print(out)
        if out:
            out = ' '.join(out)
            await message.reply(f'{out} is/are not awake')







# WHEN = time(18, 0, 20)  # 6:00 AM
# channel_id = 1211806140112052254

# async def called_once_a_day():  # Fired every day
#     await client.wait_until_ready()  # Make sure your guild cache is ready so the channel can be found via get_channel
#     channel = client.get_channel(channel_id) # Note: It's more efficient to do bot.get_guild(guild_id).get_channel(channel_id) as there's less looping involved, but just get_channel still works fine
#     await channel.send("Good Morning Everyone! Send a GM message to unlock the server")
#     admin_role = guild.get_role(1211807579416829982)
#     for guild in client.guilds:
#         for member in client.guilds:
#             await member._remove_role(admin_role, reason="It's Morning", atomic=True)

# async def background_task():
#     now = datetime.utcnow()
#     if now.time() > WHEN:  # Make sure loop doesn't start after {WHEN} as then it will send immediately the first time as negative seconds will make the sleep yield instantly
#         tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
#         seconds = (tomorrow - now).total_seconds()  # Seconds until tomorrow (midnight)
#         await asyncio.sleep(seconds)   # Sleep until tomorrow and then the loop will start 
#     while True:
#         now = datetime.utcnow() # You can do now() or a specific timezone if that matters, but I'll leave it with utcnow
#         target_time = datetime.combine(now.date(), WHEN)  # 6:00 PM today (In UTC)
#         seconds_until_target = (target_time - now).total_seconds()
#         await asyncio.sleep(seconds_until_target)  # Sleep until we hit the target time
#         await called_once_a_day()  # Call the helper function that sends the message
#         tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
#         seconds = (tomorrow - now).total_seconds()  # Seconds until tomorrow (midnight)
#         await asyncio.sleep(seconds)   # Sleep until tomorrow and then the loop will start a new iteration




#main entry point
def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()
