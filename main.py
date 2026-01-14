import telebot
from telebot.types import Message


bot = telebot.TeleBot(token="8218998010:AAE4qGXLCvj4WIeOfvlV-sJqj5_07UlAA0k")

@bot.message_handler(commands=["start"])
def start_handler(message: Message):
    bot.send_message(message.chat.id, f"ASSALOMU ALAYKUM !!! {message.from_user.full_name}!")


@bot.message_handler(commands=["info"])
def info_handler(message: Message):
    bot.send_message(message.chat.id, f"men Bekking tomonidan yaratilgan botman\n"
                                        f"men Bekkingni birinchi loyihasiman")

@bot.message_handler(commands=["support"])
def support_handler(message: Message):
    bot.send_message(message.chat.id, f"qollab-quvatlash bilan bog'lanish uchun @b5644 ga murojaat qiling")

@bot.message_handler(commands=['profile'])
def profile_handler(message):
    user = message.from_user
    first_name = user.first_name if user.first_name else ""
    last_name = user.last_name if user.last_name else ""
    username = f"@{user.username}" if user.username else ""
    user_id = user.id
    bot.send_message(message.chat.id, f"Malumotlaringiz\n"
                                        f"{"⌄"*33}\n"
                                        f"Ismingiz:> {first_name}\n"
                                        f"Familyangiz:> {last_name}\n"
                                        f"Foydalanuvchi nomingiz:> {username}\n"
                                        f"Telegram id:> {user_id}\n"
                                        f"{"^ "*35}\n")        





@bot.message_handler()
def echo(message: Message):
    bot.send_message(message.chat.id, f"Menda bunday buyruq yoq!!!\n"
                                        f"Biz yuborishingiz mumkin bolgan buyruqlar\n"
                                        f"{"⌄"*33}\n"
                                        f"Buyruq 1) /start ---> botni yangilash\n"
                                        f"Buyruq 2) /info ---> bot haqida malumot olish uchun\n"
                                        f"Buyruq 3) /support ---> qollab-quvvatlash bilan bog'lanish\n"
                                        f"Buyruq 4) /profile ---> malumotlaringizni korish\n"
                                        f"{"^ "*35}\n")





print("bot ishga tushdi")
bot.infinity_polling()


