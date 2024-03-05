from aiogram import types, Dispatcher, Bot, executor
import config as cfg
import markup as nav


bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await bot.send_message(message.from_user.id, f"Привіт, це бот від користувача @defbysby.", reply_markup=nav.start_menu)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        number = message.text
        await bot.send_message(message.from_user.id, f"Ви обрали {number} квіток.", reply_markup=nav.buy)
    if message.text == "Обрати товар":
        await bot.send_message(message.from_user.id, f"Виберіть один з товарів:", reply_markup=nav.tovar)
    if message.text == "Квіти":
        await bot.send_message(message.from_user.id, f"Виберіть квіти:", reply_markup=nav.select)
    if message.text == "Троянди":
        await bot.send_message(message.from_user.id, f"Ви обрали квітку: Троянди\n"
                                                     f"Введіть скільки квіток ви хочете купити:")
    if message.text == "Нарциси":
        await bot.send_message(message.from_user.id, f"Ви обрали квітку: Нарциси\n"
                                                     f"Введіть скільки квіток ви хочете купити:")
    if message.text == "Гіпсофіли":
        await bot.send_message(message.from_user.id, f"Ви обрали квітку: Гіпсофіли\n"
                                                     f"Введіть скільки квіток ви хочете купити:")
    if message.text == "Налаштування":
        await bot.send_message(message.from_user.id, f"Наші контакти: @defbysby")
    if message.text == "Повернутися":
        await bot.send_message(message.from_user.id, f"Виберіть один з товарів:", reply_markup=nav.tovar)


@dp.callback_query_handler(text="buy")
async def cmd_buy(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, f"Ви придбали!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

