import telebot
from extensions import keys, TOKEN
from utils import ConvertionException, CurrencyConverter
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Для начала работы введите команду в формате:\n<название валюты> \
<в какую валюту перевести> \
<количество переводимой валюты> \n Получить список доступных валют: /values'
    bot.reply_to(message,text)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Для начала работы введите команду в формате:\n<название валюты> \
<в какую валюту перевести> \
<количество переводимой валюты> \n Получить список доступных валют: /values'
    bot.reply_to(message,text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Вы ввели неверное количество параметров.')

        quote, base, amount = values
        amount = float(amount)
        total_base = float(CurrencyConverter.convert(quote, base, amount))
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base*amount}'
        bot.send_message(message.chat.id, text)

bot.polling()