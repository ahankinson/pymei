from lxml import etree #AH

import os

from pymei.Components.MeiExceptions import MeiSchemaNotValidError, MeiSchemaNotFoundError #AH
#from exceptions import MeiSchemaNotValidError, MeiSchemaNotFoundError #GVM

# Library stuff.
import logging
lg = logging.getLogger('pymei')
f = logging.Formatter("%(levelname)s %(asctime)s On Line: %(lineno)d %(message)s")
h = logging.StreamHandler()
h.setFormatter(f)

lg.setLevel(logging.DEBUG)
lg.addHandler(h)

__version__ = u"0.1a"
__authors__ = u"Andrew Hankinson"
__copyright__ = u""

#lg.debug('Initializing PyMEI Library.')

# Namespaces
MEI_NS = u"http://www.music-encoding.org/ns/mei"
XLINK_NS = u"http://www.w3.org/1999/xlink"
DATATYPE_NS = u"http://www.w3.org/2001/XMLSchema-datatypes"
XHTML_NS = u"http://www.w3.org/1999/xhtml"
TEI_NS = u"http://www.tei-c.org/ns/1.0"
XML_NS = u"http://www.w3.org/XML/1998/namespace"

# NS Prefixes
MEI_PREFIX = u"mei"
TEI_PREFIX = u"tei"
XLINK_PREFIX = u"xlink"
XHTML_PREFIX = u"xhtml"
XML_PREFIX =u"xml"

# A small lookup table so we can resolve Namespaces to Prefixes
NS_TO_PREFIX = {XML_NS: XML_PREFIX, 
                    TEI_NS: TEI_PREFIX, 
                    XHTML_NS: XHTML_PREFIX,
                    #DATATYPE_NS: DATATYPE_PREFIX, 
                    XLINK_NS: XLINK_PREFIX, 
                    MEI_NS: MEI_PREFIX
                }

PREFIX_TO_NS = dict([v,k] for k,v in NS_TO_PREFIX.iteritems())

for k,v in PREFIX_TO_NS.iteritems():
    etree.register_namespace(k, v)

ENCODING = "UTF-8"

# SCHEMAS
SCHEMA_TYPE = "relaxng" # This may change. For now we'll specify RNG, but we could change it to another schema languages
#SCHEMA_PATH = "/Users/ahankins/Documents/code/mei/branches/mei19.1/ModularizationTesting" #AH
SCHEMA_PATH = "/Users/gabriel/Documents/code/mei/mei/branches/mei19.1/ModularizationTesting" #GVM
AVAILABLE_SCHEMAS = ["mei-all.rng",]

def load_schema(schema="mei-all.rng"):
    """ Takes one of the available schemas and loads them. """
    if schema not in AVAILABLE_SCHEMAS:
        raise MeiSchemaNotValidError("The schema you have specified is not valid.")
    if not os.path.exists(os.path.join(SCHEMA_PATH, schema)):
        raise MeiSchemaNotFoundError("The schema you have specified was not found.")
        
    s = open(os.path.join(SCHEMA_PATH, schema), 'r')
    return etree.parse(s)
    