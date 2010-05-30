# An abstract class representing an MEI attribute. This will subclassed for MEI-specific
# attributes.

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
        return "{0}:{1}".format(self.__name, self.__value)
    
    def getname(self):
        return self.__name
    
    def setname(self, value):
        self.__name = value
    name = property(getname, setname, doc="Get and set the attribute name")
    
    def getvalue(self):
        return self.__value
    
    def setvalue(self, value):
        self.__value = value
    value = property(getvalue, setvalue, doc="Get and set the attribute value")
    
    def getelement(self):
        return self.__element
        
    def setelement(self, value):
        self.__element = value
    element = property(getelement, setelement, doc="Get and set the element for this attribute")

# class MeiAttribute(XMLAttribute):
#     def __init__(self, name=None, value=None, element=None, prefix=None):
#         XMLAttribute.__init__(self, name, value, element, prefix)
#         if element:
#             self.prefix = element.prefix
    
    