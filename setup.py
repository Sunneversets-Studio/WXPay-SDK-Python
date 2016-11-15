#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

import pywxpay

setup(
    name='pywxpay',
    version='0.1',
    description='python wxpay sdk.',
    long_description=open('README.rst').read(),
    author='wxpay',
    url='https://github.com/wxpay/WXPay-SDK-Python',
    author_email='wxpay1888@foxmail.com',
    license='BSD',
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    install_requires=[
        'xmltodict',
        'requests'
    ],

    py_modules=['pywxpay', ],

)