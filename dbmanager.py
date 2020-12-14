from facialauthentication_package.scripts import facematch
from facialauthentication_package.scripts import image_manager
from facialauthentication_package.scripts import security_features
import sqlite3
import random
import hashlib

package_path = 'facialauthentication_package'
db_path = package_path + '/data/database.db'

conn = None
cursor = None


def open_or_create_db(db_path):
    """Connect to the database and if not exist call create_users table()

    :return: no value
    :rtype: none
    """
    global conn
    global cursor

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM users")
    # if the table does not exist create one
    except sqlite3.OperationalError:
        create_users_table()


def create_users_table():
    """Create the users' table

    :return: no value
    :rtype: none
    """

    global conn
    global cursor

    # Create table
    cursor.execute('''CREATE TABLE users
                   (username VARCHAR(255) NOT NULL,
                    img_target IMAGE NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    salt SMALLINT NOT NULL,
                    PRIMARY KEY (username))''')


def add_new_user(username, target_img, password):
    """Save a new user in the users table

    :param username: the username
    :type username: string
    :param target_img: the img for the face recognition
    :type password: string
    :param recovery_pass: the password for the recovery
    :type password: string
    :return: no value
    :rtype: none
    """
    global conn
    global cursor
    salt = random.randint(1, 10000)
    password = str(salt) + password
    digest = hashlib.sha256(password.encode('utf-8')).hexdigest()
    binary_img = image_manager.jpgTobinary(target_img)
    encripted_binary_image = security_features.encrypt(binary_img,
                                                       password, salt)
    # if the user already exists, replace its image target and password
    cursor.execute("INSERT OR REPLACE INTO users VALUES (?,?,?,?)",
                   (username, encripted_binary_image, digest, salt))
    conn.commit()


def remove_username(username):
    """Remove a user from the users table

    :param username: the username
    :type username: string
    :return: no value
    :rtype: none
    """
    global conn
    global cursor
    # the username is the primary key
    cursor.execute("DELETE FROM users WHERE username = ?", (username,))
    conn.commit()


def check_user(username):
    """Check the username of the user
    from the database

    :param username: the username
    :type username: string
    :return: False or List
    :rtype: Bool or or List
    """
    global conn
    global cursor

    rows = cursor.execute("SELECT * FROM users WHERE username=?",
                          (username,))
    conn.commit()
    results = rows.fetchall()
    if len(results) == 0:
        return False
    return results


def check_password(username, password):
    """Check the password of the user from the database

    :param username: the username
    :type username: string
    :param password: the username
    :type password: string
    :return: False or True
    :rtype: Bool
    """
    results = check_user(username)
    if results is not False:
        # get the salt and prepend to the password before computing the digest
        salt = str(results[0][3])
        password = salt + password
        # get the binary of the image, convert and check the match
        digest = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if digest == results[0][2]:
            return True
    return False


def db_face_auth(username, check_image, password):
    """Check the credentials of a user
    The user provided his credentials for authentication. If the user exists
    in the db, the SHA256(salt+password) is computed. If the digest of the
    password provided by the user is the same as the digest computed as above,
    the function wiil decript the image on the db and try to match. Otherwise
    print "write password"

    :param username: the username provided by the user for the authentication
    :param check_image: the path provided by the user for the image
    :param password: the password provided by the user for the authentication
    :return: Json with of the match if can be authenticated, False otherwise.
    :rtype: Json or boolean
    """

    global conn
    global cursor

    results = check_user(username)
    if results is not False:  # check if the username is correct
        # get the salt and prepend to the password before computing the digest
        salt = str(results[0][3])
        password = salt + password
    # get the binary of the image, convert and check the match
        digest = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if digest == results[0][2]:
            encrypted_image = bytes(results[0][1])
            binary_image = security_features.decrypt(encrypted_image,
                                                     password, salt)
            target_img = image_manager.binaryToimg(binary_image)
            # return target_image
            auth = facematch.match_image(check_image, target_img)
            # remove temporary image
            image_manager.remove_tmp()
            return True
        else:
            print("Wrong Password")
            return False
    else:
        print("Username does not exist")
        return False

