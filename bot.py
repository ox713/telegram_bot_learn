import telebot
import random
import config
import countries

from telebot import types
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=["start"])
def menu(message):
    sticker = open('static/sticker.webp', 'rb')
    #bot.send_sticker(message.chat.id, sticker)

    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Страны мира")
    item2 = types.KeyboardButton("2")
    item3 = types.KeyboardButton("3")
    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, "What game do you wanna play?", reply_markup=markup)# \nСтраны мира \n2 \n3",


@bot.message_handler(content_types=['text'])
def message_handler(message):
    if message.chat.type == 'private':
        if message.text == "Страны мира":
            #bot.send_message(message.chat.id, "Yes")
            countries_quiz(message)


#@bot.message_handler(commands=["start"])


def countries_quiz(message):
    temp_country = random.choice(list(countries.europe.keys()))
    bot.send_message(message.chat.id, f"Какя сталица у {temp_country}?")
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call):
#     try:
#         if call.message:
#             if call.data == 'Берлин':
#                 bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
#             elif call.data == 'bad':
#                 bot.send_message(call.message.chat.id, 'Бывает 😢')
#
#             # remove inline buttons
#             bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
#                                   reply_markup=None)
#     except Exception as e:
#         print(repr(e))

if __name__ == '__main__':
    bot.infinity_polling()