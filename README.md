# Enkryptor
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/enkryptor)
![PyPI - License](https://img.shields.io/pypi/l/enkryptor)
![PyPI - Downloads](https://img.shields.io/pypi/dd/enkryptor)
![PyPI](https://img.shields.io/pypi/v/enkryptor)

A Python module designed to be able to encrypt almost any kind of data as easily as possible for you.

It uses the cryptography module to provide you SHA256 encryption on your files with little to no intervention from you.

This is a newly made module, if you find any bugs or find a way to make it better feel free to file an issue or a pull request!

## HOW TO USE:
---

### Import the class from the module

> `from enkryptor import Enkryptor`

### Create an Enkryptor object

> `enc = Enkryptor()`

Doing this will create all of the files that Enkryptor needs to work in the same directory it's in. If they already exist, they will be reused.
Enkryptor can be safely initialised without any parameters, but you can specify either the name of the file
you want to work with or its path, like this:

> `enc = Enkryptor(file='filename.e')`

> `enc = Enkryptor(file='X:/path/to/file.e')`

Having the `.e` extension is not necessary, but it separates your encrypted file from the others. You can actually set the extension to whatever you want. If you don't specify the file, the file created will be called `enc.e`.

You might also want to store different salt files for different encrypted files. You can specify the salt file's name or directory with the `salt` parameter:

> `enc = Enkryptor(salt='saltfilename.salt')`

> `enc = Enkryptor(salt='X:/path/to/salt/file.salt')`

Again, the `.salt` extension isn't strictly necessary. If you don't specify the salt file, the file created will be called `salt.salt`.
### Pass in the password

> `enc.password("yourpass")`

Replace `yourpass` with a password, as a string. This function returns true or false depending if the password was correct or incorrect. (This feature is experimental)

### Encrypt your data

> `enc.enkrypt(data)`

Replace `data` with whichever data you might want to save encrypted into your file, preferably in a list, dictionary or tuple.
The data will be encrypted and saved into the file `enc.e` in the same directory the module is called from or into the file in the path you specified when you initialised the object.

### Decrypt your data

> `enc.dekrypt()`

You dont have to pass anything into this function. All it does is open your encrypted file, decrypt its contents, and return them.

## Bucket List

- Add an `Extras` class with full access to the functions of `Enkryptor` and other sweet stuff like a password generator.
- Add an `append` parameter to enkrypt() to simply add something to the data already encrypted instead of overwriting it
- Convert the whole module into Cython to give it better performance
- ~~Upload to PyPi so anyone can use!~~ **DONE**
