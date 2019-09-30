# -*- coding: utf-8 -*-
"""Setup file for easy installation"""
import re

from os.path import join, dirname
from setuptools import setup


VERSION_RE = re.compile('__version__ = \'([\d\.]+)\'')


def read_version():
    with open('es_array_logger/__init__.py') as file:
        version_line = [line for line in file.readlines()
                        if line.startswith('__version__')][0]
        return VERSION_RE.match(version_line).groups()[0]


def long_description():
    return open(join(dirname(__file__), 'README.md')).read()


def load_requirements():
    return open(join(dirname(__file__), 'requirements.txt')).readlines()

setup(
    name='elasticsearch-array-logger',
    version=read_version(),
    author='zhangchao02',
    author_email='253572796@qq.com',
    description='Elasticsearch array logger',
    license='BSD',
    keywords='Elasticsearch,logger,list,array',
    url='https://github.com/python-social-auth/social-app-django',
    packages=['es_array_logger'],
    long_description=long_description(),
    # long_description_content_type='text/markdown',
    install_requires=load_requirements(),
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ],
    zip_safe=False
)
