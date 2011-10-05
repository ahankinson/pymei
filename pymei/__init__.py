from lxml import etree
import os
from pymei.Components.MeiExceptions import MeiSchemaNotValidError, MeiSchemaNotFoundError
from pymei.Components.MeiNamespace import MeiNamespace

import logging
lg = logging.getLogger('pymei')
f = logging.Formatter("%(levelname)s %(asctime)s On Line: %(lineno)d %(message)s")
h = logging.StreamHandler()
h.setFormatter(f)

lg.setLevel(logging.DEBUG)
lg.addHandler(h)

__version__ = u"1.0"
__authors__ = u"Andrew Hankinson, Alastair Porter, Jessica Thompson, Raffaele Viglianti"
__copyright__ = u""

MEI_VERSION="2011-05"

ENCODING = "UTF-8"

MEI_NS = MeiNamespace("mei", u"http://www.music-encoding.org/ns/mei")
XLINK_NS = MeiNamespace("xlink", u"http://www.w3.org/1999/xlink")
XHTML_NS = MeiNamespace("xhtml", u"http://www.w3.org/1999/xhtml")
TEI_NS = MeiNamespace("tei", u"http://www.tei-c.org/ns/1.0")
XML_NS = MeiNamespace("xml", u"http://www.w3.org/XML/1998/namespace")


# # A small lookup table so we can resolve Namespaces to Prefixes
# NS_TO_PREFIX = {XML_NS: XML_PREFIX, 
#                     TEI_NS: TEI_PREFIX, 
#                     XHTML_NS: XHTML_PREFIX,
#                     #DATATYPE_NS: DATATYPE_PREFIX, 
#                     XLINK_NS: XLINK_PREFIX, 
#                     MEI_NS: MEI_PREFIX
#                 }

# PREFIX_TO_NS = dict([v,k] for k,v in NS_TO_PREFIX.iteritems())

# for k,v in PREFIX_TO_NS.iteritems():
#     etree.register_namespace(k, v)

# SCHEMAS
#SCHEMA_PATH = "/Users/ahankins/Documents/code/mei/branches/mei19.1/ModularizationTesting" #AH
# SCHEMA_PATH = "/Users/gabriel/Documents/code/mei/mei/branches/mei19.1/ModularizationTesting" #GVM
# AVAILABLE_SCHEMAS = ["mei-all.rng",]

# def load_schema(schema="mei-all.rng"):
#     """ Takes one of the available schemas and loads them. """
#     if schema not in AVAILABLE_SCHEMAS:
#         raise MeiSchemaNotValidError("The schema you have specified is not valid.")
#     if not os.path.exists(os.path.join(SCHEMA_PATH, schema)):
#         raise MeiSchemaNotFoundError("The schema you have specified was not found.")
        
#     s = open(os.path.join(SCHEMA_PATH, schema), 'r')
#     return etree.parse(s)
    