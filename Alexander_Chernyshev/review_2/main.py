import telebot
import sqlite3
import time
from collections import OrderedDict


bot = telebot.TeleBot('701010387:AAEvXjhcdg5fnNCvZOJr0m7SN-qt6rsA5Us')

answer = False
flag = False


def handle_answer(message):
    global answer
    global flag
    if message.text == 'yes':
        answer = True
    elif message.text == 'no':
        answer = False
    else:
        msg = bot.send_message(message.chat.id, 'Pls answer yes or no')
        bot.register_next_step_handler(msg, handle_answer)
    flag = True


@bot.message_handler(commands=['play'])
def handle_play(message):
    game(bot, message.chat.id)


def get_parameters():
    with sqlite3.connect('charactersdata.db') as con:
        cur = con.cursor()
        parameter_list = [x[1] for x in cur.execute('PRAGMA table_info(characters)').fetchall()]
    return parameter_list


def make_question(parameter, value):
    if parameter == 'sex':
        question = 'Is your character {}?'.format(value)
    elif parameter == 'country':
        question = 'Is your character from {}?'.format(value)
    elif parameter == 'type':
        question = 'Is your character {}?'.format(value)
    elif parameter == 'age':
        question = 'Is your character {}?'.format(value)
    else:
        question = 'Your characters {0} is {1}?'.format(parameter, value)
    return question


def get_parameter_values(parameter, query_add):
    query = 'SELECT DISTINCT {} FROM characters'.format(parameter) + query_add
    with sqlite3.connect('charactersdata.db') as con:
        cur = con.cursor()
        values = [x[0] for x in cur.execute(query).fetchall()]
    return values


def game(bot, user_id):
    with sqlite3.connect('charactersdata.db') as con:
        cursor = con.cursor()
        global answer
        global flag
        current_params = OrderedDict()
        parameters = get_parameters()[1:]
        query = "SELECT name FROM characters"
        query_add = ""
        strings_count = len(cursor.execute(query).fetchall())
        pos = 0
        while strings_count > 1 and len(current_params) < len(parameters):
            current_parameter = parameters[pos]
            values = get_parameter_values(current_parameter, query_add)
            for v in values:
                print(values)
                question_message = make_question(current_parameter, v)
                msg = bot.send_message(user_id, question_message)
                bot.register_next_step_handler(msg, handle_answer)
                while not flag:
                    time.sleep(0.1)
                flag = False
                if answer:
                    if len(current_params) == 0:
                        query_add = ' WHERE ' + current_parameter + ' = ' + '\'' + v + '\''
                    else:
                        query_add += ' AND ' + current_parameter + ' = ' + '\'' + v + '\''
                    current_params[current_parameter] = v
                    pos += 1
                    break
            if not answer:
                break
            strings_count = len(cursor.execute(query + query_add).fetchall())
        if strings_count == 1:
            name = cursor.execute(query + query_add).fetchone()[0]
            bot.send_message(user_id, 'Your character is {}'.format(name))
        else:
            bot.send_message(user_id, 'Cant guess your character')


bot.polling(none_stop=True, interval=1)
