# -*- encoding: utf-8 -*-
"""
@File    :   setup.py
@Time    :   2023/03/10 22:08:26
@Author  :   blakeyzhang
@Version :   1.0
@Desc    :   None
"""

from setuptools import find_packages, setup

setup(
    name="beer",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "webob",
        "parse",
        "jinja2",
        "requests",
        "requests-wsgi-adapter",
        "whitenoise",
    ],
)
