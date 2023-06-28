import discord
import requests
from discord.ext import commands
import os
import asyncio
import multiprocessing

os.system('python depend.py')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author.id != 270904126974590976:
            return

        if message.embeds:
            for embed in message.embeds:
                if embed.description is not None and "giveaway" in embed.description.lower():
                    print("Clicking the first button on the giveaway embed...")
                    await message.components[0].children[0].click()
                    print('done')

async def run_bot(token):
    client = MyClient()
    await client.start(token)

if __name__ == '__main__':
    tokens = [os.environ['token1'], os.environ['token2']]  # Add more tokens as needed
    processes = []

    for token in tokens:
        process = multiprocessing.Process(target=asyncio.run, args=(run_bot(token),))
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()
