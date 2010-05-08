from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute

class anchoredtext_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"anchoredtext", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class curve_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"curve", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class line_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"line", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class symbol_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"symbol", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class symboldef_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"symboldef", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class symboltable_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"symboltable", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

