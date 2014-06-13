import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="Paraboley",
    version="0.1",
    author="Aurélien DESBRIÈRES",
    author_email="aurelien@hackers.camp",
    description="A simple python scrip to display an Parabola GNU / Linux-libre logo in ASCII art along with basic system information.",
    license="GPL",
    url="http://XL04D.github.com/paraboley",
    long_description=read("README.md"),
    scripts=["paraboley"]
)
