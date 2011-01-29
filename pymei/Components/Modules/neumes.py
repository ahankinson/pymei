from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute

class ineume_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"ineume", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class syllable_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"syllable", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class uneume_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"uneume", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

# this is not in the MEI standard yet.
class division_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"division", value=value, parent=parent)
        if attrs:
            self.attributes = attrs
