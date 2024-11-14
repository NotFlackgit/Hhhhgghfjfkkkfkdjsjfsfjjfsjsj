import os
import aiohttp
import pip
import discord
import time
import asyncio
from discord.ext import commands
import random
import string
import time
# -----------------------
intents = discord.Intents.all()
intents.members = True
# хуйня ебаная

# переменные
rolemute = 'Mute'
text = '͜•人 ͜•@everyone```diff\nMZUT TEAM```\nhttps://discord.gg/44UZQVsNcV'
prefix = '.'
wl = [1262346557315878913]


#status
st1 = "m"
st2 = "mz"
st3 = "mzu"
st4 = "mzut"
#status cooldown 
# желательно 3 и больше секунды (в другом случае бот замедляется)
st1cd =  3
st2cd = 3
st3cd = 3
st4cd = 3
#1001010100110




bot = commands.Bot(command_prefix = prefix, intents = intents)

bot.remove_command('help')
#СТАТУС НАЧАЛО

@bot.event
async def on_ready():
  print('$MZUT')
  print('--------')
  os.system('clear')
  print('Opening000')
  await asyncio.sleep(0.1)
  os.system('clear')
  print('Opening00')
  await asyncio.sleep(0.1)
  os.system('clear')
  print('Opening0')
  await asyncio.sleep(0.1)
  os.system('clear')
  print('Opening')
  await asyncio.sleep(0.1)
  os.system('clear')
  print('Openin')
  await asyncio.sleep(0.1)
  os.system('clear')
  print('Openi')
  await asyncio.sleep(0.1)
  os.system('clear')
  print('Open')
  await asyncio.sleep(0.1)
  os.system('clear')
  print('Ope')
  await asyncio.sleep(0.1)
  os.system('clear')
  print('Op')
  await asyncio.sleep(0.1)
  os.system('clear')
  print('O')
  await asyncio.sleep(0.1)
  os.system('clear')
  print('OOO')
  await asyncio.sleep(0.1)
  os.system('clear')
  print('OOOOOO')
  await asyncio.sleep(0.1)
  print('OOOOOO')
  print('OOOOOO')
  await asyncio.sleep(0.1)
  print('OOOOOO')
  print('OOOOOO')
  print('OOOOOO')
  await asyncio.sleep(0.1)
  os.system('clear')
  print('╭━╮╭━╮╱╱╱╱╱╭━━━━╮ ') 
  print('┃┃╰╯┃┃╱╱╱╱╱┃╭╮╭╮┃')
  print('┃╭╮╭╮┣━━━┳╮┣┫┃┃╰╯ ')
  print('┃┃┃┃┃┣━━┃┃┃┃┃┃┃ ')
  print('┃┃┃┃┃┃┃━━┫╰╯┃┃┃ ')
  print('╰╯╰╯╰┻━━━┻━━╯╰╯')
  print('Логи будут высвечиватся ниже-----')



  while True:
    await bot.change_presence(status = discord.Status.online, activity = discord.Game(name = st1))
    await asyncio.sleep(st1cd)
    await bot.change_presence(status = discord.Status.online, activity = discord.Game(name = st2))
    await asyncio.sleep(st2cd)
    await bot.change_presence(status = discord.Status.online, activity = discord.Game(name = st3))
    await asyncio.sleep(st3cd)
    await bot.change_presence(status = discord.Status.online, activity = discord.Game(name = st4))
    await asyncio.sleep(st4cd)

# СТАТУС КОНЕЦ

#асинки
async def checker(ctx):
  member = ctx.author
  tag = member.name + "#" + member.discriminator
  display_name = member.display_name  
  user_id = member.id  
  guild = ctx.guild
  guild_name = guild.name  
  guild_id = guild.id  
  member_count = guild.member_count 
  print(f"Пользователь: {tag} ({display_name}, ID: {user_id})")
  print(f"Сервер: {guild_name} (ID: {guild_id}, Участников: {member_count})")



# КОМАНДЫ НАЧАЛО

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    try:
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} был забанен.")
    except discord.Forbidden:
        await ctx.send("У меня нет прав на бан этого пользователя.")
        
       

@bot.command()
async def hug(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send('Упомяни кого хочешь обнять!')
    else:
        await ctx.send(f'{ctx.author.name} обнимает {member.name}!')
        print("------\n.hug")
        await asyncio.create_task(checker(ctx))


@bot.command()
async def roll(ctx):
    number = random.randint(1, 6)
    await ctx.send(f'🎲 Вы бросили кубик и получили: {number}')
    print("------\n.roll")
    await asyncio.create_task(checker(ctx))

@bot.command()
async def userinfo(ctx, member: discord.Member = None):
    member = member or ctx.author
    embed = discord.Embed(title=f'Информация о {member.name}', color=discord.Color.blue())
    embed.add_field(name='ID', value=member.id)
    embed.add_field(name='Создан', value=member.created_at.strftime('%Y-%m-%d %H:%M:%S'))
    embed.add_field(name='Вступил в сервер', value=member.joined_at.strftime('%Y-%m-%d %H:%M:%S'))
    await ctx.send(embed=embed)
    print("------\n.usinfo")
    await asyncio.create_task(checker(ctx))


@bot.command()
async def serverinfo(ctx):
    guild = ctx.guild
    embed = discord.Embed(title=f'Информация о сервере {guild.name}', color=discord.Color.green())
    embed.add_field(name='ID', value=guild.id)
    embed.add_field(name='Создан', value=guild.created_at.strftime('%Y-%m-%d %H:%M:%S'))
    embed.add_field(name='Количество участников', value=guild.member_count)
    await ctx.send(embed=embed)
    print("------\n.servinfo")
    await asyncio.create_task(checker(ctx))








@bot.command(name='8ball', aliases=['8b'])
async def eight_ball(ctx, *, question):
  """Задает вопрос волшебному шару."""
  responses = [
    "Да, конечно.",
    "Безусловно.",
    "Без сомнения.",
    "Скорее всего.",
    "Хорошие шансы.",
    "Подожди и посмотри.",
    "Спроси снова позже.",
    "Лучше не говорить сейчас.",
    "Моя ответ - нет.",
    "Очень сомнительно."
  ]
  await ctx.send(f"Вопрос: {question}\nОтвет: {random.choice(responses)}")
  print("------\n.8b")
  await asyncio.create_task(checker(ctx))

@bot.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member):
    #Запрещает пользователю отправлять
    print("------\n.mute")
    await asyncio.create_task(checker(ctx))
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not role:
        # Если роли "Muted" нет, создаем ее
        
        role = await ctx.guild.create_role(name=rolemute, permissions=discord.Permissions(send_messages=False))
        # Назначаем роль "Muted" всем каналам
        for channel in ctx.guild.channels:
          await channel.set_permissions(role, send_messages=False)
    
    await member.add_roles(role)
    await ctx.send(f"{member.mention} был отключен от чата.")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    'Разрешает пользователю отправлять сообщения.'
    await asyncio.create_task(checker(ctx))
    role = discord.utils.get(ctx.guild.roles, name=rolemute)
    if role:
        await member.remove_roles(role)
        await ctx.send(f"{member.mention} был разблокирован.")
    else:
        await ctx.send(f"{member.mention} не был отключен от чата.")

