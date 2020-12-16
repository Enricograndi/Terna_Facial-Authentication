import os
from PIL import Image

package_path = 'facialauthentication_package/'


def image_weight(image):
    """Take the image and check the weight

    :param path: The path to the image
    :type path: string
    :return: the weight in mb
    :rtype: Float
    """
    dimension_kb = os.stat(image).st_size
    dimension_mb = dimension_kb/(1024*1024)
    return dimension_mb


def check_img_format(image):
    """Check the extension of the image if jpg Return true

    :param path: The path to the image
    :type path: string
    :return: True if jpg
    :rtype: Boolean
    """
    file, ext = os.path.splitext(image)  # divide filename, extension
    if ext != ".jpg":
        return True
    return False


def pngTojpg(image):
    """Transform images to jpg

    :param path: The path to the image
    :type path: string
    :return: path of the jpg on tmp or the jpg
    :rtype: string
    """
    to_convert = check_img_format(image)
    if to_convert is True:
        im = Image.open(image)
        rgb_im = im.convert('RGB')
        rgb_im.save(package_path + 'data/tmp/image.jpg')
        return (package_path + "data/tmp/image.jpg")
    else:
        return image


def comprime_image(image):
    """If the image is more of 3.4 mb, comprime,

    :param path: The path to the image
    :type path: string
    :return: The path to the image
    :rtype: string
    """
    size = image_weight(image)
    while size > 3.4:
        picture = Image.open(image)
        picture.save(image, optimize=True, quality=30)
        size = image_weight(image)
    return image


def check_image(image):
    """Check if the path is a valid image

    :param path: The path to the image
    :type path: string
    :return: True if valid, False otherwise
    :rtype: Boolean
    """
    try:
        Image.open(image)
        return True
    except image.ImageNotFoundException:
        return False


def save_img_tmp(image):
    """Save the jpg to the tmp

    :param path: The path to the image
    :type path: string
    :return: The path to the image in tmp
    :rtype: string
    """
    img = pngTojpg(image)
    img = Image.open(img)
    img.save(package_path + 'data/tmp/image.jpg')
    comprime_image(package_path + 'data/tmp/image.jpg')
    return package_path + 'data/tmp/image.jpg'


def jpgTobinary(filename):
    """Read the binary of the image and return

    :param path: The path to the image
    :type path: string
    :return: the image binary
    :rtype: string
    """
    # convert digital data to binary format
    with open(filename, 'rb') as file:
        binary = file.read()
    return binary


def binaryToimg(data):
    """Read the binary and save to tmp/target.jpg

    :param path: Binary of the image
    :type path: string
    :return: the jpg image
    :rtype: string
    """
    # Convert binary data to proper format and write it on Hard Disk
    with open("FacialAuthentication_package/data/tmp/target.jpg",
              'wb') as file:
        file.write(data)
    return "FacialAuthentication_package/data/tmp/target.jpg"


def remove_tmp():
    """Remove target on the tmp folder

    :param path: None
    :type path: None
    :return: None
    :rtype: None
    """
    if os.path.exists("FacialAuthentication_package/data/tmp/target.jpg"):
        os.remove("FacialAuthentication_package/data/tmp/target.jpg")
    else:
        print("No temporary target image present")
