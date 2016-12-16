# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='kadavul',
    version='0.0.1',
    description='Who is Kadavul?',
    long_description=readme,
    authors=['Swaathi Kakarla', 'Lakshmanram'],
    author_email='swaathi@skcript.com',
    url = 'https://github.com/skcript/kadavul',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=(
    	['opencv-python']
    )
)
