import openai
from config import API_TOKEN
import json
from base64 import b64decode
from aiogram import types, Dispatcher, executor, Bot
from config import TOKEN_BOT

bot = Bot(TOKEN_BOT)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message : types.Message):
    await bot.send_message(message.from_user.id, f'Привет 👋 {message.from_user.first_name} я нейросеть  🛰 которая умеет пока что только генерировать '
                                                 f'картинки из текста ✍️, но я буду развиваться  😜 '
                                                 f'напиши мне текст любой картинки, например: Хочу видеть фото заката ')

@dp.message_handler()
async def sta(message : types.Message):

    piompt = message.text
    openai.api_key = API_TOKEN

    response = openai.Image.create(
        prompt= piompt,
        n=1,
        size = '256x256',
        response_format='b64_json'
    )

    with open('promt.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    image_data = b64decode(response['data'][0]['b64_json'])
    file_name = '_'.join(piompt.split(' '))



    with open(f'{file_name}.png', 'wb') as file:
        file.write(image_data)

    await bot.send_photo(message.from_user.id, image_data)

def generite_response(text):
    openai.api_key = API_TOKEN
    response = openai.Completion.create(
        promt=text,
        engine='text-davinci-003',
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=15
    )
    if response and response.choises:
        return response.choises[0].text.strip()
    else:
        return None

res = generite_response('Привет как у тебя дела?')

print(res)

executor.start_polling(dp, skip_updates=None)