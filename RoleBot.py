import discord
import os

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.invisible,activity = discord.Game('Game Selector Bot.'))

#When emoting a certain emote, gain that role.
@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 836987061901721640:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        if payload.emoji.name == "0️⃣":
            role = discord.utils.get(guild.roles, name="destiny")
        #print(payload.emoji.name)
        elif payload.emoji.name == "1️⃣":
            role = discord.utils.get(guild.roles, name="among us")
        elif payload.emoji.name == "2️⃣":
            role = discord.utils.get(guild.roles, name="apex")
        elif payload.emoji.name == "3️⃣":
            role = discord.utils.get(guild.roles, name="csgo")
        elif payload.emoji.name == "4️⃣":
            role = discord.utils.get(guild.roles, name="deep rock")
        elif payload.emoji.name == "5️⃣":
            role = discord.utils.get(guild.roles, name="league")
        elif payload.emoji.name == "6️⃣":
            role = discord.utils.get(guild.roles, name="minecraft")
        elif payload.emoji.name == "7️⃣":
            role = discord.utils.get(guild.roles, name="terraria")
        elif payload.emoji.name == "8️⃣":
            role = discord.utils.get(guild.roles, name="tft")
        elif payload.emoji.name == "9️⃣":
            role = discord.utils.get(guild.roles, name="valorant")
        elif payload.emoji.name == ":Booba:":
            role = discord.utils.get(guild.roles, name="nsfw")
        else:
            role = discord.utils.get(guild.roles, name="")
        if role is not None:
            #print(payload.emoji.name)
            member = payload.member
            if member is not None:
                await member.add_roles(role)

#Why is this not working?
@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 836987061901721640:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)

        #Test use. grab emoji
        print(payload.emoji.name)

        if payload.emoji.name == "0️⃣":
            role = discord.utils.get(guild.roles, name="destiny")
        elif payload.emoji.name == "1️⃣":
            role = discord.utils.get(guild.roles, name="among us")
        elif payload.emoji.name == "2️⃣":
            role = discord.utils.get(guild.roles, name="apex")
        elif payload.emoji.name == "3️⃣":
            role = discord.utils.get(guild.roles, name="csgo")
        elif payload.emoji.name == "4️⃣":
            role = discord.utils.get(guild.roles, name="deep rock")
        elif payload.emoji.name == "5️⃣":
            role = discord.utils.get(guild.roles, name="league")
        elif payload.emoji.name == "6️⃣":
            role = discord.utils.get(guild.roles, name="minecraft")
        elif payload.emoji.name == "7️⃣":
            role = discord.utils.get(guild.roles, name="terraria")
        elif payload.emoji.name == "8️⃣":
            role = discord.utils.get(guild.roles, name="tft")
        elif payload.emoji.name == "9️⃣":
            role = discord.utils.get(guild.roles, name="valorant")
        elif payload.emoji.name == ":Booba:":
            role = discord.utils.get(guild.roles, name="nsfw")
        else:
            role = discord.utils.get(guild.roles, name="")
        if role is not None:
            if member is not None:
                await member.remove_roles(role)

client.run(os.environ.get('DISCORD_TOKEN'))