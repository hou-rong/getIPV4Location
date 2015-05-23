"""
ipv4ToLocation.py
--------

"""
from setuptools import setup, find_packages
from ipv4ToLocation import __Version__

setup(
    name='ipv4ToLocation.py',
    version=__Version__,
    license='mit',
    author='HouRong',
    author_email='nmghr9@gmail.com',
    description='ipv4ToLocation',
    long_description=__doc__,
    data_files=[('ipv4ToLocation', ['README.rst', 'ipv4wry.db'])],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)