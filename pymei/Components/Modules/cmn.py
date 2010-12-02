from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute

class arpeg_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"arpeg", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class beam_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"beam", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class beamspan_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"beamspan", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class beatrpt_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"beatrpt", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class bend_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"bend", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class breath_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"breath", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class btrem_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"btrem", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class fermata_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"fermata", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class gliss_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"gliss", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class hairpin_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"hairpin", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class halfmrpt_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"halfmrpt", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class harppedal_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"harppedal", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class measure_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"measure", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)
        self.__measure_number = None
        self.__barline = None
        self.__has_barline = False
        self.__repeat = False
    
    def get_measure_number(self):
        if not self.__measure_number:
            self._measure_number()
        return self.__measure_number
    measure_number = property(get_measure_number, doc="Gets the measure's number")
    
    def get_barline(self):
        if not self.__barline:
            self._barline()
        return self.__barline
    barline = property(get_barline, doc="Gets the measure's barline")
    
    def get_has_barline(self):
        if not self.__barline:
            self._barline()
        return self.__has_barline
    has_barline = property(get_barline, doc="Does this measure have a barline?")
    
    def get_is_repeat(self):
        # repeat gets set when we check for the barline.
        # we'll make sure it's set.
        if not self.__barline:
            self._barline()
        return self.__repeat
    is_repeat = property(get_is_repeat, doc="Does this measure have a repeat sign?")
    
    # protected
    def _measure_number(self):
        mnum = filter(lambda m: m.name == "n", self.attributes)
        if len(mnum) > 0:
            self.__measure_number = mnum[0].value
        
    def _barline(self):
        bline = filter(lambda b: b.name=="right", self.attributes)
        if len(bline) > 0:
            self.__barline = bline[0].value
            self.__has_barline = True
            if self.__barline in ('rptstart, rptend, rptboth'):
                self.__repeat = True
        

class mrest_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"mrest", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class mrpt_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"mrpt", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class mrpt2_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"mrpt2", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class mspace_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"mspace", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class multirest_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"multirest", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class multirpt_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"multirpt", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class octave_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"octave", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class ossia_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"ossia", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class pedal_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"pedal", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class reh_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"reh", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class slur_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"slur", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class tie_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"tie", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class tuplet_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"tuplet", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

class tupletspan_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"tupletspan", value=value, parent=parent)
        if attrs:
            self.setattributes(attrs)

