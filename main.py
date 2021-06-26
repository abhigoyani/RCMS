import discord
import re
from verify_util import verify_start_game
from insert import insert_new_temp
import os

client = discord.Client()

roll = ['RAJA','CHOR','MANTRI','SIPAHI']

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('RCMS start '):
    msg = message.content.split('RCMS start ',1)[1]
    msg = msg.split(' ')
    print(msg)
    if not len(set(msg)) == 3:
      await message.channel.send('We need total 4 players')
      return
    for i in  range(3):
      if re.findall('<@!.*?>', msg[i]):
        msg[i] = msg[i][3:-1]
        
      else:
        await message.channel.send('invalid input......')
        return

    sts = verify_start_game(message.author.id,msg[0],msg[1],msg[2])
    
    if sts == False:
        await message.channel.send('somthing went wrong...')
    
    elif sts != True:
        await message.channel.send('<@!{}> is alerady in a game...'.format(sts))
    
    else:
        sts_in = insert_new_temp(message.author.id,msg[0],msg[1],msg[2])
        if not sts_in:
            await message.channel.send('somthing  went wrong...')
        else:
            await message.channel.send('<@!{}>, <@!{}> and <@!{}> you are invited for a game by <@!{}>, ```type RCMS accept <@!{}>``` to start the game'.format(msg[0],msg[1],msg[2],message.author.id,message.author.id))

    


      

client.run(os.environ['botToken'])