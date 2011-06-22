from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute
from pymei.Components.MeiExceptions import MeiAttributeError

from pymei.Components.Types import PitchedElementType, DurationElementType, SpatialElementType
from pymei.Helpers import generate_mei_id
import types

import logging
lg = logging.getLogger('pymei')

import pdb

class abbr_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"abbr", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class accid_(MeiElement, SpatialElementType):
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
    
class barline_(MeiElement, SpatialElementType):
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

class chord_(MeiElement, DurationElementType, SpatialElementType):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"chord", value=value, parent=parent)
        if attrs:
            self.attributes = attrs
        self.__stemdir = None
        
    @property
    def stemdir(self):
        self._stemdir()
        return self.__stemdir
    @stemdir.setter
    def stemdir(self, value):
        self.attributes = {'stem.dir': value}
        self._stemdir()
        
    def _stemdir(self):
        stmdir = self.attribute_by_name("stem.dir")
        if stmdir:
            self.__stemdir = stmdir.value
        else:
            self.__stemdir = None
            self.remove_attribute('stem.dir')

class clef_(MeiElement, SpatialElementType):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"clef", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class clefchange_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"clefchange", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class custos_(MeiElement, SpatialElementType, PitchedElementType):
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

class note_(MeiElement, PitchedElementType, DurationElementType, SpatialElementType):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"note", value=value, parent=parent)
        if attrs:
            self.attributes = attrs
        self.__stemdir = None
        self.__tie = None
        self.__is_tied = False # is this note part of a tied group?
        
        self.__tuplet = None # tuplet value
        self.__is_tuplet = False # is this note part of a tuplet group?
        self.__articulations = [] # may be many articulation on a single note.
        
    @property
    def stemdir(self):
        self._stemdir()
        return self.__stemdir
    @stemdir.setter
    def stemdir(self, value):
        self.attributes = {'stem.dir': value}
        self._stemdir()
    
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
        
    
    def _stemdir(self):
        stmdir = self.attribute_by_name("stem.dir")
        if stmdir:
            self.__stemdir = stmdir.value
        else:
            self.__stemdir = None
            self.remove_attribute('stem.dir')
    
    def _tie(self):
        tie = self.attribute_by_name("tie")
        if tie:
            self.__tie = tie.value
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
                a.id = generate_mei_id() # give it an id.
                a.attributes = {'artic': art}
                artc.append(a)
            self.add_children(artc)
        elif len(self.__articulations) == 1:
            # create an attribute & clean up any children
            self.attributes = {'artic': self.__articulations[0]}
            self.remove_children('artic')
        else:
            # clean up everything to do with articulations.
            self.remove_children('artic')
            self.remove_attribute('artic')
            self.__articulations = []
    
    def _tuplet(self):
        tuplet = self.attribute_by_name("tuplet")
        if tuplet:
            self.__tuplet = tuplet.value
            self.__is_tuplet = True
        else:
            self.__tuplet = None
            self.__is_tuplet = False
            self.remove_attribute('tuplet')
            
    
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

class rest_(MeiElement, DurationElementType, SpatialElementType):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"rest", value=value, parent=parent)
        if attrs:
            self.attributes = attrs
        
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

class staff_(MeiElement, SpatialElementType):
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

# added in MEI 2011
class castitem_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"castitem", value=value, parent=parent)
        if attrs:
            self.attributes = attrs
            
            
class roledesc_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"roledesc", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class actor_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"actor", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class role_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"role", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class castlist_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"castlist", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class castgrp_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"castgrp", value=value, parent=parent)
        if attrs:
            self.attributes = attrs



