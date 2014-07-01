#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='ccp',
    version='0.4b',
    description="A Python client for the Changelog API",
    long_description=open('README.rst').read() + '\n\n' +
                     open('CHANGES.txt').read(),
    author="Adam Papai",
    author_email="wooh@wooh.hu",
    url="http://github.com/woohgit/changelog-client-python",
    packages=['ccp'],
    package_data={'': ['LICENSE.txt']},
    package_dir={'ccp': 'ccp'},
    include_package_data=True,
    install_requires=["requests >= 1.0.4"],
    license=open('LICENSE.txt').read(),
    zip_safe=False,
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
    ),
)