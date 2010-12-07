from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute

class corpname_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"corpname", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class geogname_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"geogname", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class periodname_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"periodname", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class persname_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"persname", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class stylename_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"stylename", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

