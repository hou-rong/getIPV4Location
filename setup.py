"""
ipv4ToLocation.py
--------
##develop environment

    python3.4.3

##Install

    pip3 install ipv4ToLocation

##Usage
Code:

```python
import ipv4ToLocation
print(ipv4ToLocation.findIP("192.168.199.1"))
print(ipv4ToLocation.findIP("114.114.114.114"))
```

Output:

    {'area': '对方和您在同一内部网', 'country': '局域网'}
    {'area': '信风网络科技有限公司公众DNS服务器', 'country': '江苏省南京市'}

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
    data_files=[('ipv4ToLocation', ['README.md', 'ipv4wry.db'])],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)