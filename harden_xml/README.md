# Harden XML

Monkey patch things to make XML reading more tolerant. This is useful when
using [Breathe](https://breathe.readthedocs.io/en/latest/) and
[Exhale](https://exhale.readthedocs.io) with Sphinx because Doxygen can
occasionally produce invalid XML output (and Doxyigen-Verilog frequently does
it).

It does the following things;
 * Creates a new 'replacer' codec error mode which will work with any bytecode
   input, not just ones which are real UTF-8 characters.
 * Makes the 'replacer' codec error mode the default is no other error mode is
   given.
 * Patches minidom.parse so that if an XML file fails to parse, it will rerun
   the XML through lxml with error recovery to create valid XML.

# Install

You can install it either via;
```shell
pip install -e "git+https://github.com/mithro/sphinx-contrib-mithro#egg=harden_xml&subdirectory=harden_xml"
```

Or add the following to your `requirements.txt`
```
-e git+https://github.com/mithro/sphinx-contrib-mithro#egg=harden_xml&subdirectory=harden_xml
```

# Set Up

Just import [`harden_xml`](harden_xml.py) in your `conf.py` file *before*
Exhale or Breathe is imported. Generally right after the system imports is the
best location.

```python
# -*- coding: utf-8 -*-
#
# Random Sphinx documentation build configuration file, created by
# sphinx-quickstart on Mon Feb  5 11:04:37 2018.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import re

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

import harden_xml

...
```

# License

This extension is available under your choice of;

 * [ISC License](COPYING) ([see also](https://creativecommons.org/publicdomain/zero/1.0/legalcode))
 * [CC0 1.0 Universal](COPYING.alt.md) ([see also](https://creativecommons.org/publicdomain/zero/1.0/legalcode))
