import telebot
from telebot import types # для указание типов




bot = telebot.TeleBot('7365286742:AAEv6qWBpvodpRNinVveNPhsAsF5LLMpv8U')
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Начать")
    btn2 = types.KeyboardButton("Все команды")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="🤗Привет {0.first_name},очень рады видеть тебя!🤗\n\n\n ✨Добро пожаловать в наш Telegram-бот, посвященный нейросетям и искусственному интеллекту!🤖.\n\n Бот вам расскажет: \n🔍 Инсайты и новости из мира нейросетей;\n🧠 Обучающие материалы и пошаговые руководства по созданию и обучению моделей;\n🚀 Практические примеры применения ИИ в различных сферах;\n🛠️ Советы по выбору инструментов и платформ для работы с нейросетями;\n💬 Обсуждения актуальных тем и технологий с единомышленниками.\n\n 📈Присоединяйся к нам)📈".format(message.from_user), reply_markup=markup)
@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Начать"):
        # Создать объект клавиатуры
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # Добавить кнопку
        button = types.KeyboardButton("✅Проверить✅")  # замените "Кнопка 1" на ваше название кнопки
        markup.add(button)
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("Новости IT", url='https://t.me/+Mtg-RebYFm04NGEy')
        markup.add(button1)
        bot.send_message(message.chat.id, "🔈Что бы бот работал, подпишись на все представленные ниже телеграмм каналы🔈".format(message.from_user), reply_markup=markup)


        # Отправить пользователю сообщение с клавиатурой
    elif (message.text == "✅Проверить✅"):
        
        bot.send_message(message.chat.id, "⛔️Вы не подписались на все каналы⛔️")

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    # Создаем кнопку
    button = types.KeyboardButton('✅Проверить✅')
    
    # Добавляем кнопку на клавиатуру
    keyboard.add(button)
    
    # Отправляем сообщение с кнопкой
    bot.send_message(message.chat.id, "Жми    ✅Проверить✅,    если подписался на все каналы", reply_markup=keyboard)
    if (message.text == "Все команды"):
        
        bot.send_message(message.chat.id, "⛔️Вы не подписались на все каналы⛔️")
         
    

bot.polling(none_stop=True)