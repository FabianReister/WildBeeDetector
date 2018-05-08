# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='wild_bee_watch',
    version='0.1.0',
    description='',
    long_description=readme,
    author='Fabian Reister',
    author_email='fabian.reister92@gmail.com',
    url='https://github.com/FabianReister/WildBeeWatch',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)


