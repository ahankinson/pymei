# ================================================================
#   MeiElement.py
#
#   An abstract class representing a very basic MEI element.
#   This will most often be used to subclass a "real" element.
#   Some of this is inspired by the atomixlib atom library at 
#   http://trac.defuze.org/browser/oss/atomixlib/
#
#   Author:     Andrew Hankinson
#   License:    BSD
#
# ================================================================

import types
import uuid

from pymei import MEI_NS, MEI_PREFIX
from pymei.Components.MeiAttribute import MeiAttribute
from pymei.Components.MeiExceptions import MeiAttributeError

import logging
lg = logging.getLogger('pymei')

class MeiElement(object):
    def __init__(self, name=None, value=None, prefix=MEI_PREFIX, namespace=MEI_NS, parent=None):
        self.__parent = parent
        self.__prefix = prefix
        self.__xmlns = namespace
        self.__name = name
        self.__value = value
        self.__tail = None
        self.__children = []
        self.__attributes = []
        self.__svalue = None
        self.__id = None        
    
    def __repr__(self):
        return u"<MeiElement {0}:{1}>".format(self.__name, self.__id)
    
    def __unicode__(self):
        return u"<MeiElement {0}:{1}>".format(self.__name, self.__id)
    
    def __str__(self):
        return "<MeiElement {0}:{1}>".format(self.__name, self.__id)
    
    def getvalue(self):
        return self.__value
    
    def setvalue(self, value):
        self.__value = value
    value = property(getvalue, setvalue, doc="Get and set the text value for the element")
    
    def getsvalue(self):
        return self.__svalue
        
    def setsvalue(self, value):
        self.__svalue = value
    svalue = property(getsvalue, setsvalue, doc="Get and set the full stripped value for the element. The stripped value is the text value with any inline tags stripped out.")
    
    def gettail(self):
        return self.__tail
        
    def settail(self, value):
        self.__tail = value
    tail = property(gettail, settail, doc="Get and set the text tail for the element.")
    
    def getchildren(self):
        return self.__children
    children = property(getchildren, doc="Get the direct children of this element")
    
    def addchildren(self, children, pnt=None):
        """ Adds the child elements and, if necessary, the parent. """
        for c in children:
            self.__children.append(c)
            if not isinstance(pnt, types.NoneType):
                c.parent = pnt
    
    def getattributes(self):
        return self.__attributes
        
    def setattributes(self, value):
        if not isinstance(value, types.DictType):
            raise MeiAttributeError("You must supply a dictionary of attributes.")
            
        for k,v in value.iteritems():
            # passing in 'self' will automatically add it to this element's 
            # __attributes list. See the __init__ statement in the 
            # MeiAttribute base class to see how this works.
            MeiAttribute(name=k, value=v, element=self)
            if str(k) == "xml:id":
                self.__id = v
    attributes = property(getattributes, setattributes, doc="Get the element attributes")
    
    def attribute_by_name(self, attribute):
        """ Gets the value of an element attribute by name. """
        res = filter(lambda a: a.getname() == attribute, self.attributes)
        if len(res) == 0:
            return None
        elif len(res) > 1:
            raise MeiAttributeError("More than one attribute has that name. That's unpossible!")
            return None
        else:
            return res[0]
        
    def getname(self):
        return self.__name
        
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
    
    def getid(self):
        return self.__id
        
    def setid(self, value):
        self.__id = value
    id = property(getid, setid, doc="Get and set the id for this element.")
        