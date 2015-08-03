from setuptools import setup

setup(
    name='pytest-ayt2',
    py_modules=['pytest_ayt2'],
    entry_points={'pytest11': ['ayt2 = pytest_ayt2']},
    platforms='any',
    install_requires=['pytest']
)
