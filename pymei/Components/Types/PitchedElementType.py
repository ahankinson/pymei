"""
    All elements that have pitches should inherit from this class.    
"""
class PitchedElementType(object):
    def __init__():
        self.__pitchname = None
        self.__pitch = None
        self.__octave = None
        # a note may have multiple accidentals. This is *not* the same as
        # double-sharps, etc. The MEI spec allows for multiple <accid> child
        # elements on a note.
        self.__accidentals = []
    
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
        if isinstance(value, types.ListType):
            self.addchildren(value)
        else:
            self.attributes = {'accid': value}

        self._accidentals()

    def has_accidentals(self):
        """ Returns True if the note has an accidental; False otherwise"""
        # accidentals can be attributes or child attributes.
        if self.has_attribute('accid') or self.has_child('accid') or self.has_attribute('accid.ges'):
            return True
        else:
            # no accidental.
            return False
            
    @property
    def octave(self):
        self._octave()
        return self.__octave
    @octave.setter
    def octave(self, value):
        self.attributes = {'oct': value}
        self._octave()

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
        # if self.id == "d1e38008":
        #     pdb.set_trace()
        return "{0}{1}".format("".join(self.__pitch[0:2]), self.__octave)

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
            elif self.has_attribute('accid.ges'):
                self.__accidentals = [self.attribute_by_name('accid.ges').value]
            elif self.has_child('accid'):
                a = []
                children = self.children_by_name('accid')
                for child in children:
                    a.append(child.attribute_by_name('accid').value)
                self.__accidentals = a

    def _octave(self):
        octv = [o for o in self.attributes if o.name == 'oct']
        if len(octv) > 0:
            self.__octave = octv[0].value
        else:
            self.__octave = None
            self.remove_attribute('oct')

