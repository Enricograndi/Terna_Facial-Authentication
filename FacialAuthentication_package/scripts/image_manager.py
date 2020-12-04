import os
from PIL import Image


def image_weight(image):
    input_image = 'check.jpg'
    dimension_kb = os.stat(image).st_size
    dimension_mb = dimension_kb/(1024*1024)
    return dimension_mb


def comprime_image(input_image):
    size = image_weight(input_image)
    while size > 3.4:
        picture = Image.open(input_image)
        picture.save(input_image,optimize=True,quality=30)
        size = image_weight(input_image)        
    return input_image

def save_img_tmp(image):
    img = Image.open(image)
    img.save('data/tmp/to_check.png')
    comprime_image('data/tmp/to_check.png')
    
def check_img_format(image):
    file, ext = os.path.splitext(image)##Divide the path image, into filename "dog" and extension ".jpg"
    if ext!=".jpg":
        print("The file has a wrong format, try using .jpg file"
        return false
    return true
