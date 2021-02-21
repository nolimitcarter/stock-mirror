#!/usr/bin/python

import os
import sys
from setuptools import setup, find_packages

# Must be ran as root or as sudo
if os.getuid() != 0:
    print('ERROR: Need to run as root')
    sys.exit(1)

# Install the requirements if the system does not have it installed
print('INFO: Checking and installing requirements')
os.system('! dpkg -S python-imaging-tk && apt-get -y install python-imaging-tk')

# Generate the requirements from the file for old instructions
print('INFO: Generating the requirements from requirements.txt')
packages = []
for line in open('requirements.txt', 'r'):
    if not line.startswith('#'):
        packages.append(line.strip())

# Run setuptools for pip
setup(
    name='stock-mirror',
    version='1.0',
    description='Raspberry powered mirror',
    author='nolimitcarter',
    url='https://github.com/nolimitcarter/stock-mirror',
    install_requires=packages,
    packages=find_packages(),
)
