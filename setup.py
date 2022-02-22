"""
Setup and installation for the package.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="darksky",
    version="0.4",
    url="http://github.com/zachwill/darksky",
    author="Zach Williams",
    author_email="hey@zachwill.com",
    keywords=['darksky', 'dark sky', 'rain', 'forecast', 'weather'],
    description="A simple, Python wrapper for the Dark Sky API.",
    packages=[
        'darksky'
    ],
    install_requires=[
        'mapq',
        'requests',
        'simplejson',
    ],
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
    ],
)
