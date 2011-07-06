from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute
from pymei.Components.Types import SpatialElementType

class back_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"back", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class blockquote_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"blockquote", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class div_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"div", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class front_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"front", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class fTrem_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"fTrem", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class head_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"head", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class item_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"item", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class l_(MeiElement, SpatialElementType):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"l", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class lg_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"lg", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class list_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"list", value=value, parent=parent)
        if attrs:
            self.attributes = attrs
