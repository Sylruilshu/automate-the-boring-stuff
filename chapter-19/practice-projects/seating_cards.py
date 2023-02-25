import os
from PIL import Image, ImageFont, ImageDraw


FONTS_DIR = "Windows/Fonts"


with open("guests.txt", "r") as text_file:
    names = text_file.readlines()

arial_font = ImageFont.truetype(os.path.join(FONTS_DIR, "Amiri-Regular.ttf"), 34)

os.makedirs("seating-cards", exist_ok=True)

for name in names:
    name = name.strip("\n")

    image = Image.open("flower.jpg")
    resized_image = image.resize((360, 360))

    draw = ImageDraw.Draw(resized_image)

    text_size = draw.textsize(name, arial_font)

    center = ((180 - (text_size[0] / 2)), (180 - (text_size[1] / 2)))

    draw.rectangle((0, 0, 359, 359), outline="black", width=3)
    draw.text(center, name, fill="skyblue", font=arial_font)

    resized_image.save(os.path.join("seating-cards", f"{name}_card.png"))
