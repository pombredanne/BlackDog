"""
Blackdog

Copyright (C) 2014 Snaipe, Therozin

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="blackdog",
    version="1.0.2",
    author="Snaipe, Therozin",
    author_email="franklinmathieu@gmail.com",
    description="A bukkitdev to maven repository mapper",
    license="GPLv3",
    keywords="minecraft bukkitdev plugin maven repository",
    url="http://github.com/Snaipe/BlackDog.git",
    packages=['blackdog'],
    install_requires=['pyquery', 'baker', 'requests'],
    long_description=read('README.md'),
    scripts=['bin/blackdog'],
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.4",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities"
    ]
)
