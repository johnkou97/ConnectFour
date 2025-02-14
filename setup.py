from setuptools import setup, find_packages

'''
This file is used to create a package for the connect_four game.
'''

setup(
    name="connect_four",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "connect-four=connect_four.main:main",
        ],
    },
)
