# -*- coding: utf-8 -*-
"""
Setup package module
"""
from distutils.core import setup


def read(filename):
  with open(filename, encoding='utf-8') as file:
    return file.read()


setup(
  name='callbaker',
  packages=['callbaker'],
  version='1.2.0',
  license='MIT',
  description="Telegram Button Callback Data Converter",
  long_description=read("README.md"),
  long_description_content_type="text/markdown",
  author='torrua',
  author_email='torrua@gmail.com',
  url='https://github.com/torrua/callbaker',
  download_url='https://github.com/torrua/callbaker/archive/v1.2.0.tar.gz',
  keywords=['Convert', 'Callback', 'Keyboard', 'Telegram', "Inline"],
  classifiers=[
    'Development Status :: 4 - Beta',  # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
  python_requires='>=3.5',
)
