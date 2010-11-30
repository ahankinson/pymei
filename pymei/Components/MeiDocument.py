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

from pymei import ENCODING, MEI_PREFIX, MEI_NS

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
    
    def search(self, searchterm, **kwargs):
        """ 
            Searches an MEI Document for an object name that matches the
            search term.
            
            @TODO:
            Passing in KW args will narrow down the search by only retrieving
            objects with given attribute values.
        """
        # there should only be one toplevel element
        if not self.__flattened_elements:
            searchspace = self._flatten()
            
        result = filter(lambda x: x.getname() == searchterm, self.__flattened_elements)
        return result
    
    def _flatten(self):
        """ Flattens the nested elements into a single list.
            Caches the result in the object for future lookups.
        """
        rootl = self.gettoplevel()
        
        def __fl(ls):            
            for ch in ls.getchildren():
                if len(ch.getchildren()) > 0:
                    for cd in __fl(ch):
                        yield cd
                yield ch
        flattened = list(__fl(rootl))
        self.__flattened_elements = flattened
        
        
        
        
        