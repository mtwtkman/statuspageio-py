from setuptools import setup


dependencies = [
    'requests',
]

dev_dependencies = [
    'mypy',
    'pycodestyle',
]


setup(
    name='statuspageio-py',
    version='0.0.1',
    author='mtwtkman',
    author_email='yo@mtwtkman.dev',
    packages=['statuspageio'],
    extras_require={
        'dev': dev_dependencies,
    },
    install_requires=dependencies,
    license='WTFPL',
    url='https://github.com/mtwtkman/statuspageio-py',
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ]
)
