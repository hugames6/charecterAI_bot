# charecterAI_bot
Телеграм бот разработанный мною в свободное время.

Использованные библиотеки:
Aiogram
SQLite3
openai
Amplitude

С ботом можно общаться, и он будет давать оригинальные ответы от лица одного из двух персонажей. Для выбора необходимо нажать на соотвутсвующую кнопку, после чего выбрать бота в WebApp. Персонажа можно поменять в любой момент.

Каждый новый пользователь попадает в БД. В этой же БД содержится приветствие для каждого персонажа. В третью таблицу заносится вопрос пользователя и ответ бота.

Так же каждое действие отправляется в Amplitude, с одноимёнными ивентами: Регистрация, Выбор персонажа, Вопрос, Ответ.
