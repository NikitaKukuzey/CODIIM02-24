from aiogram import types
from aiogram.dispatcher import FSMContext
from utils import messages, utils
from bot.states import States
from model.predictor import MyModel
from giga_chat import gigachat
import os

menu = {    'apple_pie': 'яблочный пирог',
    'caesar_salad': 'салат "Цезарь"',    'caprese_salad': 'салат "Капрезе"',
    'carrot_cake': 'морковный пирог',    'cheesecake': 'чизкейк',
    'chicken_curry': 'куриное карри',    'chocolate_cake': 'шоколадный пирог',
    'chocolate_mousse': 'шоколадный мусс',    'donuts': 'пончики',
    'dumplings': 'пельмени',    'eggs_benedict': 'яичница по-бенедиктински',
    'greek_salad': 'греческий салат',    'lasagna': 'лазанья',
    'pancakes': 'блины',    'panna_cotta': 'панна котта',
    'peking_duck': 'утка по-пекински',    'pizza': 'пицца',
    'ramen': 'рамен',    'risotto': 'ризотто',
    'waffles': 'вафли'}


async def welcome(msg: types.Message):
    await States.work.set()
    await msg.answer(messages.start,reply_markup=utils.form_reply_keyboard(["Начать"]))

async def new_start(msg: types.Message):
    await States.work.set()
    await msg.answer(messages.re_start,reply_markup=utils.form_reply_keyboard(["Загрузить ещё одну картинку"]))
async def image_handler(msg: types.Message, state: FSMContext):

    images = msg.photo

    if images is None:
        await msg.reply("Это не фото")
        return 0

    model = MyModel("model/model.joblib")

    image = images[-1]
    path = f"{msg.from_user.id}.jpeg"

    await image.download(destination_file = path)

    async with state.proxy() as data:
        sign = data["sign"]

    prediction = model(path)

    os.remove(path)

    await msg.reply(messages.prediction.format(menu[prediction]+"\n"+gigachat(prediction)))
    await new_start(msg)


async def question_answer(msg: types.Message, state: FSMContext):

    await States.question.set()
    sign = "Загрузить ещё одну картинку" in msg.text

    async with state.proxy() as data:
        data["sign"] = sign

    await States.image.set()

    await msg.reply(messages.image)