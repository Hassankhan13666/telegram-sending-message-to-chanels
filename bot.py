from telethon import TelegramClient, events

api_id = ""
api_hash = ''
source_channel = '@janjanjan1234'
target_channel = '@hhhhhhhhhhhhddddssxc'


client = TelegramClient('hasan', api_id, api_hash)

@client.on(events.NewMessage(chats=source_channel))
async def handler(event):
 
    message_text = event.message.message
   
    media = event.message.media


    await client.send_message(target_channel, message_text, file=media)


client.start()
client.run_until_disconnected()
