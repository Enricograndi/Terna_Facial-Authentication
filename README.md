# Terna_Facial Authentication

In this repository you can find a file named ```main.py``` that try to simulate a double authetication with a password and a face match thanks to the Cloudmersive API.

[Cloudmersive](https://cloudmersive.com//) is an on-line service that provides some API that allow to use some visual resource via cloud. The APIs are documented in a [API documentation page](https://api.cloudmersive.com/), they also provide an [Online console](https://api.cloudmersive.com/swagger/index.html?urls.primaryName=Image%20Recognition%20and%20Processing%20API).

An example? Try to execute the main file with: ```python main.py AUTH -u totti -p totti -i faceauth_package/data/test/totti.jpg ```  

> **Note:** the project requires the following modules to run: *argparse, sqlite3, pandas, random, hashlib, os, csv, cloudmersive_image_api_client, Image, paramiko, cryptography, PIL, base64, unittest* and *sys*.

A user can choose the action to perform: it is possibile to:
AUTH, ADD or REMOVE. Once the user has insert the his data. Username is store in the database, the password is used to generate a key that is used to encrypt and decrypt the binary of the image, and then the encrypted binary is saved in the database. At the end, the password is hashed with a Nonce and saved. When the user try to log-in, the hash and the key of the password is generated, checked if is the same and then the image is decrypted and matched.  More information below.



 

## Documentation 
Documentation can be found in: ```docs/html/index.html``` and provides infos about the functions you can find in the various modules.
 
To read them with your **default browser**, from the main folder use ```$ open docs/html/index.html``` or, for other browsers you may have installed, follow these examples:
- **Chrome:** ```$ open -a "Google Chrome" docs/html/index.html```
- **Safari:** ```$ open -a "Safari" docs/html/index.html```


**DOCUMENTATION MADE WITH: [Sphinx](http://www.sphinx-doc.org/en/master/).**



## Command line parameters
As we have mentioned in the first section, some command line parameters are required in order to run the main script.
#### Positional arguments
- **An action is required**: In order to inform the package if to (AUTH)authenticate, (ADD) or to (REMOVE) an user.**Only one** action at time can be passed.
. 
#### Optional arguments
- **-h, --help:** show this help message and exit.  
- **-u U [required]:** the username (requires *-p*).  
- **-p P [required]:** the user's password.   
- **-i P [required]:** the image's path. 

## Authenticate a user

This is the example above mentioned.
```
python main.py AUTH -u totti -p totti -i faceauth_package/data/test/totti.jpg

Hi! totti you are logged in
{'error_details': None,
 'face_count': 1,
 'faces': [{'bottom_y': 158,
            'high_confidence_match': True,
            'left_x': 250,
            'match_score': 1.0,
            'right_x': 353,
            'top_y': 54}],
 'successful': True}
```
 

## How to populate the database
In order to run ```main.py``` you will need a **username**, a **password** and an image. The package comes with a **default user** with the following credenentials:
- *username*: **totti**
- *password*: **totti**
- *image*: **data/test/totti.jpg**

You may want to remove or add new users. You can find a helper module ```dbmanager.py``` in the parent directory that allows you to populate the database.

#### Adding a new user
Use the action ```ADD```. Requires the following:
 - **-u:** username 
 - **-p:** password
 - **-i:** image path


 ```
python main.py ADD -u totti -p totti -i facialauthentication_package\data\test\totti.jpg

Added User: totti
```
#### Removing a user
Use the action ```REMOVE```. Requires the following:

```
python main.py REMOVE -u totti -p totti -i facialauthentication_package\data\test\totti.jpg

User removed
```
#### Authenticate a user
```
python main.py AUTH -u totti -p totti -i facialauthentication_package\data\test\totti.jpg

Hi! totti you are logged in
{'error_details': None,
 'face_count': 1,
 'faces': [{'bottom_y': 158,
            'high_confidence_match': True,
            'left_x': 250,
            'match_score': 1.0,
            'right_x': 353,
            'top_y': 54}],
 'successful': True}
```

## Testing
Tests on parts of the code are provided here: ```

/test/``` .  
You can find a modul: ```test_check_password.py```.
To run them **from the main folder** use:```python -m unittest -v -b /test/test_check_password.py``:

```
python -m unittest -v -b faceauth_package/test/test_check_password.py
test_correct_user (faceauth_package.test.test_check_password.TestInput) ... ok
test_face_authentication_wrong_data (faceauth_package.test.test_check_password.TestInput) ... ok
test_wrong_password (faceauth_package.test.test_check_password.TestInput) ... ok
test_wrong_user (ffaceauth_package.test.test_check_password.TestInput) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.007s

OK
```

## Support
You need help? Get in touch with the authors on [Linkedin](https://www.linkedin.com/)!

## Authors and acknowledgment
Thank you all for the collaboration! Follow the authors on linkedin!
- [**Nicolò Nogara**](https://www.linkedin.com/in/nicolò-nogara-bb132413b)
- [**Enrico Grandi**](https://www.linkedin.com/in/enrico-grandi/)
- [**Ariton Duka**](https://www.linkedin.com/in/ariton-duka-571069173/)
- [**Tommaso Spessato**](https://www.linkedin.com/in/tommaso-spessato-849535176/)
- [**Roberto Franchini**](https://www.linkedin.com/in/roberto-franchini-1200891b1/)


## License
[GPL](https://www.gnu.org/licenses/gpl-3.0.html)
