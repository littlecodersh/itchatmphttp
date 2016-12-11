""" A coroutine requests for wechat massive platfrom api project itchatmp
See:
https://github.com/littlecodersh/itchatmphttp
"""

from setuptools import setup, find_packages
from codecs import open
from os import path
import itchatmphttp

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='itchatmphttp',

    version=itchatmphttp.__version__,

    description='A coroutine requests for wechat massive platfrom api project itchatmp',
    long_description=long_description,

    url='https://github.com/littlecodersh/itchatmphttp',

    author='LittleCoder',
    author_email='i7meavnktqegm1b@qq.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],

    keywords='wechat itchatmp api weixin massive platfrom requests',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),

    install_requires=['tornado', 'requests'], # lxml

    # List additional groups of dependencies here
    extras_require={},
)
