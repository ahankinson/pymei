from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute

class anchoredText_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"anchoredText", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class curve_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"curve", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class line_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"line", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class symbol_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"symbol", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class symbolDef_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"symbolDef", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class symbolTable_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"symbolTable", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

