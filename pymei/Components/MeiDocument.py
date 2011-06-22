# ================================================================
#   MeiDocument.py
#
#   An abstract class representing a complete MEI Document.
#   Contains a child MeiElement that has all other MeiElement
#   objects as children.
#
#   Author:     Andrew Hankinson
#   License:    MIT
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
            
            @TODO:
            Passing in args will narrow down the search by only retrieving
            objects with that attribute.
            
            Passing in kwargs will narrow down the search by only retrieving
            objects where k = v.
        """
        # there should only be one toplevel element
        if not self.__flattened_elements:
            self.__flattened_elements = flatten(self.gettoplevel())
            
        return [o for o in self.__flattened_elements if o.name == searchterm]
    
    def get_by_id(self, id):
        """ Gets a document object by ID. """
        if not self.__flattened_elements:
            self.__flattened_elements = flatten(self.gettoplevel())
        # return (o for o in self.__flattened_elements if o.id == id)
        return self.get_by_id_ref("xml:id", id)
    
    def get_by_facs(self, facsid):
        """ Returns the zone element for a given element's facs attribute"""
        return self.get_by_id_ref("xml:id", facsid, "zone")
        
    def get_by_id_ref(self, attrref, attrvalue, tagfilter=None):
        """ Generic function by pointer references within the document to get all
            other tags that contain this ID. For example, given:
            
                ...
                <system sbref="123" />
                ...
                <sb xml:id="123" />
                ...
            
            The call:
            
            get_by_id_ref("sbref", "123")
            
            will return a pointer to the <system /> element in the tree.
            
            If tagfilter is not None, it will only return the attribute values on
            a specific tag, e.g., 
            
            get_by_id_ref("sbref", "123", "system").
            
            This is useful if you have multiple possible places where an attribute is being
            used in the document.
            
            Returns a list of MeiElements that match.
        """
        if not self.__flattened_elements:
            self.__flattened_elements = flatten(self.gettoplevel())
            
        if tagfilter:
            filt_elements = self.search(tagfilter)
            return [f for f in filt_elements if f.has_attribute(attrref) and f.attribute_by_name(attrref).value == attrvalue]
        else:
            return [f for f in self.__flattened_elements if f.has_attribute(attrref) and f.attribute_by_name(attrref).value == attrvalue]
    
    def flat(self):
        """ Returns a flattened list of the elements in this document. Useful
            for searching and doing document-wide operations on many related
            elements in different places in the document.
        """
        if not self.__flattened_elements:
            self.__flattened_elements = flatten(self.gettoplevel())
        return self.__flattened_elements
    
    def get_system(self, element):
        """ Returns the 'n' attribute of the system break immediately preceding the given MEI Element. 
            If the element is not found, None will be returned. If the element occurs before the first system break,
            -1 will be returned.
        """
        current_system = -1
        if not self.__flattened_elements:
            self.__flattened_elements = flatten(self.gettoplevel())
        for e in self.__flattened_elements:
            if e.name == 'sb':
                current_system = int(e.attribute_by_name('n').value)
                current_system = e.attribute_by_name('n').value
            if e.id == element.id:
                return current_system      
        return None
            