import datetime
import discord
from discord.ext import commands
from discord.ext.commands import Bot

class Help():
    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True)
    async def help(self, ctx):

	    if ctx.invoked_subcommand is None:
                embed = discord.Embed(colour=discord.Colour(value=0x7289da), timestamp=datetime.datetime.utcnow())
                embed.add_field(name="Public Commands", value="🔞 **nsfw**\n`Toggles whether you can see #testing-nsfw or not.`\n`Usage: %nsfw`")
                embed.set_footer(text=f"Requested by {ctx.message.author}")

                await self.bot.say(embed=embed)

    @help.command(pass_context=True)
    async def mod(self, ctx):

        if ('Moderators' in [y.name for y in ctx.message.author.roles]) or (ctx.message.author.id == "162780049869635584"):
            embed = discord.Embed(colour=discord.Colour(value=0x7289da), timestamp=datetime.datetime.utcnow())
            embed.set_footer(text=f"Requested by {ctx.message.author}")
            embed.add_field(name="Moderation Commands", value="👢 **kick**\n`Kicks a person or bot.`\n`Usage: %kick <mention or id> <reason>`\n\n🔨 **ban**\n`Bans a person or bot.`\n`Usage: %ban <mention or id> <reason>`\n\n🔇 **mute**\n`Mutes a person or bot.`\n`Usage: %mute <mention or id> <reason>`\n\n🔊 **unmute**\n`Unmutes a person or bot.`\n`Usage: %unmute <mention or id> <reason>`\n\n🆔 **id**\n`Returns the mentioned user or bot's ID.`\n`Usage: %id <mention>`")

            await self.bot.say(embed=embed)

def setup(bot):
	bot.remove_command('help')
	bot.add_cog(Help(bot))