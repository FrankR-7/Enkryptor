from setuptools import setup
from os import path

# For legal purposes I didn't steal this from anywhere else
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'Enkryptor',         # How you named your package folder (MyLib)
  packages = ['enkryptor'],   # Chose the same as "name"
  version = '0.1.1-post1',
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A Python module designed to be able to encrypt almost any kind of data as easily as possible for you.',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'furankii',
  author_email = 'frank_rv@yahoo.com',
  url = 'https://github.com/FrankR-7/Enkryptor',
  download_url = 'https://github.com/FrankR-7/Enkryptor/archive/refs/tags/v0.1.1-post1.tar.gz',
  keywords = ['encryption', 'security', 'auth', 'authenthication'],   # Keywords that define your package best
  install_requires=[
          'cryptography',
          'pathlib',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)