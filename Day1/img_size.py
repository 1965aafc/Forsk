#imprting libraries
import os
from PIL import Image  # uses pillow

#changing the particaular directory for the required file
os.chdir("F:\\Pictures\\pictures")

#name of the image file
image_file = "20181016_065548.jpg"

#using open function from PIL library to open the file
im = Image.open(image_file)

#printing the size of the image
print im.size # return value is a tuple, ex.: (1200, 800)

