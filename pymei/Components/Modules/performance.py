from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute

class clip_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"clip", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class recording_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"recording", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class performance_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"performance", value=value, parent=parent)
        if attrs:
            self.attributes = attrs
            
class avFile_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"avFile", value=value, parent=parent)
        if attrs:
            self.attributes = attrs



