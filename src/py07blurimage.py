from PIL import Image, ImageFilter

before=Image.open("parishkar.jpg")
after=before.filter(ImageFilter.GaussianBlur(69))
after.save("parishkar2.jpg")