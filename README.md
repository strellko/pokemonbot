# : Pokemonbot
Simple discord bot that let's you play "Who's that Pokemon?" on your server. 

# : How it works

Start the game by sending the "!p" command. The first level will pop up as a discord embed. React to the message with the emoji corresponding to the pokemon silhouette in the thumbnail. You'll only progress to the next level if your guess is correct. You can also click on the thumbnail for larger preview of the photo. 

The main embed link also leads to an external pokedex website that can be found here: http://bit.ly/3eipciY

This is a timed game. Embeds will delete after 15 seconds, so don't be slow with your guesses! If the messages delete before you're able to guess, it's gameover. Use "!p" to restart! If you've made it to the end, the bot will reply with how long it took you to play, in seconds (elapsed time).

There are currently 15 "Who's that Pokemon?" questions that are a part of this bot. The code can be edited to include more / less. 

# : The Code

There are two python files in this repository:

1) main_code_bot.py

  > This is the main code for the bot, contains client events and the discord bot token.
 
2) embeds.py

  > This file lists all the embeds used in the main bot file. If you're looking to change the trivia, edit this file! Make your main_code_bot matches up to the number of embeds    you choose to have!
  > Here is a helpful embed generator, it'll save you some time: http://bit.ly/3qqsqDE







