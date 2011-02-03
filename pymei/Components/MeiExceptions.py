class MeiError(Exception):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return repr(self.message)

class MeiUnknownModuleError(MeiError): pass
class MeiAttributeError(MeiError): pass
class MeiSchemaNotFoundError(MeiError): pass
class MeiSchemaNotValidError(MeiError): pass
class MeiNotYetImplementedError(MeiError): pass
class MeiXMLParsingError(MeiError): pass
class MeiInvalidDataTypeError(MeiError): pass
class MeiChildError(MeiError): pass

