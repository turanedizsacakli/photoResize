from PIL import Image


with Image.open("./foto.jpg") as img:
    extension=img.format.lower()
    resized=img.resize(size=(500, 300))
    resized.save(f"./resized.{extension}",format=extension)