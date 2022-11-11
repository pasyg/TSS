import discord
from TOKEN import get_token
from bonk import bonk

INTENTS = discord.Intents().all()

class Client(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print('----------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        if message.content.casefold().startswith('hi'):
            await message.channel.send('hi')
        if message.content.casefold().startswith('lol'):
            await bonk(message)

if __name__ == '__main__':
    client = Client(intents=INTENTS)
    client.run(get_token())