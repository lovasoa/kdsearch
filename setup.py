from setuptools import setup

VERSION = '1.1'

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Operating System :: OS Independent',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Scientific/Engineering'
]

setup(
  name = 'kdsearch',
  packages = ['kdsearch'], # this must be the same as the name above
  version = VERSION,
  description = 'Efficient K-dimensional queries in python using KDTrees with pandas and numpy.',
  author = 'Ophir LOJKINE',
  author_email = 'pere.jobs@gmail.com',
  url = 'https://github.com/lovasoa/kdsearch',
  download_url = 'https://github.com/lovasoa/kdsearch/archive/%s.tar.gz' % (VERSION,),
  keywords = ['tree', 'search', 'query', 'bounding box', 'index', 'k-dimensional', 'dimesnions', 'data structure'],
  classifiers = CLASSIFIERS,
)
