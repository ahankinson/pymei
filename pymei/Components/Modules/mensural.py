from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute

class ligature(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"ligature", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class mensuration(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"mensuration", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class proport(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"proport", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

