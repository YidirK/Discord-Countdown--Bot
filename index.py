
import discord

__token = "NzAzMDM2NTI1NzU0OTc0MjU5.XqIvyQ.kyxA3Bmi9mNSE9Tx3ir0vG3NlYE"
__client = discord.Client()

@__client.event
async def on_ready():
    print('Logged on as {0.user}!'.format(__client))

    @__client.event
    async def on_member_join(member):
        for channel in member.guild.channels:
            if str(channel) == "timer":  # We check to make sure we are sending the message in the general channel
                await channel.send_message(f"""Welcome to the server this is test {member.mention}""")

                @__client.event
                async def on_message(message: discord.Message):
                    if message.content == "!help":
                        embed = discord.Embed(title="Help of BOT", description="commands of bot")
                        embed.add_field(name="!timer <n>M", value="Start a countdown with length 'n'M")
                        embed.add_field(name="!stop", value="stop a contdown")
                        await message.channel.send(content=None, embed=embed)



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
              await  cmd_timer(message)



async def cmd_timer(bot_message):
    _msg = bot_message.content.split()
    # on va essayer de voir si il y a des arguments ajoutés (temps) car sinon, la commande ne doit pas fonctionner
    if len(_msg) > 1:
        _args = _msg[1:]  # on recueille une liste des arguments ajoutés
        # on sait désormais que l'utilisateur veut utiliser !timer avec les arguments listés dans _args
        await bot_message.channel.send("Tu veux !timer avec les arguments %s" % _args)
    else:
        # donc l'utilisateur n'a pas mis d'arguments
        await bot_message.channel.send("Aw, t'as pas mis d'arguments a winnat! \"!help\" for a list.")

__client.run(__token)


