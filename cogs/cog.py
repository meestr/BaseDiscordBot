from discord.ext import commands


class MyCog(commands.Cog):
  def __init__(self, bot: commands.Bot):
    self.bot = bot
  @commands.command(name='mycommands')
  async def commands(self, ctx):
    return await ctx.send("this is really a bruh moment")
   
def setup(bot: commands.Bot):
  bot.add_cog(MyCog(bot=bot))
