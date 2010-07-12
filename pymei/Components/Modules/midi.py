from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute

class cc_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"cc", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class chan_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"chan", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class chanpr_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"chanpr", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class cue_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"cue", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class hex_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"hex", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class lyrics_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"lyrics", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class marker_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"marker", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class metatext_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"metatext", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class midi_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"midi", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)


class noteoff_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"noteoff", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class noteon_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"noteon", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class port_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"port", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class prog_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"prog", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class seqnum_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"seqnum", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class trkname_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"trkname", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class vel_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"vel", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

