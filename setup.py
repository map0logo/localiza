#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='localiza',
    version='0.1.0',
    description="Open source library for location models and science written in\
    Python intended to the development of high level applications.",
    long_description=readme + '\n\n' + history,
    author="Francisco Palm",
    author_email='mapologo@tuta.io',
    url='https://github.com/map0logo/localiza',
    packages=[
        'localiza',
    ],
    package_dir={'localiza':
                 'localiza'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD-3-clause",
    zip_safe=False,
    keywords='localiza',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD-3-clause',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
