#!/usr/bin/env python
from distutils.core import setup
from efl.utils.setup import build_extra, uninstall
from elmextensions import __version__


setup(
    name = 'Exterminator',
    version = __version__,
    description = 'A system process killer',
    license="BSD-3-clause",
    author = 'Jeff Hoogland',
    author_email = 'JeffHoogland@Linux.com',
    url="https://github.com/JeffHoogland/Exterminator",
    requires = ['efl (>= 1.19)'],
    provides = ['elmextensions'],
    packages = ['elmextensions'],
    cmdclass = {
        'build': build_extra,
         'uninstall': uninstall,
    },
    command_options={
        'install': {'record': ('setup.py', 'installed_files.txt')}
    },
)
