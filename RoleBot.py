import discord
import os

client = discord.Client()

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 836987061901721640:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild.id, client.guilds)

        if payload.emoji.name == "regional_indicator_l":
            role = discord.utils.get(guild.roles, name="league")
        elif payload.emoji.name == "regional_indicator_v":
            role = discord.utils.get(guild.roles, name="valorant")
        elif payload.emoji.name == "regional_indicator_c":
            role = discord.utils.get(guild.roles, name="csgo")
        elif payload.emoji.name == "regional_indicator_a":
            role = discord.utils.get(guild.roles, name="apex")
        elif payload.emoji.name == "regional_indicator_u":
            role = discord.utils.get(guild.roles, name="among us")
        elif payload.emoji.name == "regional_indicator_m":
            role = discord.utils.get(guild.roles, name="minecraft")
        elif payload.emoji.name == "regional_indicator_t":
            role = discord.utils.get(guild.roles, name="terraria")
        elif payload.emoji.name == "regional_indicator_f":
            role = discord.utils.get(guild.roles, name="tft")
        elif payload.emoji.name == "regional_indicator_d":
            role = discord.utils.get(guild.roles, name="deep rock")
        
        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.add_roles(role)

@client.event
async def on_raw_reaction_remove(payload):
    message_id = payload.message_id
    if message_id == 836987061901721640:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild.id, client.guilds)

        if payload.emoji.name == "regional_indicator_l":
            role = discord.utils.get(guild.roles, name="league")
        elif payload.emoji.name == "regional_indicator_v":
            role = discord.utils.get(guild.roles, name="valorant")
        elif payload.emoji.name == "regional_indicator_c":
            role = discord.utils.get(guild.roles, name="csgo")
        elif payload.emoji.name == "regional_indicator_a":
            role = discord.utils.get(guild.roles, name="apex")
        elif payload.emoji.name == "regional_indicator_u":
            role = discord.utils.get(guild.roles, name="among us")
        elif payload.emoji.name == "regional_indicator_m":
            role = discord.utils.get(guild.roles, name="minecraft")
        elif payload.emoji.name == "regional_indicator_t":
            role = discord.utils.get(guild.roles, name="terraria")
        elif payload.emoji.name == "regional_indicator_f":
            role = discord.utils.get(guild.roles, name="tft")
        elif payload.emoji.name == "regional_indicator_d":
            role = discord.utils.get(guild.roles, name="deep rock")
        
        if role is not None:
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if member is not None:
                await member.remove_roles(role)

client.run(os.environ.get('DISCORD_TOKEN'))