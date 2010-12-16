from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute
from pymei.Components.MeiExceptions import MeiAttributeError

import types
import uuid

import logging
lg = logging.getLogger('pymei')

class abbr_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"abbr", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class accid_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"accid", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class address_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"address", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class addressline_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"addressline", value=value, parent=parent)
        if attrs:
            self.attributes = attrs
            
class annot_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"annot", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class appinfo_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"appinfo", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class artic_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"artic", value=value, parent=parent)
        if attrs:
            self.attributes = attrs
        self.__articulation = None
    
    @property
    def articulation(self):
        self._articulation()
        return self.__articulation
    @articulation.setter
    def articulation(self, value):
        self.attributes = {'artic': value}
        self._articulation()
    
    # protected
    def _articulation(self):
        artic = [a for a in self.attributes if a.name == "artic"]
        if len(artic) > 0:
            self.__articulation = artic[0].value
        else:
            self.__articulation = None
            self.remove_attribute('artic')
    
class barline_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"barline", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class bibl_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"bibl", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class body_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"body", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class caption_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"caption", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class chord_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"chord", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class clef_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"clef", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class clefchange_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"clefchange", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class custos_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"custos", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class date_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"date", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class dir_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"dir", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class dot_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"dot", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class dynam_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"dynam", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class edition_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"edition", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class ending_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"ending", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class expan_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"expan", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class expansion_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"expansion", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class fw_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"fw", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class group_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"group", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class grpsym_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"grpsym", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class identifier_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"identifier", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class instrdef_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"instrdef", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class instrgrp_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"instrgrp", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class keyaccid_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"keyaccid", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class keychange_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"keychange", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class keysig_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"keysig", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class label_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"label", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class layer_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"layer", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class layerdef_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"layerdef", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class lb_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"lb", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class mdiv_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"mdiv", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class mei_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"mei", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class music_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"music", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class name_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"name", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class note_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"note", value=value, parent=parent)
        if attrs:
            self.attributes = attrs
        self.__pitchname = None
        self.__pitch = [] # [pitchname, accid...]
        self.__duration = None # see also __is_dotted.
        self.__octave = None
        self.__stemdir = None
        # a note may have multiple accidentals. This is *not* the same as
        # double-sharps, etc. The MEI spec allows for multiple <accid> child
        # elements on a note.
        self.__accidentals = []
        self.__is_dotted = False
        self.__dots = None # 1-4 dots.
        self.__tie = None
        self.__is_tied = False # is this note part of a tied group?
        self.__articulations = [] # may be many articulation on a single note.
        
    # some convenience methods specific to notes. 
    @property
    def pitchname(self):
        self._pitchname()
        return self.__pitchname
    @pitchname.setter
    def pitchname(self, value):
        self.attributes = {'pname': value}
        self._pitchname()
    @pitchname.deleter
    def pitchname(self):
        self.__pitchname = None
        self._pitchname()
    
    @property
    def pitch(self):
        """ The pitch is composed of the pitch name and accidentals. We won't
            allow anyone to set it directly.
        """
        self._pitch()
        return self.__pitch
    
    @property
    def accidentals(self):
        self._accidentals()
        return self.__accidentals
    @accidentals.setter
    def accidentals(self, value):
        self.attributes = {'accid': value}
        self._accidentals()
    
    def has_accidentals(self):
        """ Returns True if the note has an accidental; False otherwise"""
        # accidentals can be attributes or child attributes.
        if self.has_attribute('accid') or self.has_child('accid'):
            return True
        else:
            # no accidental.
            return False
    
    @property
    def duration(self):
        self._duration()
        return self.__duration
    @duration.setter
    def duration(self, value):
        self.attributes = {'dur': value}
        self._duration()
    
    @property
    def is_dotted(self):
        """ Returns True if dotted; False if not"""
        # the existence of dots is computed when we check the duration. 
        # therefore, if there is no duration, we may also have not checked
        # for dots yet. We'll double check now.
        self._duration()
        return self.__is_dotted

    @property
    def dots(self):
        self._duration()
        return self.__dots
    @dots.setter
    def dots(self, value):
        self.attributes = {'dots': value}
        self._duration()
    
    @property
    def octave(self):
        self._octave()
        return self.__octave
    @octave.setter
    def octave(self, value):
        self.attributes = {'oct': value}
        self._octave()
    
    @property
    def stemdir(self):
        self._stemdir()
        return self.__stemdir
    @stemdir.setter
    def stemdir(self, value):
        self.attributes = {'stem.dir': value}
        self._stemdir()
    
    @property
    def pitch_octave(self):
        """ 
            Returns the sounding pitch and octave representation, e.g. C4, F#2, B-5.
            Sets a default "B" pitch and "4" octave if neither are present, chosen
            simply because this is the middle line on the treble clef.
        """
        self._pitch()
        self._octave()
        # for now, we'll just grab the first accidental., 
        return "{0}{1}".format("".join(self.__pitch[0:2]), self.__octave)
    
    # Return values for ties can be i(nitial), m(edial), and t(erminal). Note
    # that this only works if the note has a tie attribute! Tie *elements* are
    # dealt with separately.
    @property
    def tie(self):
        self._tie()
        return self.__tie
    @tie.setter
    def tie(self, val):
        if val not in ('i', 'm', 't'):
            raise MeiAttributeError("Tie values must be one of i, m or t.")
        self.attributes = {'tie': val}
        self._tie()
    
    @property
    def is_tied(self):
        self._tie() # make sure we have the latest update.
        return self.__is_tied
    
    @property
    def articulations(self):
        self._articulations()
        return self.__articulations
    @articulations.setter
    def articulations(self, value):
        if value in self.__articulations:
            return None # it's already set.
        self.__articulations.append(value)
        self._articulations()    
    @articulations.deleter
    def articulations(self):
        self.__articulations = []
        self._articulations()
    
    def remove_articulation(self, value):
        if value not in self.__articulations:
            return None
        self.__articulations.remove(value)
        self._articulations()
        
    
    ## protected 
    # These methods are responsible for setting the note's properties.
    def _pitchname(self):
        pname = [p for p in self.attributes if p.name == 'pname']
        # there should only every be one pitch name per note
        if len(pname) > 0:
            self.__pitchname = pname[0].value
        else:
            self.__pitchname = None
            self.remove_attribute('pname')

    def _pitch(self):
        """ Gets a note's pitch *value*. This is the actual value of the pitch,
            and is returned as a list, containing the pitch name and any accidentals.
        """
        # make sure we check for the required properties first!
        self._pitchname()
        self._accidentals()
            
        self.__pitch = [self.__pitchname]
        self.__pitch.extend(self.__accidentals)
    
    def _accidentals(self):
        if self.has_accidentals():
            if self.has_attribute('accid'):
                self.__accidentals = [self.attribute_by_name('accid').value]
            elif self.has_child('accid'):
                a = []
                children = self.children_by_name('accid')
                for child in children:
                    a.append(child.attribute_by_name('accid').value)
                self.__accidentals = a
    
    def _duration(self):
        dur = filter(lambda d: d.name == 'dur', self.attributes)
        if len(dur) > 0:
            self.__duration = dur[0].value
        else:
            self.__duration = None
            self.remove_attribute('dur')
        # a dot can affect the duration. We won't compute the absolute duration,
        # but rather we'll just set a flag that this note is dotted.
        self._is_dotted()
    
    def _is_dotted(self):
        if self.has_attribute('dots') and self.attribute_by_name('dots').value is not '0':
            self.__is_dotted = True
            self.__dots = self.attribute_by_name('dots').value
        else:
            self.__is_dotted = False
            self.__dots = None
            self.remove_attribute('dots')
    
    def _octave(self):
        octv = filter(lambda o: o.name == 'oct', self.attributes)
        if len(octv) > 0:
            self.__octave = octv[0].value
        else:
            self.__octave = None
            self.remove_attribute('oct')
    
    def _stemdir(self):
        stmdir = filter(lambda s: s.getname() == 'stem.dir', self.attributes)
        if len(stmdir) > 0:
            self.__stemdir = stmdir[0].value
        else:
            self.__stemdir = None
            self.remove_attribute('stem.dir')
    
    def _tie(self):
        tie = [t for t in self.attributes if t.name == 'tie']
        if len(tie) > 0:
            self.__tie = tie[0].value
            self.__is_tied = True
        else:
            self.__tie = None
            self.__is_tied = False
            self.remove_attribute('tie')
            
    def _articulations(self):
        if len(self.__articulations) > 1:
            # create elements & clean up attributes
            # remove all articulation children for safety
            self.remove_children('artic')
            self.remove_attribute('artic')
            artc = []
            for art in self.__articulations:
                a = artic_()
                a.id = uuid.uuid4() # give it an id.
                a.attributes = {'artic': art}
                artc.append(a)
            self.addchildren(artc, self)
        elif len(self.__articulations) == 1:
            # create an attribute & clean up any children
            self.attributes = {'artic': self.__articulations[0]}
            self.remove_children('artic')
        else:
            # clean up everything to do with articulations.
            self.remove_children('artic')
            self.remove_attribute('artic')
            self.__articulations = []
            
    
