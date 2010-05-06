from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute

class arpeg(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"arpeg", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class beam(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"beam", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class beamspan(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"beamspan", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class beatrpt(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"beatrpt", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class bend(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"bend", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class breath(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"breath", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class btrem(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"btrem", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class fermata(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"fermata", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class gliss(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"gliss", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class hairpin(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"hairpin", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class halfmrpt(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"halfmrpt", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class harppedal(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"harppedal", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class measure(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"measure", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class mrest(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"mrest", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class mrpt(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"mrpt", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class mrpt2(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"mrpt2", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class mspace(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"mspace", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class multirest(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"multirest", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class multirpt(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"multirpt", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class octave(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"octave", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class ossia(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"ossia", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class pedal(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"pedal", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class reh(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"reh", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class slur(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"slur", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class tie(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"tie", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class tuplet(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"tuplet", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

class tupletspan(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"tupletspan", value=value, parent=parent)
        for k,v in attrs.iteritems():
            self.setattributes(MeiAttribute(name=k, value=v))

