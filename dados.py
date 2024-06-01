import random
import discord
from discord.ext import commands
import dadosDefinitivos

nimb = commands.Bot('.', case_insensitive = True)
dados = True

@nimb.event
async def on_ready():
    print('Pronto')

@nimb.event
async def on_message(message):
    if dados and message.author.id != 942033769077022730 and message.author.id != 240732567744151553 and 'd' in message.content.split()[0]:
      await message.channel.send(dadosDefinitivos.dados(message.content))

#dados
@nimb.command()
async def desativar_dados(ctx):
  global dados

  if dados:
    dados = False
    await ctx.send(f'{ctx.author.mention} Dados desativados, EM TODOS OS SERVIDORES')
  else:
    dados = True
    await ctx.send(f'{ctx.author.mention} Dados ativados, EM TODOS OS SERVIDORES')

nimb.run('Token')