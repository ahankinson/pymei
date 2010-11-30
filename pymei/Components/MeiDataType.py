class MeiDataType(object):
    """ Base Class for all MEI Data Types. 
        
        All Datatypes must include a regex definition to validate against.
    """
    def __init__(self, value):
        self.value = value
        self.validate()
    
    def validate(self):
        try:
            v = re.match(self.validation, self.value)
            v.group(0)
            return True
        except AttributeError:
            raise MeiInvalidDataTypeError("Value is not valid for %s." % (self.__class__.__name__,))
        except Exception, e:
            raise MeiError("Unknown error in %s encountered when validating. Error: %s" %
                                             (self.__class__.__name__, e))