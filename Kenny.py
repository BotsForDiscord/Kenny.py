from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import discord
import json

startup_extensions = ["help", "moderation", "general", "featured"]

bot = Bot (command_prefix=commands.when_mentioned_or('%'))

@bot.event
async def on_command_error(error, ctx):
        cmd = ctx.command
        if isinstance(error, commands.BadArgument):
        	await bot.send_message(ctx.message.channel, "**ERROR in the Command {}:**```py\n{}```".format(cmd, error))
        if isinstance(error, commands.CommandInvokeError):
        	await bot.send_message(ctx.message.channel, "**ERROR in the Command {}:**```py\n{}```".format(cmd, error))
        if isinstance(error, commands.CommandOnCooldown):
        	await bot.send_message(ctx.message.channel, "⏱ **This command is currently under cooldown. Try again in {:.2f} hours!**".format(error.retry_after / 3600))
        else:
            print(error)

@bot.event
async def on_ready():
	print('Logged in as '+bot.user.name+' (ID:'+bot.user.id+') | Connected to '+str(len(bot.servers))+' servers | Connected to '+str(len(set(bot.get_all_members())))+' users')
	print('--------')
	return await bot.change_presence(game=discord.Game(name='Bots for Discord', type=3))

@bot.event
async def on_message(message):
    allowed = ["308358617458016256", "374071874222686211", "374074135506190349"]
    if message.author.bot:
        return
    if message.server.id not in allowed:
        return
    await bot.process_commands(message)

@bot.command(pass_context=True)
async def shutdown(ctx):

	habchy = "162780049869635584"
	authorid = ctx.message.author.id
	if authorid == habchy:
		await bot.say("👋 **Goodbye!**")
		await bot.add_reaction(ctx.message, "✅")
		await bot.change_presence(game=discord.Game(name=''), status=discord.Status('offline'))
		await bot.logout()
	else:
		await bot.add_reaction(ctx.message, "🚫")

@bot.command(pass_context=True)
async def load(ctx, extension_name : str):
    authid = ctx.message.author.id
    owner = "162780049869635584"
    cogExt = 'cogs.' + extension_name
    if authid == owner:
        try:
            bot.load_extension(cogExt)
        except (AttributeError, ImportError) as e:
            await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
            return
        await bot.say("**{}** module loaded.".format(extension_name))
    else:
        pass

@bot.command(pass_context=True)
async def unload(ctx, extension_name : str):
    authid = ctx.message.author.id
    owner = "162780049869635584"
    cogExt = 'cogs.' + extension_name
    if authid == owner:
        bot.unload_extension(cogExt)
        await bot.say("**{}** module unloaded.".format(extension_name))
    else:
        pass

@bot.command(pass_context=True)
async def reload(ctx, extension_name : str):
    authid = ctx.message.author.id
    owner = "162780049869635584"
    cogExt = 'cogs.' + extension_name
    if authid == owner:
        bot.unload_extension(cogExt)
        try:
            bot.load_extension(cogExt)
        except (AttributeError, ImportError) as e:
            await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
            return
        await bot.say("**{}** module reloaded.".format(extension_name))
    else:
        pass

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            cogExt = 'cogs.' + extension
            bot.load_extension(cogExt)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

config = json.load(open('config.json'))
bot.run(config['token'])