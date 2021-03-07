import discord
import time
import embeds

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as [0.user]' .format(client))  # initializing bot


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content == '!p':
        start = time.time()  # start time for counting seconds

####################################################################################################

        def check(reaction1, user1):  # Pokemon 1
            return user1 == message.author and str(reaction1.emoji) == '⚡'

        await message.channel.send(embed=embeds.embed1, delete_after=15)
        await client.wait_for('reaction_add', check=check)
        await message.channel.send("Correct! Generating next level...", delete_after=10)
        time.sleep(1)

####################################################################################################

        def check(reaction2, user2):  # Pokemon 2
            return user2 == message.author and str(reaction2.emoji) == '🔥'

        await message.channel.send(embed=embeds.embed2, delete_after=15)
        await client.wait_for('reaction_add', check=check)
        await message.channel.send("Correct! Generating next level...", delete_after=10)
        time.sleep(1)

####################################################################################################

        def check(reaction3, user3):  # Pokemon 3
            return user3 == message.author and str(reaction3.emoji) == '🤡'

        await message.channel.send(embed=embeds.embed3, delete_after=15)
        await client.wait_for('reaction_add', check=check)
        await message.channel.send("Correct! Generating next level...", delete_after=10)
        time.sleep(1)

####################################################################################################

        def check(reaction4, user4):  # Pokemon 4
            return user4 == message.author and str(reaction4.emoji) == '🤖'

        await message.channel.send(embed=embeds.embed4, delete_after=15)
        await client.wait_for('reaction_add', check=check)
        await message.channel.send("Correct! Generating next level...", delete_after=10)
        time.sleep(1)

####################################################################################################

        def check(reaction5, user5):  # Pokemon 5
            return user5 == message.author and str(reaction5.emoji) == '🌵'

        await message.channel.send(embed=embeds.embed5, delete_after=15)
        await client.wait_for('reaction_add', check=check)
        await message.channel.send("Correct! Generating next level...", delete_after=10)
        time.sleep(1)

####################################################################################################

        def check(reaction6, user6):  # Pokemon 6
            return user6 == message.author and str(reaction6.emoji) == '💠'

        await message.channel.send(embed=embeds.embed6, delete_after=15)
        await client.wait_for('reaction_add', check=check)
        await message.channel.send("Correct! Generating next level...", delete_after=10)
        time.sleep(1)

####################################################################################################

        def check(reaction7, user7):  # Pokemon 7
            return user7 == message.author and str(reaction7.emoji) == '🎀'

        await message.channel.send(embed=embeds.embed7, delete_after=15)
        await client.wait_for('reaction_add', check=check)
        await message.channel.send("Correct! Generating next level...", delete_after=10)
        time.sleep(1)

####################################################################################################

        def check(reaction8, user8):  # Pokemon 8
            return user8 == message.author and str(reaction8.emoji) == '🧅'

        await message.channel.send(embed=embeds.embed8, delete_after=15)
        await client.wait_for('reaction_add', check=check)
        await message.channel.send("Correct! Generating next level...", delete_after=10)
        time.sleep(1)

####################################################################################################

        def check(reaction9, user9):  # Pokemon 9
            return user9 == message.author and str(reaction9.emoji) == '💫'

        await message.channel.send(embed=embeds.embed9, delete_after=15)
        await client.wait_for('reaction_add', check=check)
        await message.channel.send("Correct! Generating next level...", delete_after=10)
        time.sleep(1)

####################################################################################################

        def check(reaction10, user10):  # Pokemon 10
            return user10 == message.author and str(reaction10.emoji) == '🍳'

        await message.channel.send(embed=embeds.embed10, delete_after=15)
        await client.wait_for('reaction_add', check=check)
        await message.channel.send("Correct! Generating next level...", delete_after=10)
        time.sleep(1)

####################################################################################################

        def check(reaction11, user11):  # Pokemon 11
            return user11 == message.author and str(reaction11.emoji) == '👊'

        await message.channel.send(embed=embeds.embed11, delete_after=15)
        await client.wait_for('reaction_add', check=check)
        await message.channel.send("Correct! Generating next level...", delete_after=10)
        time.sleep(1)

####################################################################################################

        def check(reaction12, user12):  # Pokemon 12
            return user12 == message.author and str(reaction12.emoji) == '🦅'

        await message.channel.send(embed=embeds.embed12, delete_after=15)
        await client.wait_for('reaction_add', check=check)
        await message.channel.send("Correct! Generating next level...", delete_after=10)
        time.sleep(1)

####################################################################################################

        def check(reaction13, user13):  # Pokemon 13
            return user13 == message.author and str(reaction13.emoji) == '🥵'

        await message.channel.send(embed=embeds.embed13, delete_after=15)
        await client.wait_for('reaction_add', check=check)
        await message.channel.send("Correct! Generating next level...", delete_after=10)
        time.sleep(1)

####################################################################################################

        def check(reaction14, user14):  # Pokemon 14
            return user14 == message.author and str(reaction14.emoji) == '🐚'

        await message.channel.send(embed=embeds.embed14, delete_after=15)
        await client.wait_for('reaction_add', check=check)
        await message.channel.send("Correct! Generating next level...", delete_after=10)
        time.sleep(1)

####################################################################################################

        def check(reaction15, user15):  # Pokemon 15
            return user15 == message.author and str(reaction15.emoji) == '💣'

        await message.channel.send(embed=embeds.embed15, delete_after=15)
        await client.wait_for('reaction_add', check=check)
        await message.channel.send("Correct! Generating next level...", delete_after=10)
        time.sleep(1)

####################################################################################################

        stop = time.time()  # end time for counting seconds
        seconds = stop - start
        await message.channel.send("Congrats! You guessed all the pokemon in %d seconds." % seconds, delete_after=15)

####################################################################################################

client.run('token here')
