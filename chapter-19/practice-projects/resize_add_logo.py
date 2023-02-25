import os
from PIL import Image


SQUARE_FIT_SIZE = 300
LOGO_FILENAME = "cat_logo.png"


logo = Image.open(f"images/{LOGO_FILENAME}")
logo_width, logo_height = logo.size

os.makedirs("images-with-logo", exist_ok=True)
for filename in os.listdir("images/."):
    if (
        not (filename.endswith((".png", ".PNG")) or filename.endswith((".jpg", ".JPG")))
        or filename == LOGO_FILENAME
    ):
        continue

    image = Image.open(f"images/{filename}")
    width, height = image.size

    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        print(f"Resizing ... {filename}")
        image = image.resize((width, height))

    if width > logo_width * 2 and height > logo_height * 2:
        print(f"Adding logo to ... {filename}")
        image.paste(logo, (width - logo_width, height - logo_height), logo)

        image.save(os.path.join("images-with-logo", filename))
