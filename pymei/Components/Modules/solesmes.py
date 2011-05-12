from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute
from pymei.Components.Types import SpatialElementType

class syllable_(MeiElement, SpatialElementType):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"syllable", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class neume_(MeiElement, SpatialElementType):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"neume", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

# this is not in the MEI standard yet.
class division_(MeiElement, SpatialElementType):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"division", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class episema_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"episema", value=value, parent=parent)
        if attrs:
            self.attributes = attrs
            
class nc_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"nc", value=value, parent=parent)
        if attrs:
            self.attributes = attrs