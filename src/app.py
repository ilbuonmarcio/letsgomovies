import os
import logging

from aiogram import Bot, Dispatcher, executor, types
from webparser import Film, TheSpaceWebParser


API_TOKEN = os.getenv('LETSGOMOVIES_BOT_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=['getmovies'])
async def get_movies(message: types.Message):
    parser = TheSpaceWebParser()
    movies = parser.get_movies()

    msg = "Ciao, questi sono i film attualmente presenti in sala!\n\nTheSpaceCinema:\n" \
                      + "\n".join([movie.render() for movie in movies])

    await message.reply(msg, parse_mode="Markdown", disable_web_page_preview=True)


if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)