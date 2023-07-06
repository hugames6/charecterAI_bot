import openai

openai.api_key = ''

async def get_mario_answer(question):
    prompt = openai.Completion.create(
        model = "text-davinci-003",
        prompt = f'Instructions: You are Mario from Super Mario. Type on Russian. Do not give dangerous information. User message: {question}',
        temperature =0.9,
        max_tokens = 1000,
        top_p = 1,
        frequency_penalty = 0.0,
        presence_penalty = 0.6
    )
    answer = prompt['choices'][0]['text'].split('\n')[2]
    return answer

async def get_einstein_answer(question):
    prompt = openai.Completion.create(
        model = "text-davinci-003",
        prompt = f'Instructions: You are Albert Einstein. Type on Russian. Do not give dangerous information. User message: {question}',
        temperature =0.9,
        max_tokens = 1000,
        top_p = 1,
        frequency_penalty = 0.0,
        presence_penalty = 0.6
    )
    answer = prompt['choices'][0]['text'].split('\n')[2]
    return answer
