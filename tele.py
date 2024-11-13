import asyncio
import telegram


TOKEN = "5945035651:AAH_4sACRXJgOhqySEDatrE-ZBN2tH8Jbn0"
chat_id = '1234647619'

# Channel ID Sample: -1001829542722

bot = telegram.Bot(token=TOKEN)

class TelePy:
    def __init__(self, msg):
        asyncio.run(self.main(msg))

    async def send_message(text, chat_id):
        async with bot:
            await bot.send_message(text=text, chat_id=chat_id)


    async def main(self, msg):
        # Sending a message
        await self.send_message(text=msg, chat_id=chat_id)

            # Sending a document
        # await send_document(document=open('/path/to/document.pdf', 'rb'), chat_id=chat_id)

            # Sending a photo
            #await send_photo(photo=open('/path/to/photo.jpg', 'rb'), chat_id=chat_id)

            # Sending a video
            #await send_video(video=open('path/to/video.mp4', 'rb'), chat_id=chat_id)
