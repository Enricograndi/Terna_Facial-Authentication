import sqlite3

conn = None
cursor = None

def open_or_create_db(db_path):
    """Connect to the database
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
    """Create the users' table if it does not exist
    :return: no value
    :rtype: none
    """

    global conn
    global cursor
    
    # Create table
    cursor.execute('''CREATE TABLE users
                   (username VARCHAR(255) NOT NULL,
                    img_target Image NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    salt SMALLINT NOT NULL,
                    PRIMARY KEY (username))''')

def add_new_user(username, target_img, password):
   
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
   
    global conn
    global cursor
    # the username is the primary key
    cursor.execute("DELETE FROM users WHERE username = ?", (username,))
    conn.commit()

    def db_face_auth(username, check_image, password):
   

    global conn
    global cursor

    rows = cursor.execute("SELECT * FROM users WHERE username=?",
                          (username,))
    conn.commit()
    results = rows.fetchall()
    if len(results) == 0:
        print("Wrong Username")
        return False
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
        return auth
    else:
        print("Wrong Password")
    return False