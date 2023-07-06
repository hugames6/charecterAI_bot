import sqlite3 as sq

async def sql_start():
    global base, curs
    base = sq.connect('data.db')
    curs = base.cursor()
    if base:
        print('Connected')
    base.execute('CREATE TABLE IF NOT EXISTS user_data(user_id INTEGER PRIMARY KEY, username TEXT, name TEXT, surname TEXT, time DATETIME)')
    base.execute('CREATE TABLE IF NOT EXISTS user_text(iter_id INTEGER PRIMARY KEY NOT NULL, user_id INTEGER, bot_name TEXT, user_text TEXT, bot_answer TEXT, time DATETIME)')
    base.execute('CREATE TABLE IF NOT EXISTS bots(bot_name TEXT PRIMARY KEY, bot_hello TEXT)')
    base.commit()

async def sql_add_data(user_id, username, name, surname, date):
    try:
        base.execute('INSERT INTO user_data VALUES(?, ?, ?, ?, ?)', (user_id, username, name, surname, date))
        base.commit()
    except Exception:
        print('Юзер уже есть в базе.')
        user_is_registered = True
        return user_is_registered

async def sql_add_question(iter_id, user_id, bot_name, user_question, bot_answer, time):
    base.execute('INSERT INTO user_text VALUES(?, ?, ?, ?, ?, ?)', (iter_id, user_id, bot_name, user_question, bot_answer, time))
    base.commit()

async def sql_get_data_from_bots(bot_name):
    bot_name = f'{bot_name}'
    curs.execute(f"SELECT bot_hello FROM bots WHERE bot_name = ?", (bot_name, ))
    answer = curs.fetchone()
    return answer[0]
