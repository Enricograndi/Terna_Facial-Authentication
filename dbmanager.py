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