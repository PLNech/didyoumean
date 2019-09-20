import pathlib

from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="didyoumean3",
    version="0.3.0",
    description="\"Did You Mean?\" suggestions for your Python3 projects.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/PLNech/didyoumean3",
    author="PLNech",
    author_email="github+didyoumean@plnech.fr",
    license="GPLv3",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=['didyoumean3'],
    include_package_data=True,
    install_requires=['selenium'],
    entry_points={
        "console_scripts": [
            "didyoumean3=didyoumean3.__main__:main",
        ]
    },
)