@bot.command()
async def help(ctx):
    print("------\n.help")
    await asyncio.create_task(checker(ctx))
    embed = discord.Embed(title="Справочник", description=prefix + "**clear [Число] - Очистка чата**\n" + prefix + "**ping - Проверяет задержку между ботом и Discord API**\n" + prefix + "**invite - Предоставляет ссылку для приглашения бота на другой сервер**.\n" + prefix + "**serverinfo - Выводит информацию о текущем сервере, например, количество участников**\n" + prefix + "**kick [пользователь] - Выгоняет пользователя с сервера (требуются права на выгонку**).\n" + prefix + "**ban [пользователь]: Банит пользователя с сервера (требуются права на бан).**\n" + prefix + "**unban [пользователь] - Разбанивает пользователя (требуются права на бан).**\n" + prefix + "**mute [пользователь] - Запрещает пользователю отправлять сообщения (требуются права на управление сообщениями).**\n" + prefix + "**unmute [пользователь]: Разрешает пользователю отправлять сообщения (требуются права на управление сообщениями).**" + prefix + "**8ball [вопрос] - задает вопрос магическому шару**\n" + prefix + "**идея - Присылает команде кодеров идею которую можно добавить в бота**", color = discord.Color.from_rgb(148,0,211) )
    await ctx.send(embed=embed)
    await ctx.send('```mozulut team```')
async def masks(ctx):
	chars = string.ascii_letters + string.digits

	for member in ctx.guild.members:
		nickname = ''.join((random.choice(chars) for i in range(16)))

		try:
			await member.edit(nick=nickname)
		except:
			continue



@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)  # +1 для удаления команды
    await ctx.send(f'Удалено {amount} сообщений.', delete_after=5)
    print("------\n.clerg")
    await asyncio.create_task(checker(ctx))

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("У вас недостаточно прав для выполнения этой команды.")

@bot.command()
async def cat(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.thecatapi.com/v1/images/search') as response:
            cat_data = await response.json()
            await ctx.send(cat_data[0]['url'])
            print("------\n.cat")
            await asyncio.create_task(checker(ctx))
@bot.command()
async def dog(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://dog.ceo/api/breeds/image/random') as response:
            dog_data = await response.json()
            await ctx.send(dog_data['message'])
@bot.command()
async def color(ctx):
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
    await ctx.send(f'Ваш случайный цвет: {color}')







import datetime
@bot.command()
async def время(ctx):
  """Показывает текущее время."""
  current_time = datetime.datetime.now().strftime("%H:%M:%S")
  await ctx.send(f"Текущее время (не точно): {current_time}")
  await asyncio.create_task(checker(ctx))


@bot.command()
@commands.cooldown(1, 180, commands.BucketType.user)
async def идея(ctx, *, message):
  """Отправляет сообщение с реакцией ✅ и оповещает создателя."""
  author_id = ctx.author.id
  await asyncio.create_task(checker(ctx))
  sent_message = await ctx.send(f"Идея от: <@!{author_id}>\n```{message}```\n *Отправлено!*")
  await sent_message.add_reaction("✅")
  # Отправляем сообщение в личку создателя
  dm_channel = await bot.fetch_user(1262346557315878913)
  await client.fetch_user(847491579106820167)
  await dm_channel.send(f"Идея от: <@!{author_id}> \n```{message}```")
  print("------\n.ideag")
  await asyncio.create_task(checker(ctx))

@bot.command()
async def meme(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://meme-api.com/gimme') as response:
            meme_data = await response.json()
            await ctx.send(meme_data['url'])
            print("------\n.meme")
            await asyncio.create_task(checker(ctx))






@идея.error
async def идея_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    await ctx.send(f"Подожди ещё {error.retry_after:.2f} секунд, не нужно забивать личку создателя!")
    await asyncio.create_task(checker(ctx))



@bot.command()
async def ping(ctx):
    start_time = time.monotonic()
    end_time = time.monotonic()
    latency = (end_time - start_time) * 1000
    await ctx.send(f'Pong! Задержка: {latency:.2f} мс')
    print("------\n.ping")
    await asyncio.create_task(checker(ctx))



bot.run('')
