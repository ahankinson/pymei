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

class addrLine_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"addrLine", value=value, parent=parent)
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
    
class barLine_(MeiElement, SpatialElementType):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"barLine", value=value, parent=parent)
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

class clefChange_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"clefChange", value=value, parent=parent)
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

class grpSym_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"grpSym", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class identifier_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"identifier", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class instrDef_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"instrDef", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class instrGrp_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"instrGrp", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class keyAccid_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"keyAccid", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class keychange_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"keychange", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class keySig_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"keySig", value=value, parent=parent)
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

class layerDef_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"layerDef", value=value, parent=parent)
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

class pgDesc_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"pgDesc", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class pgFoot1_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"pgFoot1", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class pgFoot2_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"pgFoot2", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class pgHead1_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"pgHead1", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class pgHead2_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"pgHead2", value=value, parent=parent)
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

class scoreDef_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"scoreDef", value=value, parent=parent)
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

class staffDef_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"staffDef", value=value, parent=parent)
        if attrs:
            self.attributes = attrs
    
    def get_clef_array(self):
        # returns an array of clef-related attributes.
        clf = filter(lambda c: c.getname().startswith('clef.'), self.getattributes())
        return clf
    
    def get_ppq(self):
        ppq = filter(lambda p: p.getname() == 'ppq', self.getattributes())
        return ppq[0]
    
    

class staffGrp_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"staffGrp", value=value, parent=parent)
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

class titlePage_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"titlePage", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

# added in MEI 2011
class castItem_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"castItem", value=value, parent=parent)
        if attrs:
            self.attributes = attrs
            
            
class roleDesc_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"roleDesc", value=value, parent=parent)
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

class castList_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"castList", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class castGrp_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"castGrp", value=value, parent=parent)
        if attrs:
            self.attributes = attrs



