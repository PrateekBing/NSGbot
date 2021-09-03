from discord.utils import get 
import discord
from discord.ext import commands
from discord.ext.commands import clean_content
import os

client = commands.Bot(command_prefix = '.') 

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.command(description="Mutes members")
@commands.has_role('▪️ Epic Staff ▪️')
async def mute(ctx, member: discord.Member):

    role = discord.utils.get(ctx.guild.roles, name='Muted')
    role1 = discord.utils.get(ctx.guild.roles, name='▪️ Community ▪️')
    await member.remove_roles(role1)
    await member.add_roles(role)
    embed = discord.Embed(title="User Muted!",
                              description="**{}** was muted by **{}**!".format(member, ctx.author),
                              color=0xff00f6)
    await ctx.send(embed=embed)

@client.command(description="Unmutes muted members")
@commands.has_role('▪️ Epic Staff ▪️')
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    role1 = discord.utils.get(ctx.guild.roles, name='▪️ Community ▪️')
    await member.add_roles(role1)
    await member.remove_roles(role)
    embed = discord.Embed(title="User Unmuted!",
                              description="**{}** was unmuted by **{}**!".format(member, ctx.author),
                              color=0xff00f6)
    await ctx.send(embed=embed)


@client.command(description="Gives link to NSG website")
async def website(ctx):
    embed = discord.Embed(title="Our Website:", description="http://nosweatsgaming.rf.gd/")
    await ctx.send(embed=embed)

@client.command(description="Show's server information")
async def serverinfo(ctx):
  name = str(ctx.guild.name)
  description = str(ctx.guild.description)

  owner = str(ctx.guild.owner)
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)

  icon = str(ctx.guild.icon_url)
   
  embed = discord.Embed(
      title=name + " Server Information",
      description=description,
      color=discord.Color.blue()
    )
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Owner", value="@Inferno#6414", inline=True)
  embed.add_field(name="Server ID", value=id, inline=True)
  embed.add_field(name="Region", value=region, inline=True)
  embed.add_field(name="Member Count", value=memberCount, inline=True)

  await ctx.send(embed=embed)

@client.command(description="shows your ping")
async def ping(ctx):
    await ctx.send(f'{round(client.latency*1000)}ms')


token = os.environ.get('TOKEN1')
client.run(token)