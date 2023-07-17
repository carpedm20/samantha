import os

from setuptools import find_packages, setup

setup(
    name="samantha",
    packages=find_packages(),
    version="0.0.1",
    install_requires=[
        req.strip()
        for req in open(os.path.join(os.path.dirname(__file__), "requirements.txt")).readlines()
    ],
)
