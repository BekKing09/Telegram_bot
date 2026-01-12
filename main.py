import telebot
from telebot.types import Message

bot = telebot.TeleBot(token="8218998010:AAE4qGXLCvj4WIeOfvlV-sJqj5_07UlAA0k")

@bot.message_handler(commands=["start"])
def start_handler(message: Message):
    bot.send_message(message.chat.id, f"assalomu alaykum {message.from_user.full_name}!")


@bot.message_handler(commands=["info"])
def info_handler(message: Message):
    bot.send_message(message.chat.id, f"men Bekking tomonidan yaratilgan botman\n"
                                        f"men Bekkingni birinchi loyihasiman")

@bot.message_handler(commands=["support"])
def support_handler(message: Message):
    bot.send_message(message.chat.id, f"qollab-quvatlash bilan bog'lanish uchun @b5644 ga murojaat qiling")


@bot.message_handler()
def echo(message: Message):
    bot.send_message(message.chat.id, f"menda bunday buyruq yoq\n"
                                        f"siz yuborishingiz mumkin bolgan buyruqlar\n"
                                        f"buyruq 1) /start ---> botni yangilash\n"
                                        f"buyruq 2) /info ---> bot haqida malumot olish uchun\n"
                                        f"buyruq 3) /support ---> qollab-quvvatlash bilan bog'lanish")





print("bot ishga tushdi")
bot.infinity_polling()


