import telebot
from telebot.types import Message



bot = telebot.TeleBot(token="bot token")



@bot.message_handler(commands=["start"])
def get_text(message: Message):
    bot.send_message(message.chat.id, f"salom {message.from_user.full_name}\n"
                                        f"menga savol bering javob beraman")








questions = [
    ["python nima", "python bu dasturlash tili"],
    ["algoritm nima", "algoritm bu ketma ketlik"],
    ["abdulloh AIdan ko'chiradimi", "ha albatta"],
    ["isnming nima", "savol javob oyiniman"]
]


def get_question(text: str):
    for i in questions:
        if i[0] in text:
            return i
    return


@bot.message_handler()
def get_text(message: Message):
    answer = get_question(text=message.text)

    if not answer:
        bot.send_message(message.chat.id, "Bunday savol topilmadi!")
        return
    
    bot.send_message(message.chat.id, answer[1])




print("bot ishga tushdi")
bot.infinity_polling()


