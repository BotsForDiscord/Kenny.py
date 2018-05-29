import datetime
import time
import discord
from discord.ext import commands
from discord.ext.commands import Bot

class Moderation():
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(kick_members=True)
    @commands.command(pass_context=True)
    async def kick(self, ctx, onm: discord.User, *reason):

        lol = ' '.join(reason)
        men = onm.id
        author = ctx.message.author.id
        lchan = discord.Object(id='374205731483680820')
        nothing = ""
        if lol == nothing:
            lol = "Moderator did not provide a reason."
        if author == men:
            await self.bot.say("I can't let you kick yourself.")
        else:
            await self.bot.kick(onm)
            f = open('current.txt', 'r+')
            text = str(f.read())
            now = int(text) + int(1)
            f.seek(0)
            num = f.write(str(now))
            f.close()
            s = open('current.txt', 'r+')
            texts = str(s.read())
            embedk = discord.Embed(title="Kick | Case #{}".format(texts), colour=discord.Colour(value=0xfac10c), timestamp=datetime.datetime.utcnow())
            embedk.add_field(name="Username", value="{} (<@{}>)".format(onm, men))
            embedk.add_field(name=u'\u2063', value=u'\u2063')
            embedk.add_field(name="Moderator", value="{}".format(ctx.message.author))
            embedk.add_field(name="Reason", value="{}".format(lol))

            await self.bot.send_message(lchan, embed=embedk)
            await self.bot.say('Done, check <#374205731483680820>.')

    @commands.has_permissions(ban_members=True)
    @commands.command(pass_context=True)
    async def ban(self, ctx, onm: discord.User, *reason):

        lol = ' '.join(reason)
        men = onm.id
        author = ctx.message.author.id
        lchan = discord.Object(id='374205731483680820')
        nothing = ""
        if lol == nothing:
            lol = "Moderator did not provide a reason."
        if author == men:
            await self.bot.say("I can't let you ban yourself.")
        else:
            await self.bot.ban(onm)
            f = open('current.txt', 'r+')
            text = str(f.read())
            now = int(text) + int(1)
            f.seek(0)
            num = f.write(str(now))
            f.close()
            s = open('current.txt', 'r+')
            texts = str(s.read())
            embedbn = discord.Embed(title="Ban | Case #{}".format(texts), colour=discord.Colour(value=0xdd2e44), timestamp=datetime.datetime.utcnow())
            embedbn.add_field(name="Username", value="{} (<@{}>)".format(onm, men))
            embedbn.add_field(name=u'\u2063', value=u'\u2063')
            embedbn.add_field(name="Moderator", value="{}".format(ctx.message.author))
            embedbn.add_field(name="Reason", value="{}".format(lol))

            await self.bot.send_message(lchan, embed=embedbn)
            await self.bot.say('Done, check <#374205731483680820>.')

    @commands.has_permissions(kick_members=True)
    @commands.command(pass_context=True)
    async def mute(self, ctx, onm: discord.User, *reason):

        lol = ' '.join(reason)
        men = onm.id
        author = ctx.message.author.id
        server = ctx.message.server
        lchan = discord.Object(id='374205731483680820')
        mute = discord.utils.get(server.roles, id='379424100801576960')
        mutebot = discord.utils.get(server.roles, id='445305264795680768')
        nothing = ""
        if lol == nothing:
            lol = "Moderator did not provide a reason."
        if author == men:
            await self.bot.say("I can't let you mute yourself.")
        else:
            if onm.bot == True:
                typee = "Bot Mute"
                await self.bot.add_roles(onm, mutebot)
            else:
                typee = "User Mute"
                await self.bot.add_roles(onm, mute)
            f = open('current.txt', 'r+')
            text = str(f.read())
            now = int(text) + int(1)
            f.seek(0)
            num = f.write(str(now))
            f.close()
            s = open('current.txt', 'r+')
            texts = str(s.read())
            embedm = discord.Embed(title="{} | Case #{}".format(typee, texts), colour=discord.Colour(value=0xfac10c), timestamp=datetime.datetime.utcnow())
            embedm.add_field(name="Username", value="{} (<@{}>)".format(onm, men))
            embedm.add_field(name=u'\u2063', value=u'\u2063')
            embedm.add_field(name="Moderator", value="{}".format(ctx.message.author))
            embedm.add_field(name="Reason", value="{}".format(lol))

            await self.bot.send_message(lchan, embed=embedm)
            await self.bot.say('Done, check <#374205731483680820>.')

    @commands.has_permissions(kick_members=True)
    @commands.command(pass_context=True)
    async def unmute(self, ctx, onm: discord.User, *reason):

        lol = ' '.join(reason)
        men = onm.id
        author = ctx.message.author.id
        server = ctx.message.server
        lchan = discord.Object(id='374205731483680820')
        mute = discord.utils.get(server.roles, id='379424100801576960')
        mutebot = discord.utils.get(server.roles, id='445305264795680768')
        nothing = ""
        if lol == nothing:
            lol = "Moderator did not provide a reason."
        if author == men:
            await self.bot.say("You can't unmute yourself.")
        else:
            if onm.bot == True:
                typee = "Bot Unmute"
                await self.bot.remove_roles(onm, mutebot)
            else:
                typee = "User Unmute"
                await self.bot.remove_roles(onm, mute)
            f = open('current.txt', 'r+')
            text = str(f.read())
            now = int(text) + int(1)
            f.seek(0)
            num = f.write(str(now))
            f.close()
            s = open('current.txt', 'r+')
            texts = str(s.read())
            embedum = discord.Embed(title="{} | Case #{}".format(typee, text), colour=discord.Colour(value=0x08de06), timestamp=datetime.datetime.utcnow())
            embedum.add_field(name="Username", value="{} (<@{}>)".format(onm, men))
            embedum.add_field(name=u'\u2063', value=u'\u2063')
            embedum.add_field(name="Moderator", value="{}".format(ctx.message.author))
            embedum.add_field(name="Reason", value="{}".format(lol))

            await self.bot.send_message(lchan, embed=embedum)
            await self.bot.say('Done, check <#374205731483680820>.')

    @commands.command(pass_context=True)
    async def id(self, ctx, onm: discord.User):

	    await self.bot.say(onm.id)

    @commands.command(pass_context=True)
    async def say(self, ctx, *say):
        lol = ' '.join(say).replace("@everyone", "@\u200beveryone")\
                            .replace("@here", "@\u200bhere")
        if ('Moderators' in [y.name for y in ctx.message.author.roles]) or (ctx.message.author.id == "162780049869635584"):
            await self.bot.say(lol)
        else:
            pass

def setup(bot):
	bot.add_cog(Moderation(bot))