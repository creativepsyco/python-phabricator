#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='python-phabricator',
    version='0.1',
    author='Mohit Kanwal',
    author_email='mohit.kanwal@gmail.com',
    url='http://github.com/creativepsyco/python-phabricator',
    description='Python Based Phabricator API Bindings',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['python-requests'],
    license='GPL v2',
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)