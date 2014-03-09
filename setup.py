#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.rst') as infile:
    long_description = infile.read()

setup(
    name='phabricator-python',
    version='0.3',
    author='Mohit Kanwal',
    author_email='mohit.kanwal@gmail.com',
    url='http://github.com/creativepsyco/python-phabricator',
    description='Python Based Phabricator API Bindings',
    long_description=long_description,
    packages=find_packages(),
    zip_safe=False,
    install_requires=['requests'],
    license='GPL v2',
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
