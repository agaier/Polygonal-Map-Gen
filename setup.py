import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="polymap",
    description="Procedural Generation of Polygon Abstract Map",
    author="Adam Gaier",
    packages=find_packages(exclude=['images', 'notebooks', 'maps', ]),

    install_requires=[
        'fire',
        'numpy',
        'scipy',
        'shapely',
        'matplotlib',
        'plotly'
    ],

)
