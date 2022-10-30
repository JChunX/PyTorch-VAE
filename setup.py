from setuptools import setup
import setuptools
import os

with open('requirements.txt') as f:
    requirements = f.read().splitlines()
    
setup(name='pytorch_vae',
      version='0.0.1',
      packages=setuptools.find_packages(),
      install_requires=requirements)