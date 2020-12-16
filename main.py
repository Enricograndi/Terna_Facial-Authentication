from faceauth_package.scripts import dbmanager as db
from faceauth_package.scripts import facematch
from faceauth_package.scripts import first_time_checker
from faceauth_package.scripts import image_manager
from faceauth_package.scripts import action_reader
import argparse

package_path = 'faceauth_package/'
db_path = package_path + '/data/database.db'


def parse_arguments(list_action):
    """Take the argument from the terminal
    :param path: None
    :type path: None
    :return: arguments
    :rtype: String
    """

    parser = argparse.ArgumentParser(description="Faccial authenticator"
                                     " Choose an action: AUTH, REMOVE, DELETE"
                                     " All action require:"
                                     " Usename -p password -i imagepath",
                                     prog="faccial_authentication",
                                     usage="%(prog)s [options]",
                                     epilog="Using cloudmersive API")
    parser.add_argument("action", choices=list_action,
                        help="Choose an action")
    parser.add_argument('-u',
                        required=True, help="Username")
    parser.add_argument('-p',
                        help="Password for the user", required=True)
    parser.add_argument('-i',
                        required=True, help="Image path for face match (-i)")
    parser.add_argument('-v',
                        help="False to not show image match results",
                        action="store_true", required=False)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    # Take the argument from terminal with argparse
    list_action = action_reader.read_action()
    args = parse_arguments(list_action)
    # While the format of the image is not .jpg repit arg
    if image_manager.check_image(args.i) is True:
        image_manager.save_img_tmp(args.i)
        # If it is the first time, ask to add a user
        if first_time_checker.first_time() is True:
            print("There aren't users in the database")
        # Open the connection with db and (IF NECESSARY)
        db.open_or_create_db(db_path)
        # Severals control based on args
        if args.action == "ADD":
            # Add new user
            db.add_new_user(args.u, args.i, args.p)
            first_time_checker.write_used()
            print("Added User: "+args.u)
        if args.action == "REMOVE":
            # Remove user
            db.remove_username(args.u)
            print("User removed")
        if args.action == "AUTH":
            # Match faces
            auth = db.db_face_auth(args.u, args.i, args.p)
            if auth is False:
                # The password is inccorect
                print("Try again")
            elif auth.successful is True:
                # Match done
                if auth.faces[0].match_score > 0.6:
                    print("Hi! " + args.u + " you are logged in")
                    if args.v is False:
                        # if not specify print the match results
                        # check verbosity
                        print(auth)
                else:
                    print("You are not" + args.u)
            else:
                print("There aren't faces on the image you have provided")
