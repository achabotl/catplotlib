#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "matplotlib",
    "requests",
]

test_requirements = []

setup(
    author="Alexandre Chabot-Leclerc",
    author_email="accounts.github@alex.alexchabot.net",
    python_requires=">=3.6",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="Matplotlib, but for cats.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="catplotlib",
    name="catplotlib",
    packages=find_packages(include=["catplotlib", "catplotlib.*"]),
    url="https://github.com/achabotl/catplotlib",
    version="1.0.2",
    zip_safe=False,
)
