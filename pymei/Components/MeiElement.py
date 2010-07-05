from pymei import MEI_NS, MEI_PREFIX
from pymei.Components.MeiAttribute import MeiAttribute

import logging
lg = logging.getLogger('pymei')

# An abstract class representing a very basic MEI element.
# This will most often be used to subclass a "real" element.
# This is inspired by the atomixlib atom library at http://trac.defuze.org/browser/oss/atomixlib/

class MeiElement(object):
    def __init__(self, name=None, value=None, prefix=MEI_PREFIX, namespace=MEI_NS, parent=None):
        self.__parent = parent
        self.__prefix = prefix
        self.__xmlns = namespace
        self.__name = name
        self.__value = value
        self.__children = []
        self.__attributes = []
    
    def __repr__(self):
        return u"{0}:{1}".format(self.__xmlns, self.__name)
    
    def __unicode__(self):
        return u"{0}:{1}".format(self.__xmlns, self.__name)
    
    def __str__(self):
        return "{0}:{1}".format(self.__xmlns, self.__name)
    
    def getvalue(self):
        return self.__value
    
    def setvalue(self, value):
        self.__value = value
    value = property(getvalue, setvalue, doc="Get and set the text value for the element")
    
    def getchildren(self):
        return self.__children
    children = property(getchildren, doc="Get the direct children of this element")
    
    def addchildren(self, children):
        lg.debug(children)
        for c in children:
            lg.debug('adding {0} to children'.format(c))
            self.__children.append(c)
    
    def getattributes(self):
        return self.__attributes
        
    def setattributes(self, value):
        for k,v in value.iteritems():
            MeiAttribute(name=k, value=v, element=self) # passing in 'self' will automatically add it to this element's __attributes list
        
    attributes = property(getattributes, setattributes, doc="Get the element attributes")
    
    def getprefix(self):
        return self.__prefix
    
    def setprefix(self, value):
        self.__prefix = value
    prefix = property(getprefix, setprefix, doc="Get and set the prefix for the element")
    
    def getnamespace(self):
        return self.__xmlns
    
    def setnamespace(self, value):
        self.__xmlns = value
    xmlns = property(getnamespace, setnamespace, doc="Get and set the XML namespace for the element")
    
    def getparent(self):
        return self.__parent
    
    def setparent(self, value):
        self.__parent = value
    parent = property(getparent, setparent, doc="Get and set the parent element for this element")
    
    