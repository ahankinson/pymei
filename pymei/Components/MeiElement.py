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
from pymei.Helpers import flatten, prefix_to_ns

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
        self.__xml_obj = None
        self.__xml_str = None
        self.__json_str = None
        self.__dictionary = None
    
    def __repr__(self):
        return u"<MeiElement {0}:{1}>".format(self.__name, self.__id)
    
    def __unicode__(self):
        return u"<MeiElement {0}:{1}>".format(self.__name, self.__id)
    
    def __str__(self):
        return "<MeiElement {0}:{1}>".format(self.__name, self.__id)
    
    def getvalue(self):
        return self.__value
    
    def setvalue(self, value):
        value = value.strip()
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
        # get rid of any pesky newlines. XML shouldn't be newline or white
        # space sensitive anyway.
        value = value.strip()
        self.__tail = value
    tail = property(gettail, settail, doc="Get and set the text tail for the element.")
    
    def getchildren(self):
        return self.__children
        
    def addchildren(self, children, pnt=None):
        """ Adds the child elements and, if necessary, the parent. """
        for c in children:
            self.__children.append(c)
            if not isinstance(pnt, types.NoneType):
                c.parent = pnt
    children = property(getchildren, addchildren, doc="Get the direct children of this element")
    
    def has_child(self, childname):
        if [c for c in self.children if c.name == childname]:
            return True
        else:
            return False
    
    def children_by_name(self, child_name):
        res = filter(lambda c: c.name == child_name, self.children)
        if not res:
            return None
        return res
    
    
    def descendents_by_name(self, desc_name):
        """ Gets all sub-elements that match a query name """
        res = filter(lambda d: d.name == desc_name, flatten(self))
        if not res:
            return None
        return res
        
    def descendent_by_id(self, desc_id):
        """ Get a descendent element by that element's unique id """
        res = filter(lambda d: d.id == desc_id, flatten(self))
        if not res:
            return None
        elif len(res) > 1:
            raise MeiError("There is more than one element with that ID. Someone screwed up.")
            return None
        else:
            return res[0]
    
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
    
    def has_attribute(self, attribute):
        """ Returns True if the element has the attribute; False if it doesn't. """
        if [a for a in self.attributes if a.name == attribute]:
            return True
        else:
            return False
        
        
    def getname(self):
        return self.__name
        
    name = property(getname, doc = "Gets the name. Read-only, please!")
    
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
    
    def getpeers(self):
        return self.getparent().getchildren()
    peers = property(getpeers, doc="Get adjacent elements.")
    
    def as_xml_object(self):
        self._xml()
        return self.__xml_obj
    
    def as_xml_string(self):
        self._xml()
        return self.__xml_str
        
    def as_json(self):
        # a dictionary is constructed for the JSON object. It just depends
        # on how we spit it out.
        self._dictionary()
        return self.__json_str
    
    def as_dictionary(self):
        """ Returns a representation as a python dictionary. """
        self._dictionary()
        return self.__dictionary
    
    # protected
    def _xml(self):
        from lxml import etree
        
        a = {}
        for at in self.attributes:
            filtname = prefix_to_ns(at.name)
            if filtname is "namespace":
                continue
            a[str(filtname)] = str(at.value)
            
        el = etree.Element(self.__name, **a)
        if self.value is not None:
            el.text = self.value
        if self.tail is not None:
            el.tail = self.tail
        self.__xml_obj = el
        self.__xml_str = etree.tostring(el)
    
    def _dictionary(self):
        import json
        
        d = {self.name:[]}
        if self.attributes is not None:
            el_attb = {"@attributes": {}}
            for at in self.attributes:
                if at.name is "namespace":
                    continue
                el_attb["@attributes"][at.name] = at.value
            if el_attb["@attributes"].values():
                d[self.name].append(el_attb)
        if self.value is not None:
            if self.value.strip() != "":
                d[self.name].append({"@value": self.value})
        if self.tail is not None:
            if self.tail.strip() != "":
                d[self.name].append({"@tail": self.tail})
        self.__dictionary = d
        self.__json_str = json.dumps(d)