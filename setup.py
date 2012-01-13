from setuptools import setup, find_packages
import os

version = '1.2'

setup(name='collective.dewplayer',
      version=version,
      description="A simple package using Dewplayer for video content - By Makina Corpus",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='Plone Python Dewplayer',
      author='Sylvain BOURELIOU',
      author_email='sylvain.boureliou@makina-corpus.com',
      url='http://svn.plone.org/svn/collective/collective.dewplayer/trunk',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.swfobject',
          'collective.configviews',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
