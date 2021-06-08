from distutils.core import setup
setup(
  name = 'Enkryptor',         # How you named your package folder (MyLib)
  packages = ['enkryptor'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A Python module designed to be able to encrypt almost any kind of data as easily as possible for you.',   # Give a short description about your library
  author = 'furankii',                   # Type in your name
  author_email = 'frank_rv@yahoo.com',      # Type in your E-Mail
  url = 'https://github.com/FrankR-7/Enkryptor',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/FrankR-7/Enkryptor/archive/refs/tags/v0.1.tar.gz',    # I explain this later on
  keywords = ['encryption', 'security', 'auth', 'authenthication'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'cryptography',
          'pathlib',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)