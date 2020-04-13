from setuptools import setup

setup(
    name='awesome_pkg',
    version='0.0.3',
    description='My sample package from a public github repo',
    url='git@github.com:erik-farmer/awesome_pkg.git',
    author='Erik Farmer',
    license='unlicense',
    packages=['awesome_pkg'],
    zip_safe=False
)