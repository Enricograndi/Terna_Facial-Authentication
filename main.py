from FacialAuthentication_package.scripts import facematch
from FacialAuthentication_package.scripts import image_manager
import argparse

#try with the same face and same image
#target_img = image_manager.comprime_image("data/test/check_image.jpg")
#check_img = image_manager.comprime_image("data/test/check_image.jpg")
#result = facematch.match_image(target_img,check_img)
#print(result)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', "--image", required=True, help="add an image to allow the face authentication (-i)")
    args = parser.parse_args()
    return args



if __name__ == "__main__":
    #take the argument from terminal with argparse
    args = parse_arguments()
    image_manager.save_img_tmp(args.image)




