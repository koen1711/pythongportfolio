import discord
from discord import Client, Intents, Embed
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_components import create_select, create_select_option, create_actionrow
from discord_slash.utils.manage_commands import create_option, create_choice
from discord_slash.context import MenuContext
from discord_slash.model import ContextMenuType
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import wait_for_component, ComponentContext

bot = Client(intents=Intents.default())
slash = SlashCommand(bot, sync_commands=True)

@slash.slash(name="test",
  description="Test command!"
  options=[]
)
async def helpcommand(ctx):
    embed=discord.Embed(title="Test embed", description="Test embed description")
    await ctx.send(embed=embed)
    
bot.run("TOKEN")    
