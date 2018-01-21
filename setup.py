
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ssl_announcer',
    version='0.1.0',
    description='An announcer application for RoboCup SSL game.',
    long_description=readme,
    author='Shota Aoki',
    author_email='',
    install_requires=['numpy', 'protobuf', 'pygame'],
    url='',
    license=license,
    packages=find_packages(exclude=('tests')),
    test_suite='tests'
) 
