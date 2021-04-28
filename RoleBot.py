import discord
import os

client = discord.Client()

@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 836987061901721640:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)

        print(type(payload.emoji.name))
        print(payload.emoji.name)
        print(type("v"))
        if payload.emoji.name == "🇱":
            role = discord.utils.get(guild.roles, name="league")
        elif payload.emoji.name == "🇻":
            role = discord.utils.get(guild.roles, name="valorant")
        elif payload.emoji.name == "🇨":
            role = discord.utils.get(guild.roles, name="csgo")
        elif payload.emoji.name == "🇦":
            role = discord.utils.get(guild.roles, name="apex")
        elif payload.emoji.name == "🇺":
            role = discord.utils.get(guild.roles, name="among us")
        elif payload.emoji.name == "🇲":
            role = discord.utils.get(guild.roles, name="minecraft")
        elif payload.emoji.name == "🇹":
            role = discord.utils.get(guild.roles, name="terraria")
        elif payload.emoji.name == "🇫":
            role = discord.utils.get(guild.roles, name="tft")
        elif payload.emoji.name == "🇩":
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
        # guild_id = payload.guild_id
        # guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
        # member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)

        # if payload.emoji.name == "🇱":
        #     role = discord.utils.get(guild.roles, name="league")
        # elif payload.emoji.name == "🇻":
        #     role = discord.utils.get(guild.roles, name="valorant")
        # elif payload.emoji.name == "🇨":
        #     role = discord.utils.get(guild.roles, name="csgo")
        # elif payload.emoji.name == "🇦":
        #     role = discord.utils.get(guild.roles, name="apex")
        # elif payload.emoji.name == "🇺":
        #     role = discord.utils.get(guild.roles, name="among us")
        # elif payload.emoji.name == "🇲":
        #     role = discord.utils.get(guild.roles, name="minecraft")
        # elif payload.emoji.name == "🇹":
        #     role = discord.utils.get(guild.roles, name="terraria")
        # elif payload.emoji.name == "🇫":
        #     role = discord.utils.get(guild.roles, name="tft")
        # elif payload.emoji.name == "🇩":
        #     role = discord.utils.get(guild.roles, name="deep rock")
        # else:
        #     role = discord.utils.get(guild.roles, name="")
        # if role is not None:
        #     # member = payload.user_id
        #     print(member)
        #     print("Done")
        #     if member is not None:
        #         await member.remove_roles(role)
        #         print("Await Done")
        
        #get the server name from the payload
        guild = client.get_guild(payload.guild_id)
        # payload.member is not availible for REACTION_REMOVE event type
        member = guild.get_member(payload.user_id)

        #Debugging
        Post_Message = "Remove(1/3) - Message ID matches."
        Post_Message = Post_Message+"'"+str(guild)+"'"+" is the Guild ID."
        Post_Message = Post_Message+"'"+str(member)+"'"+" is the Member ID."
        print(str(Post_Message))

        # if the name of the reaction emoji is "League" theen assign the "League bois discord role
        if payload.emoji.name == "🇦":
            role = discord.utils.get(guild.roles, name="apex")

        else:
            # set role variable to the name of the reaction emoji
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:


            #Debugging
            print("Remove(2/3) - Attempting to remove Role...")


            if member is not None:
                #remove the role
                await member.remove_roles(role)
                #Debugging
                print("Remove(3/3) - Role has been removed.")
            else:
                print("Member not found.")
                print("Member returned is: "+str(member))
        else:
            print("Role not found.")
            print("Role Returned is: "+str(role))

client.run(os.environ.get('DISCORD_TOKEN'))