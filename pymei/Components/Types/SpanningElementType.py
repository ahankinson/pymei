"""
    All elements that have a startid and endid attribute.
"""
class SpanningElementType(object):
    startid_attr = None
    endid_attr = None
    staff_attr = None
    
    def __init_(self):
        pass
        
    @property
    def startid(self):
        self._startid()
        return self.startid_attr
    @startid.setter
    def startid(self, value):
        self.attributes = {'startid': value}
        self._startid()
    
    @property
    def endid(self):
        self._endid()
        return self.endid_attr
    @endid.setter
    def endid(self, value):
        self.attributes = {'endid': value}
        self._endid()
        
    @property
    def staff(self):
        self._staff()
        return self.staff_attr
    @staff.setter
    def staff(self, value):
        self.attributes = {'staff': value}
        self._staff()

    # protected
    def _startid(self):
        sid = self.attribute_by_name("startid")
        if sid:
            self.startid_attr = sid.value
        else:
            self.startid_attr = None
            self.remove_attribute('startid')

    def _endid(self):
        eid = self.attribute_by_name("endid")
        if eid:
            self.endid_attr = eid.value
        else:
            self.endid_attr = None
            self.remove_attribute('endid')

    def _staff(self):
        st = self.attribute_by_name("staff")
        if len(st) > 0:
            self.staff_attr = st[0].value
        else:
            self.staff_attr = None
            self.remove_attribute('staff')