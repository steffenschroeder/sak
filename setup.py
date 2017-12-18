from setuptools import setup

setup(
    name='sak',
    version='0.1',
    py_modules=['sak'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        sak=sak:cli
    ''',
)
