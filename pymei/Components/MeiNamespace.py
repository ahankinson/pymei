class MeiNamespace(object):
    def __init__(self, prefix, href):
        self.__href = href
        self.__prefix = prefix
    
    @property
    def href(self):
        return self.__href
    
    @property
    def prefix(self):
        return self.__prefix