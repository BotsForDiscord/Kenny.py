import datetime
import random
import urllib
import json
import requests
import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import BucketType

class General():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def nsfw(self, ctx):

        author = ctx.message.author
        authormen = author.mention
        server = ctx.message.server
        nsfwrole = discord.utils.get(server.roles, id='407290932644544523')
        if 'Hide NSFW' in [y.name for y in ctx.message.author.roles]:
            await self.bot.remove_roles(author, nsfwrole)
            await self.bot.say("{}, You can now see <#407282477225476096> have fun. 😉".format(authormen))
        else:
            await self.bot.add_roles(author, nsfwrole)
            await self.bot.say("{}, I have hidden <#407282477225476096> from your eyes. 🔞".format(authormen))

    @commands.command(pass_context=True)
    async def ping(self, ctx):
        await self.bot.say("Pong. I'm online!")

    @commands.command(pass_context=True)
    async def stats(self, ctx):
        if ('Moderators' in [y.name for y in ctx.message.author.roles]) or (ctx.message.author.id == "162780049869635584"):
            await self.bot.say(f"**{len(self.bot.servers)} Servers**")
            if len(self.bot.servers) < 20:
                question = await self.bot.say("Since you have less than 20 servers, would you like me to list them? (Type Yes or No in 10 Seconds)")
                response = await self.bot.wait_for_message(author=ctx.message.author, timeout=10)
                try:
                    if response.content.lower().strip() == "yes":
                        await self.bot.delete_message(question)
                        await self.bot.delete_message(response)
                        await self.bot.say(f"**📄 Server List (Requested By: {ctx.message.author})**\n```{[server.name for server in self.bot.servers]}```")
                    elif response.content.lower().strip() == "no":
                        fine = await self.bot.say("Ok fine. 😤")
                        await self.bot.delete_message(question)
                        await self.bot.delete_message(response)
                        await asyncio.sleep(2.5)
                        await self.bot.delete_message(fine)
                except:
                    await self.bot.delete_message(question)

    @commands.cooldown(1.0, 86400.0, commands.BucketType.user)
    @commands.command(pass_context=True)
    async def shout(self, ctx):
        author = ctx.message.author
        server = ctx.message.server
        sbrole = discord.utils.get(server.roles, id='450738085823643668')
        if ('Super Supporters' in [y.name for y in ctx.message.author.roles]) or (ctx.message.author.id == "162780049869635584"):
            question = await self.bot.say("You have **2 minutes** to **type 'Confirm'** or your shout will be wasted.")
            response = await self.bot.wait_for_message(author=ctx.message.author, timeout=120)
            try:
                if response.content.lower().strip() == "confirm":
                    await self.bot.say(f"{ctx.message.author.mention}, I have given you access to speak in <#450739722721951744> for 1 minute. Use it wisely, and remember spamming can breaking our rules can result in a punishment.")
                    await self.bot.add_roles(author, sbrole)
                    await asyncio.sleep(60.0)
                    await self.bot.say(f"{ctx.message.author.mention}, Your time is up. Thank you for using the <#450739722721951744>. We hope you used it wisely!")
                    await self.bot.remove_roles(author, sbrole)
            except:
                await self.bot.say("What a shame. You have wasted your shout! Now you must wait 24 hours. If you believe this is a mistake, please contact an online moderator for assistance.")
        else:
            pass

def setup(bot):
	bot.add_cog(General(bot))