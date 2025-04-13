from PIL import Image, ImageDraw, ImageFont
image=Image.open("../files/test2.png")
print(image.format)
print(image.size)
print(image.mode)
# image.crop((0,0,1000,1000)).show()
# image.rotate(90).show()
image.transpose(Image.FLIP_LEFT_RIGHT).show()