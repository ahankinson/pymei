from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute

class timeline_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"timeline", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class when_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"when", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

