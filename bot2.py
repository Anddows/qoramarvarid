import telebot
import sqlite3
import botprices


bot = telebot.TeleBot('5069229827:AAGeSTmQAFs-smOCQ1KoFa7OS9vtXZyLC8Y')

@bot.message_handler(commands = ['start'])
def start_message(message):
    connect = sqlite3.connect('usersid.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
          id INTEGER 
    )""")

    connect.commit()

    people_id = message.from_user.id
    cursor.execute(f"SELECT ID FROM login_id WHERE id = {people_id}")
    data = cursor.fetchone()
    if data is None:
        users_id = [message.from_user.id]
        cursor.execute("INSERT INTO login_id VALUES(?);", users_id)
        connect.commit()
        bot.reply_to(message, "Qora Marvarid")

    else:
        bot.reply_to(message, "Yana sizni ko'rayotganimizdan hursandmiz")

@bot.message_handler(content_types = ['text'])
def send_message(message):
    if message.text.lower() == "qora marvarid":
        bot.send_message(message.chat.id, "shu yerda")

    elif message.text.lower() == "m ban":
        bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, f"<b>{message.reply_to_message.from_user.first_name}</b> bloklandi",
                         parse_mode='HTML')

    elif message.text.lower() == "m unban":
        bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, f"<b>{message.reply_to_message.from_user.first_name}</b> Guruhga qayta oladi.",
                     parse_mode='HTML')

    elif message.text.lower() == "m kick":
        bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id, message.date + 1)
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, f"<b>{message.reply_to_message.from_user.first_name}</b> Guruhdan chiqarildi.",
                     parse_mode='HTML')

    elif message.text.lower() == "m mute":
        bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, f"<b>{message.reply_to_message.from_user.first_name}</b> siz endi yoza olmaysiz",
                         parse_mode='HTML')

    elif message.text.lower() == "m mute 1":
        bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, message.date + 600)
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, f"<b>{message.reply_to_message.from_user.first_name}</b> siz endi 1 soat yoza olmaysiz",
                         parse_mode='HTML')

    elif message.text.lower() == "m unmute":
        bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id)
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, f"<b>{message.reply_to_message.from_user.first_name}</b> endi yozishingiz mumkin",
                         parse_mode='HTML')

    elif message.text.lower() == "i0":
        bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id, can_delete_messages=None, can_pin_messages=None, can_restrict_members=None, can_manage_chat=None, can_manage_voice_chats = None, can_promote_members=None, can_edit_messages = None)
        bot.send_message(message.chat.id, f'<b> {message.reply_to_message.from_user.first_name} </b> admindan olindingiz',parse_mode='HTML')
        bot.delete_message(message.chat.id, message.message_id)

    elif message.text.lower() == "m pin":
        bot.delete_message(message.chat.id, message.message_id)
        bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)

    elif message.text.lower() == "m unpin":
        bot.delete_message(message.chat.id, message.message_id)
        bot.unpin_chat_message(message.chat.id, message.reply_to_message.message_id)

    elif message.text.lower() == "admin = w.reply":
        bot.promote_chat_member(message.chat.id, message.reply_to_message.from_user.id,can_delete_messages=True, can_pin_messages=True, can_restrict_members=True, can_manage_chat=True, can_manage_voice_chats = True, can_promote_members=True, can_change_info=True)
        bot.send_message(message.chat.id, f'<b> {message.reply_to_message.from_user.first_name} </b> successfully you are admin', parse_mode='HTML')
        bot.delete_message(message.chat.id, message.message_id)
        bot.set_chat_administrator_custom_title(message.chat.id, message.reply_to_message.from_user.id, "admin")

    elif message.text.lower() == "add.music":
        musics = bot.send_message(message.chat.id, "your music name >")
        bot.register_next_step_handler(musics, text)

    elif message.text.lower() == 'my musics':
        musics = bot.send_message(message.chat.id, "your music name >")
        bot.register_next_step_handler(musics, musicslist)

    elif message.text.lower() == 'list name':
        musics = bot.send_message(message.chat.id, "your list name >")
        bot.register_next_step_handler(musics, list2)


    elif message.text.lower() == 'bot => admin.reply':
        try:
            with open('https://www.pythonanywhere.com/user/ibrohim885/files/home/ibrohim885/bot/adminsid.py','a') as f:
                f.write(f'{message.reply_to_message.from_user.id},')
            bot.send_message(message.chat.id, "Done!")
            bot.delete_message(message.chat.id, message.message_id)
        except:
            bot.send_message(message.chat.id, "Commands error:" + " <em>'{bot = [i.r?]}</em>'", parse_mode='HTML')


def musicslist(message):
    list = message.text
    bot.send_message(message.chat.id, botprices.list)

def list2(message):
    listname = message.text
    with open('botprices.py', 'a') as f:
        f.write(f"{listname} = ")
    musiclink = bot.send_message(message.chat.id, "Done!")
    bot.register_next_step_handler(musiclink, textlink)

def text(message):
    musicname = message.text
    with open('botprices.py', 'a') as f:
         f.write(f"list = {musicname} = ")
    musiclink = bot.send_message(message.chat.id, "Done!")
    bot.register_next_step_handler(musiclink, textlink)

def textlink(message):
    musiclink = message.text
    with open('botprices.py', 'a') as f:
        f.write(f"'{musiclink}',\n\n")
    bot.send_message(message.chat.id, "Done!")






bot.polling(none_stop = True)

