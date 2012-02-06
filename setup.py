import os.path
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "uic920",
    version = "0.1.0",
    author = "Neil Albrock",
    author_email = "neil@atomised.coop",
    description = ("Self contained UIC 920-14 country definitions"),
    license = "MIT",
    keywords = "uic 920 country codes",
    url = "https://github.com/neilalbrock/python-uic920",
    packages=['uic920'],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python"])