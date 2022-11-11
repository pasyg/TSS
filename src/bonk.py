import random

BONKGIFS = ['https://tenor.com/view/bonk-mega-bonk-bonk-dog-bonkers-bonk-anime-gif-24565990',
            'https://tenor.com/view/bonk-gif-19410756',
            'https://images-ext-1.discordapp.net/external/rQiQjUl16giPYKygt00YIy99NqQcgTjhcmfv6vhk1vo/https/media.tenor.com/G32rcidDpqQAAAPo/donk-bonk.mp4',
            'https://tenor.com/view/despicable-me-minions-bonk-hitting-cute-gif-17663380',
            'https://tenor.com/view/cheems-bonk-doge-celestev69-gif-24399197'
            ]

async def bonk(message):
    if(message.author.id == 364227246791196683 or
       message.author.id == 342832667974434827):
        await message.channel.send(random.choice(BONKGIFS))