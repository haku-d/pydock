"""
Read manga web app
--------------
First project in 2019
"""
from setuptools import setup, find_packages

setup(
    name='read-manga',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask_paginate',
        'Flask-User',
        'Flask-SQLAlchemy',
        'psycopg2',
        'Flask-BabelEx',
        'Flask-CacheEx@https://github.com/ninja-saigon/flask-cache/archive/R-1.2.tar.gz'
    ],
)