import discord
from discord.ext import commands
from core.bot import Playground


class Owner(commands.Cog):
    def __init__(self, bot: Playground):
        self.bot = bot
        self.success = '✅'
        self.fail = '❎'
        self.delete_delay = 5


    async def cog_check(self, ctx: commands.Context):
        return await self.bot.is_owner(ctx.author)


    @commands.command(name='load')
    async def load_command(self, ctx: commands.Context, cog: str):
        extension = f'cogs.{cog}'
        try:
            await self.bot.load_extension(extension)
            print(f'Successfully loaded extension {extension}')
            emoji = self.success
        except:
            print(f'Failed to load extension {extension}')
            emoji = self.fail
        await ctx.message.add_reaction(emoji)
        await ctx.message.delete(delay=self.delete_delay)


    @commands.command(name='reload')
    async def reload_command(self, ctx: commands.Context, cog: str):
        extension = f'cogs.{cog}'
        try:
            await self.bot.reload_extension(extension)
            print(f'Successfully reloaded extension {extension}')
            emoji = self.success
        except:
            print(f'Failed to reload extension {extension}')
            emoji = self.fail
        await ctx.message.add_reaction(emoji)
        await ctx.message.delete(delay=self.delete_delay)


    @commands.command(name='unload')
    async def unload_command(self, ctx: commands.Context, cog: str):
        extension = f'cogs.{cog}'
        try:
            await self.bot.unload_extension(extension)
            print(f'Successfully unloaded extension {extension}')
            emoji = self.success
        except:
            print(f'Failed to unload extension {extension}')
            emoji = self.fail
        await ctx.message.add_reaction(emoji)
        await ctx.message.delete(delay=self.delete_delay)


    @commands.command(name='sync')
    async def sync_command(self, ctx: commands.Context, guild: str):
        try:
            guild_object = None
            if guild == 'g':
                guild_object = discord.Object(id=ctx.guild.id)
                self.bot.tree.copy_global_to(guild=guild_object)
            await self.bot.tree.sync(guild=guild_object)
            print('Successfully synchronized commands')
            emoji = self.success
        except:
            print('Failed to synchronize commands')
            emoji = self.fail
        await ctx.message.add_reaction(emoji)
        await ctx.message.delete(delay=self.delete_delay)


    @commands.command(name='clear')
    async def clear_command(self, ctx: commands.Context, guild: str):
        try:
            guild_object = None
            if guild == 'g':
                guild_object = discord.Object(id=ctx.guild.id)
            self.bot.tree.clear_commands(guild=guild_object)
            await self.bot.tree.sync(guild=guild_object)
            print('Successfully cleared commands')
            emoji = self.success
        except:
            print('Failed to clear commands')
            emoji = self.fail
        await ctx.message.add_reaction(emoji)
        await ctx.message.delete(delay=self.delete_delay)
