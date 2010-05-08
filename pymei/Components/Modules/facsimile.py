from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute

class facsimile_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"facsimile", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class surface_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"surface", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class zone_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"zone", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

