try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Localizer. Beginnings of driverless car',
    'author': 'Dan Hoerst',
    'url': 'www.github.com/Danny830x',
    'download_url': 'www.github.com/Danny830x',
    'author_email': 'Dhoerst1@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['localization'],
    'scripts': [],
    'name': 'localization'
}

setup(**config)
