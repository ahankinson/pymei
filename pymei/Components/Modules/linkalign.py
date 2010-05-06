from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute

class timeline(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"timeline", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class when(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"when", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

