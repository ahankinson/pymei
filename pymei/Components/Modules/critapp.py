from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute

class app_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"app", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class lem_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"lem", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class rdg_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"rdg", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

