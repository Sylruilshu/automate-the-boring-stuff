import os, PIL
from PIL import Image


IMAGE_SIZE_PIXELS = 500


for foldername, subfolders, filenames in os.walk("C:\\"):
    num_photo_files = 0
    num_non_photo_files = 0
    for filename in filenames:
        # Check if file extension isn't .png or .jpg.
        if not (
            filename.endswith((".jpg", ".JPG")) or filename.endswith((".png", ".PNG"))
        ):
            num_non_photo_files += 1
            continue  # skip to next filename

        # Open image file using Pillow.
        try:
            image = Image.open(
                os.path.join(
                    "C:\\",
                    foldername,
                    filename,
                )
            )
        except PIL.UnidentifiedImageError:
            continue

        width, height = image.size
        # Check if width & height are larger than 500.
        if width > IMAGE_SIZE_PIXELS and height > IMAGE_SIZE_PIXELS:
            # Image is large enough to be considered a photo.
            num_photo_files += 1
        else:
            # Image is too small to be a photo.
            num_non_photo_files += 1

    # If more than half of files were photos,
    # print the absolute path of the folder.
    total_files = num_non_photo_files + num_photo_files

    if num_photo_files != 0 and num_photo_files / total_files > 0.5:
        print(os.path.join("C:\\", foldername))
