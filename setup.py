from setuptools import setup, find_packages

setup(
    name='imhotep',
    version='0.1.2',
    packages=find_packages(),
    url='https://github.com/glowdigitalmedia/imhotep',
    license='MIT',
    author='Justin Abrahms, Konrad Korzel',
    author_email='justin@abrah.ms, konrad.korzel@gmail.com',
    description='A fork of Justin Abrahms tool to pipe linters into code review by ',
    install_requires=['requests==2.2.1'],
    extras_require={'pylint': 'PyLint'},
    entry_points={
        'console_scripts': [
            'imhotep = imhotep.main:main',
        ],
    }
)
