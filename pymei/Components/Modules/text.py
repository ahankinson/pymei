from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute

class back_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"back", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class blockquote_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"blockquote", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class div_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"div", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class front_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"front", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class ftrem_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"ftrem", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class head_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"head", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class item_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"item", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class l_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"l", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class lg_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"lg", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class list_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"list", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))