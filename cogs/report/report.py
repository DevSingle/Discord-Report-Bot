import datetime
import nextcord
from nextcord.ext import commands


class Report(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.guild_only()
    async def report(self, ctx,*,text = None):
        if text == None:
            await ctx.reply('â  Enter You Text On Command\nrb!report test') #Set Your Bot Prefix
            await ctx.message.delete()
        else:
            await ctx.message.delete()
            await ctx.send('â Your request has been sent successfully', delete_after=2)
            embed = nextcord.Embed(title='â  New Report â ',timestamp=datetime.datetime.utcnow(),color=nextcord.Color.red())
            embed.add_field(name='ð¤ Member',value=ctx.author.name)
            embed.add_field(name='â Text', value=text)
            embed.set_thumbnail(url=ctx.author.display_avatar)
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.display_avatar)
            embed.set_footer(text='ð¨âð»By < Black / Eye >')
            msg = await self.bot.get_channel(Report Channel Id).send(f'{ctx.author.mention} <@&ROLE ID>',embed=embed) #report channel = report channel id & ROLE ID = Role ID For Mention On Report Channel
            await msg.add_reaction('â')
            await msg.add_reaction('â')

def setup(bot):
    bot.add_cog(Report(bot))
