"""
# Enkryptor

A Python module designed to create files with encrypted data parsed in JSON.

This module takes care about all of the encrypting and JSON parsing
without much supervision from you.

Made by Franklin Rosales
This source code is available for everyone to use and/or modify.
"""

import json
from pathlib import Path
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import os
import base64


class Enkryptor:
    """
    Initialize an Enkryptor class. This class will handle the encrypting, decrypting, and storing of your data.
    NOTE: YOU MUST CALL PASSWORD() AT LEAST ONCE BEFORE CALLING ENKRYPTOR() OR DEKRYPTOR()

    > Arguments:
        filename(string): (default: "enc.e")
        A string containing the name of the file in which you want to store your data.
        directory(string): (default: "")
        A string with the path of your .e file if it's not in the current working directory.
        If you give this variable a value, it's not necessary to pass [filename].
    """

    def __init__(self, filename="enc.e", directory=""):
        self.__file = filename
        self.__cwd = Path.cwd()
        self.__path = Path.joinpath(self.__cwd, self.__file)
        self.__dir = Path(directory)
        self._salter()
        if directory:
            self.__path = self.__dir
        if not self.__path.is_file():
            print(
                f"[ENKRYPTOR] {self.__path} doesn't exist in this directory. A new file will be created.")
            self.__path.touch()
        print(f"[ENKRYPTOR] Enkryptor has been successfully initialised.\nWorking file: {self.__path}")

    def _salter(self):
        self.__spath = Path.joinpath(self.__cwd, 'salt.salt')
        if not self.__spath.exists():
            print("Salt file doesn't exist. A new one will be created")
            self.__salt = os.urandom(16)
            with open(self.__spath, 'xb') as stream:
                stream.write(self.__salt)
        else:
            with open(self.__spath, 'rb') as stream:
                self.__salt = stream.read()

    def enkrypt(self, data={}):
        """
        Takes any data (supported by JSON), turns it into JSON, encrypts it, and then saves it into the file specified.

        Arguments:
        data(any type): (default: {})
            All of the data you want to be included in your file, preferably as a dictionary
        """

        self.__strdata = str(json.dumps(data)).encode()
        self.__encdata = self.__f.encrypt(self.__strdata)
        with open(self.__path, 'wb') as stream:
            stream.write(self.__encdata)
            ret = 1

        return ret

    def dekrypt(self):
        """
        Opens your encrypted file, reads it, de-encrypts it, converts the JSON data
        into its corresponding data type and returns it.
        """
        with open(self.__path, 'rb') as stream:
            self.__d = stream.read()
        self.__d = json.loads(self.__f.decrypt(self.__d))
        return self.__d

    def password(self, password):
        """
        Enter the password you will use to gain access to the encrypted file.
        NOTE: ALWAYS ASK THE USER TO ENTER THE PASSWORD AGAIN IF IT WAS INCORRECT,
        ELSE YOU MIGHT GET UNHANDLED EXCEPTIONS WHEN USING ENKRYPT() AND DEKRYPT()

        Arguments:
        password(string):
            The password that you will use to decrypt your file.

        Returns:
        True if the password you entered was correct
        False if the password was incorrect
        """
        try:
            self.__oldkey = self.__key
        except:
            pass
        __passw = password.encode()
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.__salt,
            iterations=100000,
            backend=default_backend()
        )
        self.__key = base64.urlsafe_b64encode(kdf.derive(__passw))
        self.__f = Fernet(self.__key)
        try:
            self.dekrypt()
        except:
            if self.__oldkey:
                self.__key = self.__oldkey
            return False
        else:
            return True
