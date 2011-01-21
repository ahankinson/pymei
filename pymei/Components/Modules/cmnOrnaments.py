from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute

class mordent_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"mordent", value=value, parent=parent)
        if attrs:
            self.attributes = attrs
            
    @property
    def tstamp(self):
        if self.has_attribute('tstamp'):
            return self.attribute_by_name('tstamp').value
        else:
            return None
    @tstamp.setter
    def tstamp(self, value):
        self.attributes = {'tstamp': value}
        
    @property
    def place(self):
        if self.has_attribute('place'):
            return self.attribute_by_name('place').value
        else:
            return None
    @place.setter
    def place(self, value):
        self.attributes = {'place': value}
    
    @property
    def form(self):
        if self.has_attribute('form'):
            return self.attribute_by_name('form').value
        else:
            return None
    @form.setter
    def form(self, value):
        self.attributes = {'form': value}
    
    @property
    def staff(self):
        if self.has_attribute('staff'):
            return self.attribute_by_name('staff').value
        else:
            return None
    @staff.setter
    def staff(self, value):
        self.attributes = {'staff': value}
    
    

class trill_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"trill", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class turn_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"turn", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

