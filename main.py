import telebot
from telebot.types import Message
from googletrans import Translator


translator = Translator()

def translate_to(text: str, lang="uz"):
    return translator.translate(text=text, dest=lang).text




bot = telebot.TeleBot(token="bot token")


@bot.message_handler(commands=["start"])
def start_handler(message: Message):
    bot.send_message(message.chat.id, f"Assalomu alaykum {message.from_user.full_name}!\n"
                     "Men tarjimon botman. Istalgan matnni rus tiliga tarjima qilaman.\n"
                     "Yuborilgan matnni shunchaki qaysi tilga tarjima qilish kerakligini yuboring!\n")




@bot.message_handler()
def get_all_texts(message: Message):

    translated_text = translate_to(message.text, lang="ru")

    bot.send_message(message.chat.id, translated_text)











print("bot ishga tushdi")
bot.infinity_polling()


