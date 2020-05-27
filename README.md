# Enkryptor
A Python module designed to be able to encrypt almost any kind of data as easily as possible for you.

It uses the cryptography module to provide you SHA256 encryption on your files with little to no intervention from you.

## HOW TO USE:

### Import the class from the module

> `from enkryptor import Enkryptor`

### Create an Enkryptor object

> `enc = Enkryptor()`

Doing this will create all of the files that Enkryptor needs to work in the same directory it's in. If they already exist, they will be reused.
Enkryptor can be safely initialised without any parameters, but you can specify the name of the file
you want to work with or even the path to the file, in this order: 

> `enc = Enkryptor(filename, directory)`

If you specify the path to the file, it's not necessary to specify the filename.

### Pass in the password

> `enc.password("yourpass")`

Replace `yourpass` with a password, as a strng. This function returns true or false depending if the password was correct or incorrect. (This feature is experimental)

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
- Upload to PyPi so anyone can use!
