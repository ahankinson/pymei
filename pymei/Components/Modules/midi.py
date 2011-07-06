from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute

class cc_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"cc", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class chan_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"chan", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class chanPr_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"chanPr", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class cue_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"cue", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class hex_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"hex", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class lyrics_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"lyrics", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class marker_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"marker", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class metaText_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"metaText", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class midi_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"midi", value=value, parent=parent)
        if attrs:
            self.attributes = attrs


class noteOff_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"noteOff", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class noteOn_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"noteOn", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class port_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"port", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class prog_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"prog", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class seqNum_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"seqNum", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class trkName_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"trkName", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class vel_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"vel", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

