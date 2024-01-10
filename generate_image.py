import os  
import requests 
from openai import OpenAI


client=OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="a beautiful and colored certificate base background with very small border, very small padding and a very large space for the content, the picture should have relation with AI. The frame should fill the entire image, without text, without title, without stamp and without signature",
  size = "1024x1024",
  quality="standard",
  n=1,
)
image_url = response.data[0].url

rep = requests.get(image_url)

with open("images/background.png","wb") as f :
    f.write(rep.content)
