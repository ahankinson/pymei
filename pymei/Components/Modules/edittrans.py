from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute

class add(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"add", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))
            
class choice(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"choice", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class corr(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"corr", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class damage(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"damage", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class del(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"del", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class gap(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"gap", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class handshift(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"handshift", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class orig(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"orig", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class reg(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"reg", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class restore(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"restore", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class sic(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"sic", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class subst(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"subst", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class supplied(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"supplied", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class unclear(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"unclear", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

