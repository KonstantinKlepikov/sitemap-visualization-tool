from setuptools import setup, find_packages
import os


def strip_coments(l):
    return l.split('#', 1)[0].strip()


def reqs(*f):
    return list(filter(None, [strip_coments(l) for l in open(
        os.path.join(os.getcwd(), *f)).readlines()
    ]))


setup(
    name='sitemap_vizualisation_tool',
    version='0.1',
    ackages=find_packages(),
    include_package_data=True,
    install_requires=reqs('requirements.txt'),
    entry_points='''
        [console_scripts]
    '''
)
