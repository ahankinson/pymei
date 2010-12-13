# ================================================================
#   MeiDocument.py
#
#   An abstract class representing an MEI attribute.
#
#   Author:     Andrew Hankinson
#   License:    MIT
#
# ================================================================

class MeiAttribute(object):
    def __init__(self, name=None, value=None, element=None, prefix=None):
        self.__element = element # the element this attribute is attached to.
        self.__name = name
        self.__value = value
        self.__prefix = prefix
        
        # automatically add this object to the parent's attribute list.
        if element:
            element.attributes.append(self)
    
    def __repr__(self):
        return "<MeiAttribute {0}>".format(self.__name)
    
    def __str__(self):
        return "<MeiAttribute {0}>".format(self.__name)
        
    def __unicode__(self):
        return u"<MeiAttribute {0}>".format(self.__name)
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = unicode(value)
    
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value):
        self.__value = unicode(value)
    
    # the element this attribute is attached to.
    @property
    def element(self):
        return self.__element
    @element.setter
    def element(self, value):
        self.__element = value

# class MeiAttribute(XMLAttribute):
#     def __init__(self, name=None, value=None, element=None, prefix=None):
#         XMLAttribute.__init__(self, name, value, element, prefix)
#         if element:
#             self.prefix = element.prefix
    
    