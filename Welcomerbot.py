import discord
from discord.ext import commands

# Your bot's token
TOKEN = ''

# Create the bot instance
intents = discord.Intents.default()
intents.members = True  # Enable access to member events
bot = commands.Bot(command_prefix="!", intents=intents)

welcomer_channel_id = None

# Command to setup the welcomer channel
@bot.command(name="setup_welcomer")
async def setup_welcomer(ctx):
    global welcomer_channel_id
    welcomer_channel_id = ctx.channel.id
    await ctx.send(f"Welcomer is setuped in this channel: {ctx.channel.name}")

# Event to welcome new members
@bot.event
async def on_member_join(member):
    if welcomer_channel_id is not None:
        channel = bot.get_channel(welcomer_channel_id)
        role = discord.Object(id=SET YOUR OWN ID ROLE WHICH WILL BE GIVEN WHEN MEMBER JOIN)
        await member.add_roles(role)
        await channel.send(f"Welcome add your text here for welcome message, {member.mention}!")

# Run the bot
bot.run(TOKEN)