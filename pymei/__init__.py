from lxml import etree
import os

from pymei.exceptions import MeiSchemaNotValidError, MeiSchemaNotFoundError

# Library stuff.

__version__ = u"0.1a"
__authors__ = u"Andrew Hankinson"
__copyright__ = u""

# Namespaces
MEI_NS = u"http://www.music-encoding.org/ns/mei"
XLINK_NS = u"http://www.w3.org/1999/xlink"
DATATYPE_NS = u"http://www.w3.org/2001/XMLSchema-datatypes"
XHTML_NS = u"http://www.w3.org/1999/xhtml"
TEI_NS = u"http://www.tei-c.org/ns/1.0"

# NS Prefixes
MEI_PREFIX = u"mei"
TEI_PREFIX = u"tei"
XLINK_PREFIX = u"xlink"
XHTML_PREFIX = u"xhtml"

ENCODING = "UTF-8"

# SCHEMAS
SCHEMA_TYPE = "relaxng" # This may change. For now we'll specify XSD, but we could change it to another schema languages
SCHEMA_PATH = "/Users/ahankins/Documents/code/mei/branches/mei19.1/ModularizationTesting"
AVAILABLE_SCHEMAS = ["mei-all.rng",]

def load_schema(schema="mei-all.rng"):
    """ Takes one of the available schemas and loads them. """
    if schema not in AVAILABLE_SCHEMAS:
        raise MeiSchemaNotValidError("The schema you have specified is not valid.")
    if not os.path.exists(os.path.join(SCHEMA_PATH, schema)):
        raise MeiSchemaNotFoundError("The schema you have specified was not found.")
        
    s = open(os.path.join(SCHEMA_PATH, schema), 'r')
    return etree.parse(s)