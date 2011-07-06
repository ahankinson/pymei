from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute
from pymei.Components.Types import PitchedElementType, DurationElementType, SpatialElementType, SpanningElementType
import logging
lg = logging.getLogger('pymei')


class arpeg_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"arpeg", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class beam_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"beam", value=value, parent=parent)
        if attrs:
            self.attributes = attrs
    
    @property
    def first_child(self):
        if len(self.children) > 0:
            return self.children[0]
    
    @property
    def last_child(self):
        if len(self.children) > 0:
            return self.children[-1]
            
class beamSpan_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"beamSpan", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class beatRpt_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"beatRpt", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class bend_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"bend", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class breath_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"breath", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class bTrem_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"bTrem", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class fermata_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"fermata", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class ftrem_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"ftrem", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class gliss_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"gliss", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class hairpin_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"hairpin", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class halfmRpt_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"halfmRpt", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class harpPedal_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"harpPedal", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class measure_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"measure", value=value, parent=parent)
        if attrs:
            self.attributes = attrs
        self.__measure_number = None
        self.__barline = None
        self.__has_barline = False
        self.__repeat = False
    
    @property
    def measure_number(self):
        self._measure_number()
        return self.__measure_number
    @measure_number.setter
    def measure_number(self, value):
        self.attributes = {'n': value}
        self._measure_number()
    
    @property
    def barline(self):
        self._barline()
        return self.__barline
    @barline.setter
    def barline(self, value):
        self.attribute = {'right': value}
        self._barline()
    
    @property
    def has_barline(self):
        self._barline()
        return self.__has_barline
    
    @property
    def is_repeat(self):
        # repeat gets set when we check for the barline.
        # we'll make sure it's set.
        if not self.__barline:
            self._barline()
        return self.__repeat
    
    # protected
    def _measure_number(self):
        mnum = self.attribute_by_name("n")
        if mnum:
            self.__measure_number = mnum.value
        else:
            self.__measure_number = None
            self.remove_attribute('n')
        
    def _barline(self):
        bline = self.attribute_by_name("right")
        if bline:
            self.__barline = bline[0].value
            self.__has_barline = True
            lg.debug(self.__barline)
            if self.__barline in ('rptstart', 'rptend', 'rptboth'):
                self.__repeat = True
        else:
            self.__barline = None
            self.__has_barline = False
            self.__repeat = False
            self.remove_attribute('right')
        

class mRest_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"mRest", value=value, parent=parent)
        if attrs:
            self.attributes = attrs
        # measure rests can have all sorts of possible durations, depending
        # on their measure context. We'll just set up a placeholder attribute
        # for duration, but won't actually compute the duration from its context. 
        # That will be left as an exercise to the reader.
        self.duration = None

class mRpt_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"mRpt", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class mRpt2_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"mRpt2", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class mSpace_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"mSpace", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class multiRest_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"multiRest", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class multiRpt_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"multiRpt", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class octave_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"octave", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class ossia_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"ossia", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class pedal_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"pedal", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class reh_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"reh", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class slur_(MeiElement, SpanningElementType):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"slur", value=value, parent=parent)
        if attrs:
            self.attributes = attrs
            
class tie_(MeiElement, SpanningElementType):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"tie", value=value, parent=parent)
        if attrs:
            self.attributes = attrs
            
class tuplet_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"tuplet", value=value, parent=parent)
        if attrs:
            self.attributes = attrs
            
class tupletSpan_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"tupletSpan", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

