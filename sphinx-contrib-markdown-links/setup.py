from setuptools import setup, find_packages

setup(
    name = 'sphinx-contrib-markdown-links',
    version = '0.0.1',
    url = 'https://github.com/mithro/sphinx-contrib-mithro/tree/master/sphinx-contrib-markdown-links',
    author = "Tim 'mithro' Ansell",
    author_email = 'me@mith.ro',
    packages = find_packages(),
    install_requires = ['lxml'],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
