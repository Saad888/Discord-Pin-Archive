import discord
from pyshorteners import Shortener
from datetime import datetime, timedelta

with open("token.txt", "r") as file:
    TOKEN = file.read()

with open('bitly key.txt', 'r') as file:
    AUTHKEY = file.read()



client = discord.Client()
global TARGET
global CHANNELIN


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)

    if message.content.startswith('!TARGET'):
        global TARGET 
        TARGET = message.channel
        msg = 'This is now target channel'
        await message.channel.send(msg)

"""
    if message.content.startswith('!PINS'):
        msg = 'Grabbing pins'
        await message.channel.send(msg)
        await TARGET.send("-"*15)
        await TARGET.send(message.channel.name)
        await TARGET.send("-"*15)
        PINS = await message.channel.pins()
        async with TARGET.typing():
            for pin in PINS[::-1]:

                date = pin.created_at + timedelta(hours=-4)
                msg = "=====\n**{} [{} EST]**:".format(
                    pin.author.name,
                    date.strftime("%b %d, %Y %H:%M:%S")
                )
                await TARGET.send(msg)

                grab = pin.clean_content
                if len(grab) > 0:
                    await TARGET.send(pin.clean_content)

                att = pin.attachments
                if len(att) > 0:
                    for at in att:
                        URL = at.url
                        FileName = URL.split("/")[-1]
                        shortener = Shortener('Bitly', bitly_token=AUTHKEY)
                        shortURL = shortener.short(URL) + "#" + FileName
                        await TARGET.send(shortURL)
        msg = 'Jobs done'
        await message.channel.send(msg)

"""
    if message.content.startswith('!exit'):
        await message.channel.send("Fine I'll leave.")
        await client.logout()
"""
    if message.content.startswith('!I killed them. Not just the men.'):
        await message.channel.purge()
        await message.channel.send("But the women and children too.")
"""

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)