class num_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"num", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class p_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"p", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class pad_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"pad", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class part_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"part", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class parts_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"parts", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class pb_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"pb", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class pgdesc_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"pgdesc", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class pgfoot1_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"pgfoot1", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class pgfoot2_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"pgfoot2", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class pghead1_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"pghead1", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class pghead2_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"pghead2", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class phrase_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"phrase", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class rend_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"rend", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class repository_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"repository", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class rest_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"rest", value=value, parent=parent)
        if attrs:
            self.attributes = attrs
        self.__duration = None
        self.__is_dotted = False
        self.__dots = None
        
    # public
    @property
    def duration(self):
        self._duration()
        return self.__duration
    @duration.setter
    def duration(self, duration):
        self.attributes = {'dur': duration}
        # update the duration state of this object.
        self._duration()
    
    @property
    def dots(self):
        # we'll do the full duration update, instead of just the
        # dot update.
        self._duration()
        return self.__dots
    @dots.setter
    def dots(self, dotnum):
        self.attributes = {'dots': dotnum}
        self._duration()
    
    @property
    def is_dotted(self):
        self._duration()
        return self.__is_dotted
    
    #protected 
    def _duration(self):
        dur = [d for d in self.attributes if d.name == 'dur']
        if len(dur) > 0:
            self.__duration = dur[0].value
        else:
            self.__duration = None
            self.remove_attribute('dur')
        self._is_dotted()
    
    def _is_dotted(self):
        if self.has_attribute('dots') and self.attribute_by_name('dots').value is not '0':
            self.__is_dotted = True
            self.__dots = self.attribute_by_name('dots').value
        else:
            self.__is_dotted = False
            self.__dots = None
            self.remove_attribute('dots')
            
        
class sb_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"sb", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class score_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"score", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class scoredef_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"scoredef", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class section_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"section", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class space_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"space", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class stack_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"stack", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class staff_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"staff", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class staffdef_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"staffdef", value=value, parent=parent)
        if attrs:
            self.attributes = attrs
    
    def get_clef_array(self):
        # returns an array of clef-related attributes.
        clf = filter(lambda c: c.getname().startswith('clef.'), self.getattributes())
        return clf
    
    def get_ppq(self):
        ppq = filter(lambda p: p.getname() == 'ppq', self.getattributes())
        return ppq[0]
    
    

class staffgrp_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"staffgrp", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class syl_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"syl", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class tempo_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"tempo", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class title_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"title", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class titlepage_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"titlepage", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

