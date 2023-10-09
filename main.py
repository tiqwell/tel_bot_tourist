import openai
import telebot

openai.api_key = ""
token = ""

# подключаемся к телеграму
bot = telebot.TeleBot(token=token)

def get_country(attractoins):
    messages = [{"role": "user", "content": f"Представь что ты туристический агент и человек хотел бы посмотреть это: {attractoins}, куда стоит ему поехать?"}]

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )

    return chat.choices[0].message.content

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Что бы ты хотел посмотреть?")

@bot.message_handler(content_types=["text"])
def send_country(message):
    country = get_country(message)

    bot.send_message(message.chat.id, country)

bot.polling(none_stop=True)