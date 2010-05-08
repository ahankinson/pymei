from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute

class ligature_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"ligature", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class mensuration_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"mensuration", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class proport_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"proport", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

