#!/usr/bin/env python

from setuptools import setup

with open("README.md", "r") as rm:
    long_description = rm.read()

VERSION = "0.0.2"

setup(name='buildbot-matrix',
        version=VERSION,
        description='buildbot plugin for using matrix for notifications',
        author='HayWo',
        author_email='opensource@nct08.de',
        url='https://github.com/HayWo/buildbot-matrix',
        long_description=long_description,
        long_description_content_type="text/markdown",
        packages=['buildbot_matrix'],
        requires=[
            "buildbot (>=2.0.0)"
        ],
        entry_points={
            "buildbot.reporters": [
                "MatrixStatusPush = buildbot_matrix.reporter:MatrixStatusPush"
            ]
        },
        classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Programming Language :: Python :: 3",
            "Environment :: Plugins",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: MacOS",
            "Operating System :: POSIX :: Linux",
            "Topic :: Software Development :: Build Tools"
        ],
        python_requires='>=3.6',
    )
