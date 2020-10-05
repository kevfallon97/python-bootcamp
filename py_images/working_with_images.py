
# Use the Pillow library
# pip install pillow
# documentation @ pillow.readthedocs.io

from PIL import Image

mac = Image.open("example.jpg") # specialised Pillow object

# mac.show() # used to display the image
# mac.size # size of the image in pixels (width, height)
# mac.format_description # provide info on the image format

# CROPPING IMAGES
mac.crop((0,0,100,100))

pencils = Image.open("pencils.jpg")
print(pencils.size)

# co-ordinates for crop
x = 0
y = 0

w = 1950 / 3
h = 1300 / 10

pencils_crop = pencils.crop((x,y,w,h))
pencils_crop.show()

# pencils_crop.save("filepath")