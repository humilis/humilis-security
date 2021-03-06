"""Setuptools entry point."""

import os
import codecs
from setuptools import setup, find_packages

from humilis_security import __version__, __author__

dirname = os.path.dirname(__file__)
description = "Humilis plug-in to deploy security groups in a VPC"

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError, RuntimeError):
    if os.path.isfile("README.md"):
        long_description = codecs.open(os.path.join(dirname, "README.md"),
                                       encoding="utf-8").read()
    else:
        long_description = description

setup(
    name="humilis-security",
    include_package_data=True,
    package_data={
        "": ["*.j2", "*.yaml"]},
    packages=find_packages(include=["humilis_security"]),
    version=__version__,
    author=__author__,
    author_email="german@findhotel.net",
    url="https://github.com/humilis/humilis-security",
    license="MIT",
    description=description,
    long_description=long_description,
    install_requires=[
        "humilis>=0.9.5"],
    classifiers=[
        "Programming Language :: Python :: 3"],
    zip_safe=False,
    entry_points={
        "humilis.layers": [
            "security=humilis_security.plugin:get_layer_path"]}
)
