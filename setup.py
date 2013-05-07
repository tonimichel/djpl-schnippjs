#! /usr/bin/env python
import os
from setuptools import setup, find_packages

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name='django-productline-schnippjs',
    version='0.1',
    description='a django-productline feature to include schnipp.js',
    long_description=read('README.rst'),
    license='The MIT License',
    keywords='django, FOSD, FOP, feature-oriented-programming, product-line, javascript, schnipp.js',
    author='Toni Michel',
    author_email='toni@schnapptack.de',
    url="https://github.com/toni/django-productline-schnippjs",
    packages=find_packages(),
    package_dir={'schnippjs': 'schnippjs'},
    package_data={'django_productline': []},
    include_package_data=True,
    scripts=[],
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent'
    ],
    install_requires=[
        'django-productline',
    ]
)

