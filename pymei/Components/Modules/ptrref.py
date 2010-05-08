from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute

class extptr_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"extptr", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class extref_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"extref", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class ptr_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"ptr", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class ref_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"ref", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

