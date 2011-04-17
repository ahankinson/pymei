from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute

class facsimile_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"facsimile", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class surface_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"surface", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class zone_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"zone", value=value, parent=parent)
        if attrs:
            self.attributes = attrs
    
    @property
    def ulx(self):
        return self.attribute_by_name('ulx').value
    @ulx.setter
    def ulx(self, value):
        self.attributes = {'ulx': value}
    
    @property
    def uly(self):
        return self.attribute_by_name('uly').value
    @uly.setter
    def uly(self, value):
        self.attributes = {'uly': value}
    
    @property
    def lrx(self):
        return self.attribute_by_name('lrx').value
    @lrx.setter
    def lrx(self, value):
        self.attributes = {'lrx': value}
    
    @property
    def lry(self):
        return self.attribute_by_name('lry').value
    @lry.setter
    def lry(self, value):
        self.attributes = {'lry': value}

