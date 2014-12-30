try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Udacity Data Wrangling with MongoDB Project',
    'author': 'Paul Reiners',
    'url': 'URL to get it at.',
    'download_url': 'https://github.com/paul-reiners/udacity-data-wrangling-mongo-db',
    'author_email': 'paul.reiners@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['maps'],
    'scripts': [],
    'name': 'udacity-data-wrangling-mongo-db'
}

setup(**config)
