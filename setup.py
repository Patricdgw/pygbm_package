from setuptools import setup, find_packages

setup(
    name='pygbm',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click',
        'numpy',
        'matplotlib',
    ],
    entry_points={
        'console_scripts': [
            'pygbm=pygbm.cli:cli',
        ],
    },
)