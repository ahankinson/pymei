from pymei import ENCODING, MEI_PREFIX, MEI_NS

# A class representing an MEI document.
# Provides an interface for accessing and adding elements.
class MeiDocument(object):
    def __init__(self, encoding=ENCODING):
        self.__encoding = ENCODING
        self.__default_prefix = MEI_PREFIX
        self.__default_namespace = MEI_NS
        self.elements = []
    
    def addelement(self, element):
        self.elements.append(value)
    
    def delelement(self, element):
        del element
    
    def getencoding(self):
        return self.__encoding
    
    def setencoding(self, value):
        self.__encoding = value
        
    encoding = property(getencoding, setencoding, doc="Get and set a document's encoding")
    
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