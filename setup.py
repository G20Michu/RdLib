from setuptools import setup, find_packages

setup(
    name='RdLib',
    version='0.1',
    description='Simple Library to communicate with Rd03D Radar Via Serial on Raspberrypi',
    author='G20Michu',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib'
    ],
)