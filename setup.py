"""
Canasta CLI Configuration
"""

from setuptools import find_packages, setup

setup(
    name="canasta",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    ## Entry point for command line and function to be executed
    entry_points={
        'console_scripts': ['canasta=main:main'],
    }
)
