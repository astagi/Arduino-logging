#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name="arduino_logging",
      py_modules=['arduino_logging'],
      version="0.1",
      description="Arduino serial receiver",
      license="MIT",
      author="Andrea Stagi",
      author_email="stagi.andrea@gmail.com",
      url="https://github.com/astagi/Arduino-logging",
      keywords= "arduino logging serial log",
      install_requires=[
        "pyserial",
      ],
      entry_points = {
        'console_scripts': [
            'arduino_logging = arduino_logging.arduino_logging:main',
        ],
      },
      zip_safe = True)