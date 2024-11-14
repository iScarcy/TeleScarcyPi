import asyncio
import telegram
import configparser


config = configparser.ConfigParser()
config.sections()
config.read('config.ini')
# Channel ID Sample: -1001829542722
TOKEN   = config['TELEGRAM']['TelegramAccessTocken']
chat_id = config['TELEGRAM']['TelegramChatId']

bot = telegram.Bot(token=TOKEN)

class TeleP:
    def __init__(self, msg):
        self.message = msg
        asyncio.run(self.main())

    async def send_message(self,text, chat_id):
        async with bot:
            await bot.send_message(text=text, chat_id=chat_id)



    async def main(self):
        # Sending a message
        await self.send_message(self.message, chat_id=chat_id)

    
        