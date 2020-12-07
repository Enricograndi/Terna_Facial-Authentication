import os
from PIL import Image

package_path = 'FacialAuthentication_package/'

def image_weight(image):
    input_image = 'check.jpg'
    dimension_kb = os.stat(image).st_size
    dimension_mb = dimension_kb/(1024*1024)
    return dimension_mb

def check_img_format(image):
    file, ext = os.path.splitext(image)##Divide the path image, into filename "dog" and extension ".jpg"
    if ext!=".jpg":
        return True
    return False

def pngTojpg(image):
    to_convert = check_img_format(image)
    if to_convert == True:
        im = Image.open(image)
        rgb_im = im.convert('RGB')
        rgb_im.save(package_path + 'data/tmp/image.jpg')
        return (package_path + "data/tmp/image.jpg")
    return image

def comprime_image(input_image):
    size = image_weight(input_image)
    while size > 3.4:
        picture = Image.open(input_image)
        picture.save(input_image,optimize=True,quality=30)
        size = image_weight(input_image)        
    return input_image

def save_img_tmp(image):
    img = pngTojpg(image)
    img = Image.open(img)
    img.save(package_path + 'data/tmp/image.jpg')
    comprime_image(package_path + 'data/tmp/image.jpg')
    
def jpgTobinary(jpg):
    #Convert digital data to binary format
    with open(jpg, 'rb') as file:
        binary = file.read()
    return binary

def binaryToimg(data):
    # Convert binary data to proper format and write it on Hard Disk
    with open("FacialAuthentication_package/data/tmp/target.jpg", 'wb') as file:
        file.write(data)
    #print("Stored temporary target image into: ", "tmp/target.jpg", "\n")
    return "FacialAuthentication_package/data/tmp/target.jpg"
