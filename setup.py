from setuptools import setup

setup(
    name='tplinkswitch',
    version='1.0',
    description='Control TP-Link smart plug',
    author='Yuhao Zhang',
    author_email='tplinkswitch@yuha0.com',
    packages=['tplinkswitch'],
    entry_points={
        'console_scripts': ['tplinkswitch=tplinkswitch.switch:main']
    }
)
