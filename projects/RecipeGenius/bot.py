from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from handlers import welcome, image_handler, question_answer, new_start
from bot.states import States

bot = Bot(token="7043394890:AAHfDBDYkDI08kE7eeqfKtHl_ij17YiIUUU")
dp = Dispatcher(bot, storage=MemoryStorage())

dp.register_message_handler(welcome, commands=["start"], state="*")
dp.register_message_handler(new_start, state=States.re_start)
dp.register_message_handler(image_handler, state=States.image, content_types="photo")
dp.register_message_handler(question_answer, state=States.work)

if __name__ == "__main__":
    executor.start_polling(dp)