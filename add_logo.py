import os
from PIL import Image


# resize the logo.png 
logo1 = Image.open('images/logo.png')
logo2=logo1.resize((300,150))
logo2.save('images/logo_300.png')

# import the background
im = Image.open('images/background.png')

#paste the logo onto the background
im.paste(logo2,(0,0),logo2)

os.makedirs("images/withlogo", exist_ok = True)
im.save(os.path.join('images/withlogo','backlogo.png'))

