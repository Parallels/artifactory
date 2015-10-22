#!/usr/bin/env python

import codecs
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read_file(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    with codecs.open(path, mode='r', encoding='utf-8') as handle:
        return handle.read()


setup(
    name='artifactory',
    version='0.1.13',
    py_modules=['artifactory'],
    license='MIT License',
    description='A Python to Artifactory interface',
    long_description=read_file('README.rst'),
    author='Konstantin Nazarov',
    author_email='knazarov@parallels.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Filesystems',
    ],
    url='http://github.com/parallels/artifactory',
    download_url='http://github.com/parallels/artifactory',
    install_requires=['pathlib', 'requests', 'python-dateutil'],
    zip_safe=False,
    package_data={'': ['README.rst']}
)
