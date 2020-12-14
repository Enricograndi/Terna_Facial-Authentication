import dbmanager as db
from facialauthentication_package.scripts import facematch
from facialauthentication_package.scripts import first_time_checker
from facialauthentication_package.scripts import image_manager
from facialauthentication_package.scripts import action_reader
import argparse

package_path = 'facialauthentication_package/'
db_path = package_path + '/data/database.db'


def parse_arguments(list_action):
    """Take the argument from the terminal
    
    :param path: None
    :type path: None
    :return: arguments
    :rtype: String
    """

    parser = argparse.ArgumentParser(description="Faccial authenticator"
                                     " Choose an action: -(u) authenticate, "
                                     "-(r) remove user, -(a): add user. "
                                     "All action require:"
                                     "-*(username) -p(password) -i(path of your image)",
                                     prog="faccial_authentication",
                                     usage="%(prog)s [options]",
                                     epilog="Using cloudmersive API")
    parser.add_argument("action", choices= list_action,
                        help="Choose an action")
    parser.add_argument('-u',
                        required=True, help="Username")
    parser.add_argument('-p',
                        help="Password for the user", required=True)
    parser.add_argument('-i',
                        required=True, help="Image path for face match (-i)")
    parser.add_argument('-v',
                        help="False to not show image match results",
                        action="store_true",required=False)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    #take the argument from terminal with argparse
    args = parse_arguments()
    image_manager.save_img_tmp(args.image)




