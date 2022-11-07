from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import discord
from discord.ext import commands
import asyncio

chatbot = ChatBot("Billexa")

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")
"""
exit_conditions = (":q", "quit", "exit")

while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"Billexa: {chatbot.get_response(query)}")
"""
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot is Ready")

@client.command(aliases=['ai'])
async def chatter(ctx, *, chatInput):
    response = chatbot.get_response(chatInput)
    await ctx.send(f'Billexa: {chatbot.get_response(chatInput)}')

client.run("")
