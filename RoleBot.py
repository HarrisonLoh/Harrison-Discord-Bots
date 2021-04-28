import discord
import os

client = discord.Client()

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 836987061901721640:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        print(payload.emoji.name == "v")
        if payload.emoji.name == "l":
            role = discord.utils.get(guild.roles, name="league")
        elif payload.emoji.name == "v":
            print("in v")
            role = discord.utils.get(guild.roles, name="valorant")
        elif payload.emoji.name == "c":
            role = discord.utils.get(guild.roles, name="csgo")
        elif payload.emoji.name == "a":
            role = discord.utils.get(guild.roles, name="apex")
        elif payload.emoji.name == "u":
            role = discord.utils.get(guild.roles, name="among us")
        elif payload.emoji.name == "m":
            role = discord.utils.get(guild.roles, name="minecraft")
        elif payload.emoji.name == "t":
            role = discord.utils.get(guild.roles, name="terraria")
        elif payload.emoji.name == "f":
            role = discord.utils.get(guild.roles, name="tft")
        elif payload.emoji.name == "d":
            role = discord.utils.get(guild.roles, name="deep rock")
        else:
            role = discord.utils.get(guild.roles, name="")
        if role is not None:
            member = payload.member
            print("Done")
            print(member)
            if member is not None:
                await member.add_roles(role)
                print("Await Done")


@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 836987061901721640:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

        if payload.emoji.name == "l":
            role = discord.utils.get(guild.roles, name="league")
        elif payload.emoji.name == "v":
            role = discord.utils.get(guild.roles, name="valorant")
        elif payload.emoji.name == "c":
            role = discord.utils.get(guild.roles, name="csgo")
        elif payload.emoji.name == "a":
            role = discord.utils.get(guild.roles, name="apex")
        elif payload.emoji.name == "u":
            role = discord.utils.get(guild.roles, name="among us")
        elif payload.emoji.name == "m":
            role = discord.utils.get(guild.roles, name="minecraft")
        elif payload.emoji.name == "t":
            role = discord.utils.get(guild.roles, name="terraria")
        elif payload.emoji.name == "f":
            role = discord.utils.get(guild.roles, name="tft")
        elif payload.emoji.name == "d":
            role = discord.utils.get(guild.roles, name="deep rock")
        else:
            role = discord.utils.get(guild.roles, name="")
        if role is not None:
            member = payload.member
            print("Done")
            if member is not None:
                await member.remove_roles(role)
                print("Await Done")

client.run(os.environ.get('DISCORD_TOKEN'))