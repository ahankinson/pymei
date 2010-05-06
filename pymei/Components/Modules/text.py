from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute

class back(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"back", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class blockquote(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"blockquote", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class div(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"div", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class front(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"front", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class ftrem(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"ftrem", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class head(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"head", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class item(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"item", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class l(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"l", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class lg(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"lg", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class list(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"list", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))