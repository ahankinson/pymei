from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute

class mordent_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"mordent", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class trill_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"trill", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class turn_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"turn", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

