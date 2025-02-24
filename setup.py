from setuptools import setup, find_packages

'''
This file is used to create a package for the connect_four game.
'''

setup(
    name="connect_four",
    version="0.2",
    packages=find_packages(),
    description="A classic Connect Four game with CLI and GUI.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Ioannis Koutalios",
    author_email="jkoutalios@gmail.com",
    url="https://github.com/johnkou97/ConnectFour",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
    ],
    entry_points={
        "console_scripts": [
            "connect-four=connect_four.main:launch_cli",
            "connect-four-gui=connect_four.main:launch_gui",
        ],
    },
)
