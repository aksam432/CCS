from setuptools import setup,find_packages

import sys


if sys.version_info[:2] < (3,0):
    raise SystemExit('Python 3 required')
setup(
        name='ccs',
        version="0.1.0",
        url="https://github.com/aksam432/CCS",
        description=" A Python package for fitting two-body potentials using curvature constrained splines",
        author="Akshay Krishna AK",
        author_email="akshay.kandy@kemi.uu.se",
        platforms=['unix'],
        include_package_data=True,
        packages=find_packages(),
        license='GPLv3',
        scripts=['bin/atom-json','bin/ccs_fit'],
        install_requires=[
            "cvxopt==1.2.7",
            "matplotlib==3.0.3",
            "numpy>=1.18.1",
            "pandas==0.24.2",
            "scipy",
            "ase>=3.19.0"
            ],
        keywords = ['Two-body Potentials', 'optimisation', 'Force Field'],
        classifiers=[],
        )
