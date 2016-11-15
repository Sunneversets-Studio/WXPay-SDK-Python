#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

import pywxpay

setup(
    name='pywxpay',
    version='0.1',
    description='python wxpay sdk.',
    long_description=open('README.rst').read(),
    author='',
    url='https://github.com/wxpay/WXPay-SDK-Python',
    author_email='',
    license='BSD',
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    install_requires=[
        'lazyxml',
        'requests'
    ],

    py_modules=['pywxpay', ],

)