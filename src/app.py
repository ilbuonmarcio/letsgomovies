import logging
import os

from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = os.getenv('LETSGOMOVIES_BOT_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dispatcher = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_cities_list(message: types.Message):
    await message.reply("Hi, LetsGoMovies here!\nSelect your city below:")


if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)