# ================================================================
#   MeiDocument.py
#
#   An abstract class representing a complete MEI Document.
#   Contains a child MeiElement that has all other MeiElement
#   objects as children.
#
#   Author:     Andrew Hankinson
#   License:    BSD
#
# ================================================================

import itertools

from pymei import ENCODING, MEI_PREFIX, MEI_NS
from pymei.Helpers import flatten

import logging
lg = logging.getLogger('pymei')

class MeiDocument(object):
    def __init__(self, docname="Untitled", encoding=ENCODING):
        self.__encoding = ENCODING
        self.__default_prefix = MEI_PREFIX
        self.__default_namespace = MEI_NS
        self.__standalone = False
        self.__xml_version = "1.0"
        self.__name = docname
        self.elements = []
        self.__flattened_elements = None
    
    def __repr__(self):
        return u"<MeiDocument {0}>".format(self.__name)
        
    def __str__(self):
        return "<MeiDocument {0}>".format(self.__name)
    
    def __unicode__(self):
        return u"<MeiDocument {0}>".format(self.__name)
    
    def addelement(self, element):
        self.elements.append(element)
    
    def delelement(self, element):
        del element
    
    def getencoding(self):
        return self.__encoding
    
    def setencoding(self, value):
        self.__encoding = value
        
    encoding = property(getencoding, setencoding, doc="Get and set a document's encoding")
    
    def gettoplevel(self):
        return self.elements[0]
    
    def getdefaultnamespace(self):
        return self.__default_namespace
    
    def setdefaultnamespace(self, value):
        self.__default_namespace = value
    
    default_namespace = property(getdefaultnamespace, setdefaultnamespace, doc="Get and set a document's default namespace")
    
    def getdefaultprefix(self):
        return self.__default_prefix
    
    def setdefaultprefix(self, value):
        self.__default_prefix = value
    default_prefix = property(getdefaultprefix, setdefaultprefix, doc = "Get and set a document's default namespace")
    
    def getstandalone(self):
        return self.__standalone
    
    def getxmlversion(self):
        return self.__xml_version
    
    def search(self, searchterm, *args, **kwargs):
        """ 
            Searches an MEI Document for an object name that matches the
            search term.
            
            Note: Returns a generator object, and not the actual list of elements,
            with the assumption that you will either want to loop through all 
            the things found in the search, or you can cast it to a list or tuple.
            
            @TODO:
            Passing in args will narrow down the search by only retrieving
            objects with that attribute.
            
            Passing in kwargs will narrow down the search by only retrieving
            objects where k = v.
        """
        # there should only be one toplevel element
        if not self.__flattened_elements:
            self.__flattened_elements = flatten(self.gettoplevel())
        return (o for o in self.__flattened_elements if o.name == searchterm)
    
    def get_by_id(self, id):
        """ Gets a document object by ID. """
        if not self.__flattened_elements:
            self.__flattened_elements = flatten(self.gettoplevel())
        return (o for o in self.__flattened_elements if o.id == id)
            