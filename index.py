<<<<<<< Updated upstream
import discord, json, time, os, random
=======
import discord, json, time
>>>>>>> Stashed changes

with open("config.json") as _j:
	__token = json.loads(_j.read())["token"]

__client = discord.Client()
__timer_max = 120
__num_emoji = [":zero:", ":one:", ":two:", ":three:", ":four:",
					 ":five:", ":six:", ":seven:", ":eight:", ":nine:", ":ten:"]


@__client.event
async def on_ready():
	print('Logged on as {0.user}!'.format(__client))


@__client.event
async def on_message(message: discord.Message):
	if message.author == __client.user:
		return
<<<<<<< Updated upstream

	if message.type != discord.MessageType.default:
		return
=======

	if message.type != discord.MessageType.default:
		return

	if message.content[0] == '!':
		# donc dans le cas où le message commence par !, c'est une commande
		# On va voir si c'est la commande qui nous intéresse
		_msg = message.content.split()  # ça permet de découper le message là où il y a des espaces
		if _msg[0] == '!timer':
			# donc le message commence par !timer suivi d'une espace
			await cmd_timer(message)
>>>>>>> Stashed changes

	if message.content[0] == '!':
		# donc dans le cas où le message commence par !, c'est une commande
		# On va voir si c'est la commande qui nous intéresse
		_msg = message.content.split()  # ça permet de découper le message là où il y a des espaces
		if _msg[0] == '!timer':
			# donc le message commence par !timer suivi d'une espace
			await cmd_timer(message)

			
async def cmd_timer(bot_message):
	# on va essayer de voir si il y a des arguments ajoutés (temps) car sinon, la commande ne doit pas fonctionner
	_msg = bot_message.content.split()
	if len(_msg) > 1:
		_args = _msg[1:]  # on recueille une liste des arguments ajoutés
		# on sait désormais que l'utilisateur veut utiliser !timer avec les arguments listés dans _args
		await bot_message.channel.send("Tu veux !timer avec les arguments %s" % _args)
		t = int(_args[0])
<<<<<<< Updated upstream
		if t > __timer_max:
			await bot_message.channel.send("impossible! (!help)")
			if t == 10:
				await bot_message.channel.send(":one::zero:")
				return
			if t == 9:
				await bot_message.channel.send(":nine:")
				return
		else:
			while t:
				time.sleep(1)
				t -= 1
			await bot_message.channel.send(f"Time's up! {_args[0]}s,{_args[1]} ")
=======
		while t:
			time.sleep(1)
			t -= 1
		await bot_message.channel.send("Time's up!")
>>>>>>> Stashed changes
	else:
		# donc l'utilisateur n'a pas mis d'arguments
		await bot_message.channel.send("Aw, t'as pas mis d'arguments a winnat !")

<<<<<<< Updated upstream
		@__client.event
		async def on_message(message: discord.Message):
			if message.author == __client.user:
				return
			if message.type != discord.MessageType.default:
				return
			if message.content[0] == '!':
				_msg = message.content.split()  # ça permet de découper le message là où il y a des espaces
				if _msg[0] == '!help':
					await bot_message.channel.send("test")



=======
>>>>>>> Stashed changes

__client.run(__token)
