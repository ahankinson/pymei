# ================================================================
#   MeiElement.py
#
#   An abstract class representing a very basic MEI element.
#   This will most often be used to subclass a "real" element.
#   Some of this is inspired by the atomixlib atom library at 
#   http://trac.defuze.org/browser/oss/atomixlib/
#
#   Author:     Andrew Hankinson
#   License:    MIT
#
# ================================================================

import types
from lxml import etree

#deal with deprecated code.
import warnings
warnings.simplefilter('once')

from pymei import MEI_NS, MEI_PREFIX, PREFIX_TO_NS
from pymei.Components.MeiAttribute import MeiAttribute
from pymei.Components.MeiExceptions import *
from pymei.Helpers import flatten, prefix_to_ns

import logging
lg = logging.getLogger('pymei')

class MeiElement(object):
    def __init__(self, name=None, value=None, prefix=MEI_PREFIX, namespace=MEI_NS, parent=None):
        self.__parent = parent
        if parent:
            parent.children.append(self)
            
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
    
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value):
        value = value.strip()
        self.__value = value
    
    @property
    def svalue(self):
        """
            Get and set the full stripped value for the element. 
            The stripped value is the text value with any inline tags 
            stripped out.
        """
        return self.__svalue
    @svalue.setter
    def svalue(self, value):
        self.__svalue = value
    
    @property
    def tail(self):
        """ Get and set the text tail for the element. """
        return self.__tail    
    @tail.setter
    def tail(self, value):
        # get rid of any pesky newlines. XML shouldn't be newline or white
        # space sensitive anyway.
        value = value.strip()
        self.__tail = value
    
    @property
    def children(self):
        """ Get the direct children of this element """
        return self.__children
    @children.setter
    def children(self, children):
        """ Adds the child elements and, if necessary, the parent. 
            
            Note: This property APPENDS children, it does not overwrite them.
            You should call element.delete_children() to clear the list of
            child elements.
            
            It may not make much sense to use a property to append instead of set,
            so the convenience methods add_children() and add_child() have been
            added.

        """
        if not isinstance(children, types.ListType):
            raise MeiChildError("You must supply a list of child elements.")
        for c in children:
            self.__children.append(c)
            c.parent = self
    
    def add_child(self, child):
        """ 
            Appends a single child element to this element. May make more sense
            to call:
            
            foo.add_child(child) (where 'child' is a single object)
            
            than:
            
            foo.add_children([child])
            
            or
            
            foo.children = child
        """
        self.children = [child]
        
    def add_children(self, children):
        """ Convenience method. May make more sense than the form:
            
            foo.children = [c1, c2, c3]
            
            especially since we handle children by APPENDING to an existing list.
        """
        self.children = children
    
    def addchildren(self, children):
        warnings.warn('Addchildren() has been renamed add_children()', DeprecationWarning)
        self.children = children
    
    def delete_children(self):
        """ Completely removes all child elements from this element."""
        self.__children = []
        
    def remove_child(self, child):
        if child not in self.__children:
            return None
        self.__children.remove(child)
    
    def has_child(self, childname):
        if [c for c in self.children if c.name == childname]:
            return True
        else:
            return False
    
    def children_by_name(self, child_name):
        res = [c for c in self.children if c.name == child_name]
        return res
        
    def remove_children(self, child_name):
        if not self.has_child(child_name):
            return None
        to_remove = (c for c in self.__children if c.name == child_name)
        for child in to_remove:
            if child.name == child_name:
                self.__children.remove(child)
    
    def descendants_by_name(self, desc_name):
        """ Gets all sub-elements that match a query name """
        r = (d for d in flatten(self) if d.name == desc_name)
        res = tuple(r)
        if not res:
            return None
        return res
        
    def descendant_by_id(self, desc_id):
        """ Get a descendant element by that element's unique id """
        r = (d for d in flatten(self) if d.id == desc_id)
        res = tuple(r)
        if not res:
            return None
        elif len(res) > 1:
            raise MeiError("There is more than one element with that ID. Someone screwed up.")
            return None
        else:
            return res[0]

    @property
    def attributes(self):
        return self.__attributes
    @attributes.setter
    def attributes(self, value):
        if not isinstance(value, types.DictType):
            raise MeiAttributeError("You must supply a dictionary of attributes.")
            
        for k,v in value.iteritems():
            # passing in 'self' will automatically add it to this element's 
            # __attributes list. See the __init__ statement in the 
            # MeiAttribute base class to see how this works.
            if self.attribute_by_name(k):
                # we already have this attribute set. Since
                # we can only have one attribute per name, we'll just update 
                # the existing one.
                self.attribute_by_name(k).value = unicode(v)
            else:
                MeiAttribute(name=unicode(k), value=unicode(v), element=self)
            
            # update this object's id if we have a xml:id attribute.
            if k == "xml:id":
                self.__id = v
    
    def remove_attribute(self, attr_name):
        """
            Given an attribute name, removes that from this element's attributes
            
            If it does not have that attribute, it returns None.
        """
        if not self.has_attribute(attr_name):
            return None
        self.attributes.remove(self.attribute_by_name(attr_name))
        
    def attribute_by_name(self, attribute):
        """ Gets the value of an element attribute by name. """
        if not self.has_attribute(attribute):
            return None
        res = [a for a in self.attributes if a.name == attribute]
        if len(res) > 1:
            raise MeiAttributeError("More than one attribute has that name. That's unpossible!")
        else:
            return res[0]
    
    def has_attribute(self, attribute):
        """ Returns True if the element has the attribute; False if it doesn't. """
        if [a for a in self.attributes if a.name == attribute]:
            return True
        else:
            return False
    
    @property
    def name(self):
        """ Gets the name. Read-only, please! This will be set
            by the specific element sub-class, e.g., "note" or "measure".
        """
        return self.__name
    
    @property
    def prefix(self):
        return self.__prefix
    @prefix.setter
    def prefix(self, value):
        self.__prefix = value
    
    @property
    def namespace(self):
        return self.__xmlns
    @namespace.setter
    def namespace(self, value):
        self.__xmlns = value
    
    @property    
    def parent(self):
        return self.__parent
    @parent.setter
    def parent(self, value):
        self.__parent = value
    
    def ancestor_by_name(self, ancestor_name):
        """ 
            Looks for the existence of <ancestor_name> in the element's parents, 
            and their parents parents, etc.
            
            Returns the first ancestor found that matches; otherwise returns None.
        """
        def __anc(nm, meiobj, lst):
            if isinstance(meiobj.parent, types.NoneType):
                # if we've reached a point where there is no parent, we 
                # have failed in our quest.
                return None
            if meiobj.name == nm:
                lst.append(meiobj)
            else:
                __anc(nm, meiobj.parent, lst)
        pnt = self.parent
        plist = []
        __anc(ancestor_name, pnt, plist)
        
        if plist:
            return plist[0]
        else:
            return None
    
    def has_ancestor(self, ancestor_name):
        # convenience wrapper for the ancestor_by_name() method.
        if self.ancestor_by_name(ancestor_name):
            return True
        else:
            return False
    
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, value):
        self.__id = value
        self.attributes = {'xml:id': value}
    
    @property
    def peers(self):
        return self.parent.children
    
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
        a = {}
        for at in self.attributes:
            filtname = prefix_to_ns(at.name)
            if filtname == "namespace":
                continue
            a[str(filtname)] = at.value
        
        el = etree.Element(self.__name, **a)
        if self.value is not None:
            el.text = self.value
        if self.tail is not None:
            el.tail = self.tail
        self.__xml_obj = el
        self.__xml_str = etree.tostring(el, pretty_print=True)
    
    def _dictionary(self):
        import json
        
        d = {self.name:[]}
        if self.attributes is not None:
            el_attb = {"@a": {}}
            for at in self.attributes:
                if at.name is "namespace":
                    continue
                el_attb["@a"][at.name] = at.value
            if el_attb["@a"].values():
                d[self.name].append(el_attb)
        if self.value is not None:
            if self.value.strip() != "":
                d[self.name].append({"@v": self.value})
        if self.tail is not None:
            if self.tail.strip() != "":
                d[self.name].append({"@t": self.tail})
        self.__dictionary = d
        self.__json_str = json.dumps(d)