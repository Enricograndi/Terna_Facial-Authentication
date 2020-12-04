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
