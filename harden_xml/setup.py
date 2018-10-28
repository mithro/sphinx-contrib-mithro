from setuptools import setup, find_packages

setup(
    name = 'harden_xml',
    version = '0.0.1',
    url = 'https://github.com/mithro/sphinx-contrib-mithro/tree/master/harden_xml',
    author = "Tim 'mithro' Ansell",
    author_email = 'me@mith.ro',
    packages = find_packages(),
    install_requires = ['lxml'],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
