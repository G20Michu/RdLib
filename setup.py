from setuptools import setup, find_packages

setup(
    name='RdLib',
    version='0.9',
    description='Simple Library to communicate with Rd03D and HLK-LD2450 Radar Via Serial on Raspberrypi',
    author='G20Michu',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib'
    ],
)
url='https://github.com/G20Michu/RdLib.git'