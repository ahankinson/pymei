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

from pymei import ENCODING, MEI_PREFIX, MEI_NS, MEI_VERSION
from pymei.Helpers import flatten

#deal with deprecated code.
import warnings
warnings.simplefilter('once')

import logging
lg = logging.getLogger('pymei')

import time

class MeiDocument(object):
    def __init__(self):
        self.__encoding = ENCODING
        self.__version = MEI_VERSION
        self.__namespaces = [MEI_NS]
        self.__standalone = False
        self.__xml_version = "1.0"
        self.__root = None
        self.__flattened_tree = None
        self.__idmap = {}
    
    def __repr__(self):
        return u"<MeiDocument {0}:{1}>".format(self.__version, self.__root.name)
        
    def __str__(self):
        return "<MeiDocument {0}:{1}>".format(self.__version, self.__root.name)
    
    def __unicode__(self):
        return u"<MeiDocument {0}:{1}>".format(self.__version, self.__root.name)
    
    @property
    def namespaces(self):
        return self.__namespaces
    
    def add_namespace(self, namespace):
        pass
    
    def get_namespace(self, href):
        pass
    
    def has_namespace(self, href):
        pass
    
    @property
    def version(self):
        return self.__version
    
    @property
    def root(self):
        return self.__root
    @root.setter
    def root(self, value):
        self.__root = value
    @root.deleter
    def root(self):
        self.__root = None
    
    def get_element_by_id(self, id):
        # ensure we're working with the latest info
        self._update_document()

        if id not in self.__idmap.keys():
            return None
        else:
            return self.__idmap[id]
    
    def get_elements_by_name(self, name):
        self._update_document()
        return [c for c in self.__flattened_tree if c.name == name]
    
    def get_position_in_document(self, element):
        self._update_document()
        if element.id not in self.__idmap.keys():
            return None
        else:
            return self.__flattened_tree.index(element)


    @property
    def flattened_tree(self):
        return self.__flattened_tree

    def lookback(self, from_element, name):
        self._update_document()

        if from_element.id not in self.__idmap.keys():
            return None
        
        idx = self.__flattened_tree.index(from_element)

        # slice the list and reverse it so that we only 
        # search the elements we need.
        search_elements = self.__flattened_tree[:idx].reverse()

        for el in search_elements:
            if el.name == name:
                return el

        return None

    
    def _update_document(self):
        """ 
            Update both the list of all elements
            as well as the {id,element} dictionary.

            Protected since only the document should
            be able to update itself.
        """
        self.__idmap = {} # unset any old element maps
        self.__flattened_tree = flatten(self.__root)

        for el in self.__flattened_tree:
            self.__idmap[el.id] = el



    # @property
    # def root(self):
    #     return self.__root
    # @root.setter
    # def root(self, value):
    #     self.__root = value
    # @root.deleter
    # def root(self):
    #     del self.__root
    
    # def addelement(self, element):
    #     warnings.warn('Addelement is no longer used. Use foo.root = bar instead.', DeprecationWarning)
    #     self.root = element
    
    # def add_element(self, element):
    #     self.root = element
    
    # def delelement(self, element):
    #     warnings.warn('Delelement is no longer used. Use del foo.root instead.', DeprecationWarning)
    #     del self.root
    
    # def del_element(self, element):
    #     del self.root
    
    # def getencoding(self):
    #     warnings.warn('Getencoding() is now a @property decorator. Use foo.encoding now.', DeprecationWarning)
    #     return self.encoding
    
    # def setencoding(self, value):
    #     warnings.warn('SetEncoding() is now an @property decorator. use foo.encoding = bar now', DeprecationWarning)
    #     self.encoding = value
    
    # @property
    # def encoding(self):
    #     return self.__encoding
    # @encoding.setter
    # def encoding(self, value):
    #     self.__encoding = value
    
    # def gettoplevel(self):
    #     warnings.warn('GetTopLevel() has been renamed to root. Use foo.root to get the first element.', DeprecationWarning)    
    #     return self.root
    
    # @property
    # def default_namespace(self):
    #     return self.__default_namespace
    # @default_namespace.setter
    # def default_namespace(self, value):
    #     self.__default_namespace = value
        
    # @property
    # def default_prefix(self):
    #     return self.__default_prefix
    # @default_prefix.setter
    # def default_prefix(self, value):
    #     self.__default_prefix = value
    
    # @property
    # def standalone(self):
    #     return self.__standalone
    
    # @property
    # def xmlversion(self):
    #     return self.__xml_version
    
    # @property
    # def meiversion(self):
    #     if not self.__root:
    #         raise MeiDocumentRootNotSetError("You must set the root element before getting the version number.")
    #     if not self.__root.has_attribute("meiversion"):
    #         raise MeiDocumentRootVersionError("The meiversion attribute is requried, but not present on the root element.")
    #     return self.__root.attribute_by_name("meiversion").value
    
    # def search(self, searchterm, *args, **kwargs):
    #     """ 
    #         Searches an MEI Document for an object name that matches the
    #         search term.
            
    #         @TODO:
    #         Passing in args will narrow down the search by only retrieving
    #         objects with that attribute.
            
    #         Passing in kwargs will narrow down the search by only retrieving
    #         objects where k = v.
    #     """
    #     # there should only be one toplevel element
    #     if not self.__flattened_elements:
    #         self.__flattened_elements = flatten(self.root)
            
    #     return [o for o in self.__flattened_elements if o.name == searchterm]
    
    # def get_by_id(self, id):
    #     """ Gets a document object by ID. """
    #     if not self.__flattened_elements:
    #         self.__flattened_elements = flatten(self.root)
    #     # return (o for o in self.__flattened_elements if o.id == id)
    #     return self.get_by_id_ref("xml:id", id)
    
    # def get_by_facs(self, facsid):
    #     """ Returns the zone element for a given element's facs attribute"""
    #     return self.get_by_id_ref("xml:id", facsid, "zone")
        
    # def get_by_id_ref(self, attrref, attrvalue, tagfilter=None):
    #     """ Generic function by pointer references within the document to get all
    #         other tags that contain this ID. For example, given:
            
    #             ...
    #             <system sbref="123" />
    #             ...
    #             <sb xml:id="123" />
    #             ...
            
    #         The call:
            
    #         get_by_id_ref("sbref", "123")
            
    #         will return a pointer to the <system /> element in the tree.
            
    #         If tagfilter is not None, it will only return the attribute values on
    #         a specific tag, e.g., 
            
    #         get_by_id_ref("sbref", "123", "system").
            
    #         This is useful if you have multiple possible places where an attribute is being
    #         used in the document.
            
    #         Returns a list of MeiElements that match.
    #     """
    #     if not self.__flattened_elements:
    #         self.__flattened_elements = flatten(self.root)
            
    #     if tagfilter:
    #         filt_elements = self.search(tagfilter)
    #         return [f for f in filt_elements if f.has_attribute(attrref) and f.attribute_by_name(attrref).value == attrvalue]
    #     else:
    #         return [f for f in self.__flattened_elements if f.has_attribute(attrref) and f.attribute_by_name(attrref).value == attrvalue]
    
    # def flat(self):
    #     """ Returns a flattened list of the elements in this document. Useful
    #         for searching and doing document-wide operations on many related
    #         elements in different places in the document.
    #     """
    #     if not self.__flattened_elements:
    #         self.__flattened_elements = flatten(self.root)
    #     return self.__flattened_elements
    
    # def get_system(self, element):
    #     """ Returns the 'n' attribute of the system break immediately preceding the given MEI Element. 
    #         If the element is not found, None will be returned. If the element occurs before the first system break,
    #         -1 will be returned.
    #     """
    #     current_system = -1
    #     if not self.__flattened_elements:
    #         self.__flattened_elements = flatten(self.root)
        
    #     for e in self.__flattened_elements:
    #         if e.name == 'sb':
    #             current_system = e.attribute_by_name('n').value
    #         if e.id == element.id:
    #             return current_system
    #     return None
