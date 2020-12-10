#https://nitratine.net/blog/post/encryption-and-decryption-in-python/
#python -m pip install cryptography
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

def generating_key(password, salt):
    password = password.encode()  # Convert to type bytes
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=str(salt).encode(),  
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once
    return key

def encrypt(message, password, salt):
    key = generating_key(password, salt)
    encryption = Fernet(key).encrypt(message)
    return encryption

def decrypt(message_encrypted, password, salt):
    key = generating_key(password, salt)
    decryption = Fernet(key).decrypt(message_encrypted)
    decryption = decryption  # decode from bytes to string
    return decryption

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import base64


def generating_key(password, salt):
    """In order to perform symmetric encription and decription we need to
    generate key from password that respect the requirment asked,
    
    :param password: the password given
    :param salt: the salt given
    :type password: string
    :type salt: string
    :return: the key
    :rtype: bytes
    """

    password = password.encode()  # Convert to type bytes
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=str(salt).encode(),
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key