#!/usr/bin/python
# coding: utf8

import os

from setuptools import setup, find_packages
here = os.path.abspath(os.path.dirname(__file__))

try:  # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements('requirements.txt', session=False)

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
try:
    reqs = [str(ir.req) for ir in install_reqs]
except AttributeError:
    reqs = [str(ir.requirement) for ir in install_reqs]

config = {
    'description': 'Flask Azure Active Directory Auth',
    'author': 'Matthias Wutte',
    'url': '',
    'download_url': 'https://github.com/wuttem',
    'author_email': 'matthias.wutte@gmail.com',
    'version': '0.7',
    'install_requires': reqs,
    'tests_require': reqs,
    'packages': find_packages(),
    'scripts': [],
    'name': 'flask-ad-auth'
}

setup(**config)