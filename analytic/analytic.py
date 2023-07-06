from amplitude import Amplitude, BaseEvent

amplitude = Amplitude("cd83e2bdd790698a8289d7548056853d")


async def user_registration(user_id):
    amplitude.track(BaseEvent(
        event_type="Регистрация пользователя",
        user_id=f"{user_id}"))
    
async def user_choise(user_id):
    amplitude.track(BaseEvent(
        event_type="Пользователь выбирает персонажа",
        user_id=f"{user_id}"))
    
async def user_send_question(user_id):
    amplitude.track(BaseEvent(
        event_type="Пользователь отправил вопрос",
        user_id=f"{user_id}"))

async def we_get_API_answer(user_id):
    amplitude.track(BaseEvent(
        event_type="Получаем запрос по API",
        user_id=f"{user_id}"))

async def send_answer_to_user(user_id):
    amplitude.track(BaseEvent(
        event_type="Отправляем ответ пользователю",
        user_id=f"{user_id}"))
