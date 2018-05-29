from typing import List
import schedule
import datetime
import time
import random
import urllib
import json
import requests
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import BucketType

class Featured():
    def __init__(self, bot):
        self.bot = bot

    def _member_has_role(self, member: discord.Member, role: discord.Role):
        return role in member.roles

    def _get_users_with_role(self, server: discord.Server,
                             role: discord.Role) -> List[discord.User]:
        roled = []
        for member in server.members:
            if self._member_has_role(member, role):
                roled.append(member)
        return roled

    @commands.command(no_pm=True, pass_context=True)
    async def feature(self, ctx):

        auid = ctx.message.author.id
        server = ctx.message.server
        sender = ctx.message.author
        role = discord.utils.get(server.roles, id='374083302237274113')
        fchan = discord.Object(id='413177656276942873')
        ft_these = self._get_users_with_role(server, role)
        now = datetime.datetime.now()
        habchy = "162780049869635584"
        if auid == habchy:
            async for x in self.bot.logs_from(fchan, limit = 100):
                await self.bot.delete_message(x)
            vbotr = random.choice(ft_these)
            vbotr2 = random.choice(ft_these)
            if vbotr == vbotr2:
                vbotr2 = random.choice(ft_these)
            api = "https://botsfordiscord.com/api/v1/bots/{}".format(vbotr.id)
            r = requests.get(api)
            rm = r.json()
            snd = rm["owner"]
            short = rm["shortDesc"]
            fix = rm["prefix"]
            inv = rm["invite"]
            owner = discord.utils.get(self.bot.get_all_members(), id='{}'.format(snd))
            api2 = "https://botsfordiscord.com/api/v1/bots/{}".format(vbotr2.id)
            r2 = requests.get(api2)
            rm2 = r2.json()
            snd2 = rm2["owner"]
            short2 = rm2["shortDesc"]
            fix2 = rm2["prefix"]
            inv2 = rm2["invite"]
            owner2 = discord.utils.get(self.bot.get_all_members(), id='{}'.format(snd2))
            await self.bot.send_message(fchan, f"<:bfdfeatured:413473382135234571> The Featured Bots for **{now.month}/{now.day}/{now.year}** are brought to you by **{owner.name}** and **{owner2.name}**.")
            embed1 = discord.Embed(title="<:bfdfeatured:413473382135234571> **Featured Bot**", colour=discord.Colour(value=0x7289da), timestamp=datetime.datetime.utcnow())
            embed1.set_thumbnail(url="{}".format(vbotr.avatar_url))
            embed1.add_field(name="**Bot**", value=f"<@{vbotr.id}> `[{vbotr}]`")
            embed1.add_field(name="**Made By**", value=f"<@{snd}> `[{owner}]`")
            embed1.add_field(name="**Prefix**", value=f"`{fix}`")
            embed1.add_field(name="**About**", value=f"```{short}```")
            embed1.add_field(name="**Learn More**", value=f"[**View Bot Page**](https://botsfordiscord.com/bot/{vbotr.id}) | [**Invite Bot**]({inv})")
            embed1.set_footer(text="Bots for Discord", icon_url=f"{owner.avatar_url}")
            await self.bot.send_message(fchan, embed=embed1)
            embed2 = discord.Embed(title="<:bfdfeatured:413473382135234571> **Featured Bot**", colour=discord.Colour(value=0x7289da), timestamp=datetime.datetime.utcnow())
            embed2.set_thumbnail(url="{}".format(vbotr2.avatar_url))
            embed2.add_field(name="**Bot**", value=f"<@{vbotr2.id}> `[{vbotr2}]`")
            embed2.add_field(name="**Made By**", value=f"<@{snd2}> `[{owner2}]`")
            embed2.add_field(name="**Prefix**", value=f"`{fix2}`")
            embed2.add_field(name="**About**", value=f"```{short2}```")
            embed2.add_field(name="**Learn More**", value=f"[**View Bot Page**](https://botsfordiscord.com/bot/{vbotr2.id}) | [**Invite Bot**]({inv2})")
            embed2.set_footer(text="Bots for Discord", icon_url=f"{owner2.avatar_url}")
            await self.bot.send_message(fchan, embed=embed2)
            await self.bot.say("Everything is complete with 0 errors, check <#413177656276942873>.")
        else:
            pass

    @commands.command(no_pm=True, pass_context=True)
    async def featuretest(self, ctx):

        auid = ctx.message.author.id
        server = ctx.message.server
        sender = ctx.message.author
        role = discord.utils.get(server.roles, id='374083302237274113')
        fchan = discord.Object(id='413899638764994561')
        ft_these = self._get_users_with_role(server, role)
        now = datetime.datetime.now()
        habchy = "162780049869635584"
        if auid == habchy:
            async for x in self.bot.logs_from(fchan, limit = 100):
                await self.bot.delete_message(x)
            vbotr = random.choice(ft_these)
            vbotr2 = random.choice(ft_these)
            if vbotr == vbotr2:
                vbotr2 = random.choice(ft_these)
            api = "https://botsfordiscord.com/api/v1/bots/{}".format(vbotr.id)
            r = requests.get(api)
            rm = r.json()
            snd = rm["owner"]
            short = rm["shortDesc"]
            fix = rm["prefix"]
            inv = rm["invite"]
            owner = discord.utils.get(self.bot.get_all_members(), id='{}'.format(snd))
            api2 = "https://botsfordiscord.com/api/v1/bots/{}".format(vbotr2.id)
            r2 = requests.get(api2)
            rm2 = r2.json()
            snd2 = rm2["owner"]
            short2 = rm2["shortDesc"]
            fix2 = rm2["prefix"]
            inv2 = rm2["invite"]
            owner2 = discord.utils.get(self.bot.get_all_members(), id='{}'.format(snd2))
            await self.bot.send_message(fchan, f"<:bfdfeatured:413473382135234571> The Featured Bots for **{now.month}/{now.day}/{now.year}** are brought to you by **{owner.name}** and **{owner2.name}**.")
            embed1 = discord.Embed(title="<:bfdfeatured:413473382135234571> **Featured Bot**", colour=discord.Colour(value=0x7289da), timestamp=datetime.datetime.utcnow())
            embed1.set_thumbnail(url="{}".format(vbotr.avatar_url))
            embed1.add_field(name="**Bot**", value=f"<@{vbotr.id}> `[{vbotr}]`")
            embed1.add_field(name="**Made By**", value=f"<@{snd}> `[{owner}]`")
            embed1.add_field(name="**Prefix**", value=f"`{fix}`")
            embed1.add_field(name="**About**", value=f"```{short}```")
            embed1.add_field(name="**Learn More**", value=f"[**View Bot Page**](https://botsfordiscord.com/bot/{vbotr.id}) | [**Invite Bot**]({inv})")
            embed1.set_footer(text="Bots for Discord", icon_url=f"{owner.avatar_url}")
            await self.bot.send_message(fchan, embed=embed1)
            embed2 = discord.Embed(title="<:bfdfeatured:413473382135234571> **Featured Bot**", colour=discord.Colour(value=0x7289da), timestamp=datetime.datetime.utcnow())
            embed2.set_thumbnail(url="{}".format(vbotr2.avatar_url))
            embed2.add_field(name="**Bot**", value=f"<@{vbotr2.id}> `[{vbotr2}]`")
            embed2.add_field(name="**Made By**", value=f"<@{snd2}> `[{owner2}]`")
            embed2.add_field(name="**Prefix**", value=f"`{fix2}`")
            embed2.add_field(name="**About**", value=f"```{short2}```")
            embed2.add_field(name="**Learn More**", value=f"[**View Bot Page**](https://botsfordiscord.com/bot/{vbotr2.id}) | [**Invite Bot**]({inv2})")
            embed2.set_footer(text="Bots for Discord", icon_url=f"{owner2.avatar_url}")
            await self.bot.send_message(fchan, embed=embed2)
            await self.bot.say("Everything is complete with 0 errors, check <#413899638764994561>.")
        else:
            pass

    @commands.command(no_pm=True, pass_context=True)
    async def featurerig(self, ctx, vbotr: discord.User, vbotr2: discord.User):

        #pls dont yell at me. ive never used it lol
        auid = ctx.message.author.id
        server = ctx.message.server
        sender = ctx.message.author
        role = discord.utils.get(server.roles, id='374083302237274113')
        fchan = discord.Object(id='413177656276942873')
        now = datetime.datetime.now()
        habchy = "162780049869635584"
        if auid == habchy:
            async for x in self.bot.logs_from(fchan, limit = 100):
                await self.bot.delete_message(x)
            api = "https://botsfordiscord.com/api/v1/bots/{}".format(vbotr.id)
            r = requests.get(api)
            rm = r.json()
            snd = rm["owner"]
            short = rm["shortDesc"]
            fix = rm["prefix"]
            inv = rm["invite"]
            owner = discord.utils.get(self.bot.get_all_members(), id='{}'.format(snd))
            api2 = "https://botsfordiscord.com/api/v1/bots/{}".format(vbotr2.id)
            r2 = requests.get(api2)
            rm2 = r2.json()
            snd2 = rm2["owner"]
            short2 = rm2["shortDesc"]
            fix2 = rm2["prefix"]
            inv2 = rm2["invite"]
            owner2 = discord.utils.get(self.bot.get_all_members(), id='{}'.format(snd2))
            await self.bot.send_message(fchan, f"<:bfdfeatured:413473382135234571> The Featured Bots for **{now.month}/{now.day}/{now.year}** are brought to you by <@{owner.id}> and <@{owner2.id}>.")
            embed1 = discord.Embed(title="<:bfdfeatured:413473382135234571> **Featured Bot**", colour=discord.Colour(value=0x7289da), timestamp=datetime.datetime.utcnow())
            embed1.set_thumbnail(url="{}".format(vbotr.avatar_url))
            embed1.add_field(name="**Bot**", value=f"<@{vbotr.id}> `[{vbotr}]`")
            embed1.add_field(name="**Made By**", value=f"<@{snd}> `[{owner}]`")
            embed1.add_field(name="**Prefix**", value=f"`{fix}`")
            embed1.add_field(name="**About**", value=f"```{short}```")
            embed1.add_field(name="**Learn More**", value=f"[**View Bot Page**](https://botsfordiscord.com/bot/{vbotr.id}) | [**Invite Bot**]({inv})")
            embed1.set_footer(text="Bots for Discord", icon_url=f"{owner.avatar_url}")
            await self.bot.send_message(fchan, embed=embed1)
            embed2 = discord.Embed(title="<:bfdfeatured:413473382135234571> **Featured Bot**", colour=discord.Colour(value=0x7289da), timestamp=datetime.datetime.utcnow())
            embed2.set_thumbnail(url="{}".format(vbotr2.avatar_url))
            embed2.add_field(name="**Bot**", value=f"<@{vbotr2.id}> `[{vbotr2}]`")
            embed2.add_field(name="**Made By**", value=f"<@{snd2}> `[{owner2}]`")
            embed2.add_field(name="**Prefix**", value=f"`{fix2}`")
            embed2.add_field(name="**About**", value=f"```{short2}```")
            embed2.add_field(name="**Learn More**", value=f"[**View Bot Page**](https://botsfordiscord.com/bot/{vbotr2.id}) | [**Invite Bot**]({inv2})")
            embed2.set_footer(text="Bots for Discord", icon_url=f"{owner2.avatar_url}")
            await self.bot.send_message(fchan, embed=embed2)
            await self.bot.say("Everything is complete with 0 errors, check <#413177656276942873>.")
        else:
            pass

    @commands.command(no_pm=True, pass_context=True)
    async def resetfeature(self, ctx):

        auid = ctx.message.author.id 
        habchy = "162780049869635584"
        fchan = discord.Object(id='413177656276942873')
        if auid == habchy:
            async for x in self.bot.logs_from(fchan, limit = 100):
                await self.bot.delete_message(x)
            await self.bot.say("Featured bots reset.")
        else:
            pass

def setup(bot):
    bot.add_cog(Featured(bot))