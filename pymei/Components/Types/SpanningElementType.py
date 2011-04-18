"""
    All elements that have a startid and endid attribute.
"""
class SpanningElementType(object):
    def __init_(self):
        self.__startid = None
        self.__endid = None
        self.__staff = None # staff that the tie is attached to.
    
    @property
    def startid(self):
        self._startid()
        return self.__startid
    @startid.setter
    def startid(self, value):
        self.attributes = {'startid': value}
        self._startid()
    
    @property
    def endid(self):
        self._endid()
        return self.__endid
    @endid.setter
    def endid(self, value):
        self.attributes = {'endid': value}
        self._endid()
        
    @property
    def staff(self):
        self._staff()
        return self.__staff
    @staff.setter
    def staff(self, value):
        self.attributes = {'staff': value}
        self._staff()

    # protected
    def _startid(self):
        sid = self.attribute_by_name("startid")
        if sid:
            self.__startid = sid.value
        else:
            self.__startid = None
            self.remove_attribute('startid')

    def _endid(self):
        eid = self.attribute_by_name("endid")
        if eid:
            self.__endid = eid.value
        else:
            self.__endid = None
            self.remove_attribute('endid')

    def _staff(self):
        st = self.attribute_by_name("staff")
        if len(st) > 0:
            self.__staff = st[0].value
        else:
            self.__staf = None
            self.remove_attribute('staff')