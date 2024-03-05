from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

start_menu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
start_menu.row(KeyboardButton(text="Обрати товар"))
start_menu.add(KeyboardButton(text="Налаштування"),
               KeyboardButton(text="Зв'язок"))


tovar = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
tovar.add(KeyboardButton(text="Квіти"),
          KeyboardButton(text="Подарунки"),
          KeyboardButton(text="Подушки"))


select = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
select.add(KeyboardButton(text="Троянди"),
           KeyboardButton(text="Нарциси"),
           KeyboardButton(text="Гіпсофіли"),
           KeyboardButton(text="Повернутися"))

buy = InlineKeyboardMarkup()
buy.add(InlineKeyboardButton(text="Купити", callback_data="buy"))
