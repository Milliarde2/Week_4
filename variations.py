import requests
import openai
from openai import OpenAI

client=OpenAI()

response = client.images.create_variation(
    image = open ("images/background.png","rb"),
    n=1,
    model="dall-e-2",
    size="1024x1024"
)

image_url = response.data[0].url

rep = requests.get(image_url)

with open("images/background_mod.png","wb") as f :
      f.write(rep.content)


