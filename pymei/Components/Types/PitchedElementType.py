"""
    All elements that have pitches should inherit from this class.    
"""
class PitchedElementType(object):
    pitchname_attr = None
    pitch_attr = None
    octave_attr = None
    accidentals_attr = []
    
    def __init__(self):
        # this should probably raise some sort of warning that it shouldn't
        # be instantiated directly.
        pass
    
    @property
    def pitchname(self):
        self._pitchname()
        return self.pitchname_attr
    @pitchname.setter
    def pitchname(self, value):
        self.attributes = {'pname': value}
        self._pitchname()
    @pitchname.deleter
    def pitchname(self):
        self.pitchname_attr = None
        self._pitchname()

    @property
    def pitch(self):
        """ The pitch is composed of the pitch name and accidentals. We won't
            allow anyone to set it directly.
        """
        self._pitch()
        return self.pitch_attr

    @property
    def accidentals(self):
        self._accidentals()
        return self.accidentals_attr
    @accidentals.setter
    def accidentals(self, value):
        if isinstance(value, types.ListType):
            self.add_children(value)
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
        return self.octave_attr
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
        return "{0}{1}".format("".join(self.pitch_attr[0:2]), self.octave_attr)

    ## protected 
    # These methods are responsible for setting the note's properties.
    def _pitchname(self):
        pname = self.attribute_by_name("pname")
        # there should only every be one pitch name per note
        if pname:
            self.pitchname_attr = pname.value
        else:
            self.pitchname_attr = None
            self.remove_attribute('pname')

    def _pitch(self):
        """ Gets a note's pitch *value*. This is the actual value of the pitch,
            and is returned as a list, containing the pitch name and any accidentals.
        """
        # make sure we check for the required properties first!
        self._pitchname()
        self._accidentals()

        self.pitch_attr = [self.pitchname_attr]
        self.pitch_attr.extend(self.accidentals_attr)

    def _accidentals(self):
        if self.has_accidentals():
            if self.has_attribute('accid'):
                self.accidentals_attr = [self.attribute_by_name('accid').value]
            elif self.has_attribute('accid.ges'):
                self.accidentals_attr = [self.attribute_by_name('accid.ges').value]
            elif self.has_child('accid'):
                a = []
                children = self.children_by_name('accid')
                for child in children:
                    a.append(child.attribute_by_name('accid').value)
                self.accidentals_attr = a

    def _octave(self):
        octv = self.attribute_by_name("oct")
        if octv:
            self.octave_attr = octv.value
        else:
            self.octave_attr = None
            self.remove_attribute('oct')

