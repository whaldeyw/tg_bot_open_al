from base64 import b64decode

import openai
from config import API_TOKEN
import json



piompt = input('Какую картинку сгенерируем? ')
openai.api_key = API_TOKEN

response = openai.Image.create(
    prompt=piompt,
    n=1,
    size='256x256',
    response_format='b64_json'
)

with open('promt.json', 'w') as file:
    json.dump(response, file, indent=4, ensure_ascii=False)

image_data = b64decode(response['data'][0]['b64_json'])
file_name = '_'.join(piompt.split(' '))

with open(f'{file_name}.png', 'wb') as file:
    file.write(image_data)