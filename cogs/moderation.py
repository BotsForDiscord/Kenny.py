import datetime
import json
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
            lol = "`%reason {} [reason]`".format(ctx.message.id)
        if author == men:
            await self.bot.say("I can't let you kick yourself.")
        else:
            await self.bot.kick(onm)
            embed = discord.Embed(title="Kick", colour=discord.Colour(value=0xfac10c), timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Username", value="{} (<@{}>)".format(onm, men))
            embed.add_field(name=u'\u2063', value=u'\u2063')
            embed.add_field(name="Moderator", value="{}".format(ctx.message.author))
            embed.add_field(name="Reason", value="{}".format(lol))
            embed.set_footer(text="Case ID: {}".format(ctx.message.id))

            await self.bot.send_message(lchan, embed=embed)
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
            lol = "`%reason {} [reason]`".format(ctx.message.id)
        if author == men:
            await self.bot.say("I can't let you ban yourself.")
        else:
            await self.bot.ban(onm)
            embed = discord.Embed(title="Ban", colour=discord.Colour(value=0xdd2e44), timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Username", value="{} (<@{}>)".format(onm, men))
            embed.add_field(name=u'\u2063', value=u'\u2063')
            embed.add_field(name="Moderator", value="{}".format(ctx.message.author))
            embed.add_field(name="Reason", value="{}".format(lol))
            embed.set_footer(text="Case ID: {}".format(ctx.message.id))

            await self.bot.send_message(lchan, embed=embed)
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
            lol = "`%reason {} [reason]`".format(ctx.message.id)
        if author == men:
            await self.bot.say("I can't let you mute yourself.")
        else:
            if onm.bot == True:
                typee = "Bot Mute"
                await self.bot.add_roles(onm, mutebot)
            else:
                typee = "User Mute"
                await self.bot.add_roles(onm, mute)
            embed = discord.Embed(title="{}".format(typee), colour=discord.Colour(value=0x000000), timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Username", value="{} (<@{}>)".format(onm, men))
            embed.add_field(name=u'\u2063', value=u'\u2063')
            embed.add_field(name="Moderator", value="{}".format(ctx.message.author))
            embed.add_field(name="Reason", value="{}".format(lol))
            embed.set_footer(text="Case ID: {}".format(ctx.message.id))

            await self.bot.send_message(lchan, embed=embed)
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
            lol = "`%reason {} [reason]`".format(ctx.message.id)
        if author == men:
            await self.bot.say("You can't unmute yourself.")
        else:
            if onm.bot == True:
                typee = "Bot Unmute"
                await self.bot.remove_roles(onm, mutebot)
            else:
                typee = "User Unmute"
                await self.bot.remove_roles(onm, mute)
            embed = discord.Embed(title="{}".format(typee), colour=discord.Colour(value=0x08de06), timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Username", value="{} (<@{}>)".format(onm, men))
            embed.add_field(name=u'\u2063', value=u'\u2063')
            embed.add_field(name="Moderator", value="{}".format(ctx.message.author))
            embed.add_field(name="Reason", value="{}".format(lol))
            embed.set_footer(text="Case ID: {}".format(ctx.message.id))

            await self.bot.send_message(lchan, embed=embed)
            await self.bot.say('Done, check <#374205731483680820>.')

    @commands.has_permissions(kick_members=True)
    @commands.command(pass_context=True)
    async def reason(self, ctx, mid: int, *reason):
        lol = ' '.join(reason)
        channel = ctx.message.channel
        channels = discord.Object(id="374205731483680820")
        logchan = discord.Object(id="467351665691852800")
        message = await self.bot.get_message(channels, str(mid))
        messages = message.embeds
        embedcolor = messages[0]['color']
        embed = discord.Embed(title="{}".format(messages[0]['title']), colour=discord.Colour(value=embedcolor), timestamp=message.timestamp)
        embed.add_field(name="Username", value="{}".format(messages[0]['fields'][0]['value']))
        embed.add_field(name=u'\u2063', value=u'\u2063')
        embed.add_field(name="Moderator", value="{}".format(messages[0]['fields'][2]['value']))
        embed.add_field(name="Reason", value="{}".format(lol))
        embed.set_footer(text="Case ID: {}".format(str(mid)))
        await self.bot.edit_message(message, embed=embed)
        await self.bot.send_message(logchan, "{} ({}) edited case {}.\n**Old:** `{}`\n**New:** `{}`".format(ctx.message.author, ctx.message.author.id, str(mid), messages[0]['fields'][3]['value'], lol))
        await self.bot.say("Case updated, check <#374205731483680820>.")

    @commands.command(pass_context=True)
    async def id(self, ctx, onm: discord.User):

	    await self.bot.say(onm.id)

    @commands.command(pass_context=True)
    async def say(self, ctx, *say):
        lol = ' '.join(say).replace("@everyone", "@\u200beveryone")\
                            .replace("@here", "@\u200bhere")
        if ('Moderators' in [y.name for y in ctx.message.author.roles]) or (ctx.message.author.id == "162780049869635584"):
            await self.bot.say(lol)
        if ctx.message.author.id == "162780049869635584":
            await self.bot.delete_message(ctx.message)
        else:
            pass

def setup(bot):
	bot.add_cog(Moderation(bot))