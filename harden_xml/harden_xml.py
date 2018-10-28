# -*- coding: utf-8 -*-

"""
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

"""

import force_unicode

# Monkey patch codecs.open to default to our errors='replacer' when errors
# isn't specified.
import codecs
from html import entities as html_entities

def replacer(exc):
    logging.warn("Error: {}".format(exc), exc_info=exc)
    l = []
    for c in exc.object[exc.start:exc.end]:
        if isinstance(exc, UnicodeEncodeError):
            c = ord(c)
        elif isinstance(exc, UnicodeDecodeError):
            pass
        else:
            raise TypeError("don't know how to handle %r" % exc)
        try:
            l.append("&%s;" % html_entities.codepoint2name[c])
        except KeyError:
            l.append("&#%d;" % c)
    return ("".join(l), exc.end)

codecs.register_error("replacer", replacer)

_codecs_open = codecs.open
def codecs_open_replace_errors(*args, **kw):
    if "errors" not in kw and len(args) < 4:
        kw['errors'] = 'replacer'
    return _codecs_open(*args, **kw)
codecs.open = codecs_open_replace_errors

# MonkeyPatch minidom.parse to deal with broken XML "Doxygen for Verilog"
# occasionally produced.
import logging
from lxml import etree as ET
from xml.dom import minidom
from xml.parsers import expat
_minidom_parse = minidom.parse

def minidom_parse_with_fixup(inFilename, *args, **kw):
    try:
        return _minidom_parse(inFilename, *args, **kw)
    except expat.ExpatError as e:
        logging.warn("Fixing up XML in {}".format(inFilename), exc_info=e)
        fixxml = ET.parse(codecs.open(inFilename, 'r', "utf-8"), ET.XMLParser(recover=True))
        fixstr = ET.tostring(fixxml, method="xml", encoding='utf-8', xml_declaration=True)
        return minidom.parseString(fixstr, *args, **kw)
minidom.parse = minidom_parse_with_fixup
