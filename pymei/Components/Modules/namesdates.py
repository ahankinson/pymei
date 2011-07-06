from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute

class corpName_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"corpName", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class geogName_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"geogName", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class periodName_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"periodName", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class persName_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"persName", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class styleName_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"styleName", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

