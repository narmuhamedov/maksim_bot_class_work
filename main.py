from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import base, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from decouple import config
from database import db
from handlers import fsmadmin
from bot_instanse import dp
from keyboards import admin_kb



async def on_startup(_):
    db.sql_create()
    print('bot online')

fsmadmin.register_handlers_fsmadmin(dp)


#Забыл добавить кнопку для отображения в main.py
@dp.message_handler(commands=['show_all'])
async def show_database(message: types.Message):
    await db.sql_command_select(message)

# #начало викторины
# @dp.message_handler(commands=['quiz'])
# async def quiz_1(message: types.Message):
#     markup = InlineKeyboardMarkup()
#     button_call_1_2 = InlineKeyboardButton('Следующий вопрос', callback_data='button_call_1_2')
#     markup.add(button_call_1_2)
#     question = 'Зимой и летом одним цветом'
#     answer = ['Елка', "Тополь", 'Береза']
#     image = open('media/store-img1.webp', "rb")
#     await bot.send_photo(message.chat.id, photo=image)
#     await bot.send_poll(
#         message.chat.id,
#         question=question,
#         options=answer,
#         is_anonymous=False,
#         type='quiz',
#         correct_option_id=0,
#         open_period=90,
#         explanation='Не дам посказку это детская загадка',
#         explanation_parse_mode=ParseMode.MARKDOWN_V2,
#         reply_markup=markup
#     )
#
# @dp.callback_query_handler(lambda func: func.data=='button_call_1_2')
# async def quiz2(call: types.CallbackQuery):
#     markup = InlineKeyboardMarkup()
#     button_call_2_3 = InlineKeyboardButton('Следующий вопрос', callback_data='button_call_2_3')
#     markup.add(button_call_2_3)
#     question = 'Сидит дет в 100 шуб одет кто его раздевает тот слезы проливает'
#     answer = ['огурец', 'помидор', 'лук', 'перец']
#     image = open('media/store-img2.webp', "rb")
#     await bot.send_photo(call.message.chat.id, photo=image)
#     await bot.send_poll(
#         call.message.chat.id,
#         question=question,
#         options=answer,
#         is_anonymous=False,
#         type='quiz',
#         correct_option_id=2,
#         open_period=90,
#         explanation='Используется везде',
#         explanation_parse_mode=ParseMode.MARKDOWN_V2,
#         reply_markup=markup
#     )
#
#     @dp.callback_query_handler(lambda func: func.data == 'button_call_2_3')
#     async def quiz3(call: types.CallbackQuery):
#         question = 'Продолжи фразу "Расскажи снегурочка где........" '
#         answer = ['спала', 'была', 'кушала', 'ночевала']
#         image = open('media/store-img3.webp', "rb")
#         await bot.send_photo(call.message.chat.id, photo=image)
#         await bot.send_poll(
#             call.message.chat.id,
#             question=question,
#             options=answer,
#             is_anonymous=False,
#             type='quiz',
#             correct_option_id=1,
#             explanation='Из ну погоди',
#             explanation_parse_mode=ParseMode.MARKDOWN_V2,
#         )

#конец викторины


# @dp.message_handler(commands=['start'])
# async def hello(message: types.Message):
#     await bot.send_message(message.chat.id, f'Здорва тебя приветствует {message.from_user.full_name}')


# @dp.message_handler()
# async def echo_message(message: types.Message):
#     await message.answer(message.text.lower())

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)