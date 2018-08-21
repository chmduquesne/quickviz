import subprocess
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

LONG_DESCRIPTION = """
This package provides widgets for quickly visualizing pandas dataframes

It is often necessary to plot data in order to understand it. It allows to
quiclky spot glitches: that person who is 180 meters tall, this car which
can speed thousands of kilometers per hour. In this situation, one needs a
way to quickly (rather than beautifully) plot what is there. This package
provides a set of widgets to do this very quickly in a few clicks. It
targets speed and ease of use over completeness of the api.
"""

DESCRIPTION         = 'quickviz: interactive widgets for plotting pandas dataframes.'
NAME                = 'quickviz'
PACKAGES            = ['quickviz']
AUTHOR              = 'Christophe-Marie Duquesne'
AUTHOR_EMAIL        = 'chmd@chmd.fr'
URL                 = 'https://github.com/chmduquesne/quickviz'
DOWNLOAD_URL        = 'https://github.com/chmduquesne/quickviz'
LICENSE             = 'MIT'


with open('requirements.txt') as f:
    INSTALL_REQUIRES = [r for r in f.read().split('\n') if r != '']


def version():
    tag = os.getenv('TRAVIS_TAG')
    if not tag:
        tag = subprocess.check_output(
                'git describe --abbrev=0'.split(' ')
                ).strip()
    return tag.decode('utf-8')


VERSION = version()
# update __version__ in __init__.py
with open('quickviz/__init__.py') as f:
    init_py = f.read()
init_py = init_py.replace(str('GIT_TAG'), str(VERSION))
with open('quickviz/__init__.py', 'w') as f:
    f.write(init_py)


setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      download_url=DOWNLOAD_URL,
      license=LICENSE,
      packages=PACKAGES,
      # package_data=PACKAGE_DATA,
      install_requires=INSTALL_REQUIRES,
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5'],
     )
