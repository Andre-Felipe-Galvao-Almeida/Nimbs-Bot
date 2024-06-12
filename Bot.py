import random
import time
import discord
from discord.ext import commands
import dadosDefinitivos

# Mudei para que o prefix seja . e aceite nos comandos letras maiusculas e minisculas fodase
intents = discord.Intents.default() # tive que mudar por politicas novas do discord
intents.message_content = True
nimb = commands.Bot(intents=intents, command_prefix=".", case_insensitive = True)
dados = True
ligado = True
@nimb.event
async def on_ready():
    print('Pronto')

@nimb.event
async def on_message(message):
  if message.author == nimb.user:
    return
  if dados and ligado and message.author.id != 240732567744151553 and 'd' in message.content.split()[0] and message.content[message.content.find('d')+1:message.content.find('d')+2].isnumeric():
      await message.channel.send(dadosDefinitivos.dados(message.content))
  await nimb.process_commands(message)

@nimb.command()
async def dice(ctx):
  await ctx.send(f'{ctx.author.mention}\n```Para os meus dados é simples.\nChamar um dado pelo nome o faz rolar "d20".\nColocar valores antes dele faz rolar varias vezes e somar "3d20"\nColocar "Número#" o faz rolar sem somar "3#d20\nVocê pode usar as duas funcionalidades juntas "2#3d20"\nE pode também fazer calculos após os dados "d20+12-2","d20/2*3"\n```')

@nimb.command()
async def desativar_dados(ctx):
  global dados, ligado
  if ligado and dados:
    dados = False
    await ctx.send(f'{ctx.author.mention} Dados desativados, EM TODOS OS SERVIDORES')
  else:
    dados = True
    await ctx.send(f'{ctx.author.mention} Dados ativados, EM TODOS OS SERVIDORES')

@nimb.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member):
  if ligado:
    await user.kick()

@nimb.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member):
  if ligado:
    await user.ban()

@nimb.command()
async def comandos(ctx):
  if ligado:
    await ctx.send('**A lista de comandos é:** ```\n criadores \n clear \n ban \n dice \n teste \n kick```')

@nimb.command()
async def teste(ctx):
  if ligado:
    await ctx.send(f'olha a mãe do {ctx.author.mention}')

@nimb.command()
async def criadores(ctx):
  if ligado:
    await ctx.send('**Git dos criadores:** \n https://github.com/DarthFontes \n https://github.com/Andre-Felipe-Galvao-Almeida')

@nimb.command(aliases = ['purge', 'delete'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount: int = 1000000):
  if ligado:
    await ctx.channel.purge(limit = amount)

@nimb.command()
async def dee(ctx):
  if ligado:
    await ctx.author.send(f'Parabéns por descobrir o segredo {ctx.author.mention} \n **Não repasse para frente, assim não estraga a brincadeira** \n https://discord.gg/g9WZSDSDZT \n https://i.pinimg.com/564x/1f/54/67/1f54674fbc2efec9caa124988406f945.jpg')
    time.sleep(1000)

@nimb.command()
async def ccbbededba(ctx):
  await ctx.author.send('Modo Deus desboqueado')
  time.sleep(300)

@nimb.command()
async def morra(ctx):
  global ligado
  if ctx.author.id == 365660914177015809 or ctx.author.id == 496795235289006091:
    if ligado:
      ligado = False
      await ctx.send('**I will be back**')
    else:
      ligado = True
      await ctx.send('**Não há morte**')

nimb.run('')