
import discord

__token = "NzAzMDM2NTI1NzU0OTc0MjU5.XqIvyQ.kyxA3Bmi9mNSE9Tx3ir0vG3NlYE"
__client = discord.Client()

@__client.event
async def on_ready():
    print('Logged on as {0.user}!'.format(__client))

@__client.event
async def on_message(message: discord.Message):
    if message.author == __client.user:
        return

    if message.type != discord.MessageType.default:
        return

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
    else:
        # donc l'utilisateur n'a pas mis d'arguments
        await bot_message.channel.send("Aw, t'as pas mis d'arguments a winnat !")
        # voila le scripte pour le timer
        import time
        def countdown(t):
            while t:
                mins, secs = divmod(t, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end="\r")
                time.sleep(1)
                t -= 1

            print('aya ḥves!!!')
        await bot_message.channel.send("dayen ikefa")

        t = int(_args[0])

        if t >= 120: print("impossible")



        countdown(int(t))

__client.run(__token)