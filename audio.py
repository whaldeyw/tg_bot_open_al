import openai
from config import NEW_TOKEN
import json



openai.api_key = NEW_TOKEN

my_song = openai.api_key.Completion.create(
 prompt="Write a rap song:\n\n",
 max_tokens=200,
 temperature=0.5,
)
print(my_song.choices[0]["text"].strip())