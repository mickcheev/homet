from aiogram import Bot, Dispatcher, executor, types

from telebot.interfaces import authentication, manage_notes

API_TOKEN = ''

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def say_hello(message: types.Message):
    return await message.answer('Hello, you are using quick-notes taking bot, please, register your account via login '
                                'form and bound it')


@dp.message_handler(commands=['bound'])
async def bound_with_telegram(message: types.Message):
    try:
        key = message.text.split(' ')[1]
    except IndexError:
        return await message.answer('You have entered Invalid key format'
                                    '\nYou must enter like in example:\n'
                                    '/bound <key>')

    return await message.reply(authentication.bound_account(key, telegram_id=message.from_user.id))


@dp.message_handler(content_types=['text'])
@authentication.check_reg()
async def add_new_quick_note(message: types.Message, user):
    manage_notes.make_note(message.text, user)
    return await message.answer('You have created new quick-note 📗')


@dp.message_handler(commands=['del'])
async def delete_last_note(message: types.Message):
    pass

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
