# coding=utf-8
"""
ipv4ToLocation.py
--------
You can use this model to find ipAddress' Location
Support better for chinese ipAddress

Source:

```python
import ipv4ToLocation
print(ipv4ToLocation.findIP("192.168.199.1"))
print(ipv4ToLocation.findIP("114.114.114.114"))
```

Output:

    {'area': '对方和您在同一内部网', 'country': '局域网'}
    {'area': '信风网络科技有限公司公众DNS服务器', 'country': '江苏省南京市'}

"""
from setuptools import find_packages, setup
from ipv4ToLocation import __Version__

setup(
    name='ipv4ToLocation.py',
    version=__Version__,
    license='mit',
    author='HouRong',
    author_email='nmghr9@gmail.com',
    url='https://github.com/nmghr9/getIPV4Location',
    description='ipv4ToLocation',
    long_description=__doc__,
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
    packages=find_packages(),
    include_package_data=True,
    package_data={'ipv4ToLocation': ["ipv4ToLocation/ipv4wry.dat", ]},
)