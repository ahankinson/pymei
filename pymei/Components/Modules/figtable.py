from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute

class fig_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"fig", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class figDesc_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"figDesc", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class graphic_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"graphic", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class table_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"table", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class td_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"td", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class th_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"th", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class tr_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"tr", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

