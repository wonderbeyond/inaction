#!/usr/bin/python
# coding=utf-8
from setuptools import setup

setup(name='inaction',
      version='1.0',
      description='Run specified commands while specified files changes.',
      author='Wonder Beyond',
      author_email='wonderbeyond@gmail.com',
      url='https://github.com/wonderbeyond/inaction',
      py_modules=['inaction'],
      install_requires=['pyinotify'],
     )
