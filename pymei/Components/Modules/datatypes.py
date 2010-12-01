from pymei.Components.MeiDataType import MeiDataType
from pymei.Components.MeiExceptions import MeiError, MeiInvalidDataTypeError
import re

class data_BEND_AMOUNT(MeiDataType):
    """ Either a decimal value or a token. The decimal values are
      limited to .25, .5, .75, or 1, while the token values are restricted to
      'full'. """
    validation = r'^(full|0?\.25|0?\.50?|0?\.75|1\.?0?)'
    
class data_BEAT(MeiDataType):
    """ A beat location, i.e., [0-9]+(\.?[0-9]*)? The value must
      fall between 0 and the numerator of the time signature + 1, where 0
      represents the left barline and the upper bound represents the right
      barline. For example, in 12/8 the value must be in the range from 0 to
      13. 
      
      i.e. beats[.fractional beat part]
      """
    validation = r'^(\d+(\.?\d*)?)'
    
class data_BEATRPT_REND(MeiDataType):
    """ Visual and performance information for a repeated beat
      symbol. """
    validation = r'^(mixed|4|8|16|32|64|128)(?!\.)'

class data_COLOR(MeiDataType):
    """Either a hexadecimal color value, ie., x[0-9A-Fa-f]{6,6} OR
      a descriptive word, i.e., aqua, black, blue, fuchsia, gray, green, lime,
      maroon, navy, olive, purple, red, silver, teal, white, or yellow, for
      colors defined by the HTML 4.01 specification."""
    validation = r'(x[0-9A-Fa-f]{6,6}|aqua|black|fuchsia|gray|green|lime|maroon|navy|olive|purple|red|silver|teal|white|yellow)'

class data_DEGREES(MeiDataType):
    """ 360th-unit measure of a cirle's circumference; optionally
      signed decimal number, i.e., [+-]?[0-9]+(\.?[0-9]*)? """
    validation = r'^([+-]?\d+(\.?[\d]*)?)'

class data_FINGER_FRET(MeiDataType):
    """ In a guitar chord diagram, a label indicating which finger,
      if any, should be used to play an individual string. The values 'x' and
      'o' indicate stopped and open strings, respectively. """
    validation = r'^(x|o|1|2|3|4)(?!.)'

class data_FRET(MeiDataType):
    """ In a guitar chord diagram, the fret where the finger should
      be placed. Since guitar chord diagrams are limited to the range of frets
      that fall under the hand, the value here is also limited. The pos
      (position) attribute on the chorddef element must be used to indicate at
      which fret this range begins. """
    validation = r'^(1|2|3|4|5)(?!.)'

class data_ISODATE(MeiDataType):
    """ ISO Date Formats. Validation Regex taken from
        http://underground.infovark.com/2008/07/22/iso-date-validation-regex/"""
    validation = r'^[0-9][0-9][0-9][0-9](-[0-1][0-9](-[0-3][0-9](T[0-9][0-9](:[0-9][0-9](:[0-9][0-9])?)?)?)?)?$'

class data_ISOTIME(MeiDataType):
    """ ISO 24-hour time format: HH:MM:SS.ss i.e.,
      [0-9][0-9]:[0-9][0-9]:[0-9][0-9](\.?[0-9]*)? """
    validation = r'^([01]\d|2[0-3])\D?([0-5]\d)\D?([0-5]\d)?\D?(\d{3})?$'

class data_MEASUREBEAT(MeiDataType):
    """ A duration expressed as a count of measures plus a beat
      location, i.e., [0-9]+m *\+ *[0-9]+(\.?[0-9]*)?, e.g., dur="1m + 3.5"
      indicates a duration of 1 measure plus 3 and one half beats or, in other
      words, on the 2nd half of the 3rd beat of the next measure. The measure
      number must be in the range of 0 to the number of remaining measures and
      the beat number must be in the range from 0 to the numerator of the time
      signature plus 1. For example, for an event starting in the first measure
      of a piece containing 6 measures in 6/8, the measure number must be
      between 0 to 5 and the beat number must be within the range from 0 to 7,
      e.g., "4m+3". """
    validation = r'^[0-9]+m *\+ *[0-9]+(\.?[0-9]*)?'

class data_MIDINAMES(MeiDataType):
    """ General MIDI Instrument Names """
    validation = re.compile(r"""^(
      Acoustic_Grand_Piano|Bright_Acoustic_Piano|Electric_Grand_Piano|Honky-tonk_Piano|
      Electric_Piano_1|Electric_Piano_2|Harpsichord|Clavi|Celesta|Glockenspiel|
      Music_Box|Vibraphone|Marimba|Xylophone|Tubular_Bells|Dulcimer|Drawbar_Organ|
      Percussive_Organ|Rock_Organ|Church_Organ|Reed_Organ|Accordion|Harmonica|
      Tango_Accordion|Acoustic_Guitar_nylon|Acoustic_Guitar_steel|Electric_Guitar_jazz|
      Electric_Guitar_clean|Electric_Guitar_muted|Overdriven_Guitar|Distortion_Guitar|
      Guitar_harmonics|Acoustic_Bass|Electric_Bass_finger|Electric_Bass_pick|
      Fretless_Bass|Slap_Bass_1|Slap_Bass_2|Synth_Bass_1|Synth_Bass_2|Violin|
      Viola|Cello|Contrabass|Tremolo_Strings|Pizzicato_Strings|Orchestral_Harp|
      Timpani|String_Ensemble_1|String_Ensemble_2|SynthStrings_1|SynthStrings_2|
      Choir_Aahs|Voice_Oohs|Synth_Voice|Orchestra_Hit|Trumpet|Trombone|Tuba|
      Muted_Trumpet|French_Horn|Brass_Section|SynthBrass_1|SynthBrass_2|
      Soprano_Sax|Alto_Sax|Tenor_Sax|Baritone_Sax|Oboe|English_Horn|Bassoon|
      Clarinet|Piccolo|Flute|Recorder|Pan_Flute|Blown_Bottle|Shakuhachi|Whistle|
      Ocarina|Lead_1_square|Lead_2_sawtooth|Lead_3_calliope|Lead_4_chiff|Lead_5_charang|
      Lead_6_voice|Lead_7_fifths|Lead_8_bass_and_lead|Pad_1_new_age|Pad_2_warm|
      Pad_3_polysynth|Pad_4_choir|Pad_5_bowed|Pad_6_metallic|Pad_7_halo|Pad_8_sweep|
      FX_1_rain|FX_2_soundtrack|FX_3_crystal|FX_4_atmosphere|FX_5_brightness|
      FX_6_goblins|FX_7_echoes|FX_8_sci-fi|Sitar|Banjo|Shamisen|Koto|Kalimba|
      Bagpipe|Fiddle|Shanai|Tinkle_Bell|Agogo|Steel_Drums|Woodblock|Taiko_Drum|
      Melodic_Tom|Synth_Drum|Reverse_Cymbal|Guitar_Fret_Noise|Breath_Noise|
      Seashore|Bird_Tweet|Telephone_Ring|Helicopter|Applause|Gunshot)""", re.X)

class data_MIDITEMPO(MeiDataType):
    """ MIDI quarter notes per minute: positive integer in the
      range 10-1000 """
    validation = r'^([0-9]{2,3}$|1000$)'

class data_MODUSMAIOR(MeiDataType):
    """ Maxima-long relationship values. """
    validation = r'^([2-3]$)(?!\.)'

class data_MODUSMINOR(MeiDataType):
    """ Long-breve relationship values."""
    validation = r'^([2-3]$)(?!\.)'

class data_OCTAVE_DIS(MeiDataType):
    """ The amount of octave displacement; that is, '8' (as in
      '8va' for 1 octave), '15' (for 2 octaves), or rarely '22' (for 3
      octaves)."""
    validation = r'^(8|15|22)$'

class data_ORIENTATION(MeiDataType):
    """ Rotation or reflection of base symbol values."""
    validation = r'^(reversed|90CW|90CCW)$'

class data_PAGE_PANELS(MeiDataType):
    """ The number of panels per page."""
    validation = r'^([1-2]$)(?!\.)'
    
class data_PERCENT(MeiDataType):
    """ Positive decimal number plus '%', i.e.,
      [0-9]+(\.?[0-9]*)?\%
    """
    validation = r'^[0-9]+(\.?[0-9]*)?%'

class data_PROLATIO(MeiDataType):
    """ Semibreve-minim relationship values. """
    validation = r'^([2-3]$)(?!\.)'

class data_RATIO(MeiDataType):
    """ A ratio, i.e., [0-9]+(\.?[0-9]*)?:[0-9]+(\.?[0-9]*)? For
      example, "40:7.2319 """
    validation = r'[0-9]+(\.?[0-9]*)?:[0-9]+(\.?[0-9]*)?'

class data_SLASH(MeiDataType):
    """ The number of slashes to be rendered for
      tremolandi."""
    validation = r'^([1-6]$)(?!\.)'
    
class data_STRINGNUMBER(MeiDataType):
    """ In string tablature, the number of the string to be played,
      i.e., [1-9]+."""
    validation = r'^([1-9]+)(?!\.)'
    
class data_TEMPOVALUE(MeiDataType):
    """Beats (meter signature denominator) per minute, e.g.
      120.
      This may need to be adjusted in the spec to allow for decimal beats; 
      e.g. 120.5BPM. We'll allow this here."""
    validation = r'^([1-9]+\.?[0-9]*?)'

class data_TEMPUS(MeiDataType):
    """ Breve-semibreve relationship values """
    validation = r'^([2-3]$)(?!\.)'

class data_TSTAMPOFFSET(MeiDataType):
    """ A positive or negative offset from the value given in the
      tstamp attribute in terms of musical time, i.e., beats[.fractional beat
      part] """
    validation = r'^(\d+(\.?\d*)?)'

class data_URI(MeiDataType):
    """ a Uniform Resource Identifier, see [RFC2396]
        For now, allow anything.
    """
    validation = r'^(.*)'

class data_ACCIDENTAL_EXPLICIT(MeiDataType):
    """ Accidental attribute values: s = sharp, f = flat, ss =
      dblsharp, x=dblsharp, ff = dblflat, xs = triple sharp, tb = triple flat, n
      = natural, nf = naturalflat, ns = naturalsharp. ss indicates the use of 2
      sharp signs, while x indicates the use of a single double sharp. nf and ns
      are used to cancel dbflats and dblsharps, respectively. su = sharp note
      qtr. tone up, sd = sharp note qtr. tone down, fu = flat note qtr. tone up,
      fd = flat note qtr. tone down, nu = natural note qtr. tone up, nd =
      natural note quarter tone down. Quarter-tone accidentals listed in Read,
      p. 145."""
    validation = r'^(s|f|ss|x|ff|xs|tb|n|nf|ns|su|sd|fu|fd|nu|nd)$'

class data_ACCIDENTAL_IMPLICIT(MeiDataType):
    """ Accidental attribute values: s = sharp, f = flat, ss =
      dblsharp, x=dblsharp, ff = dblflat, xs = triple sharp, tb = triple flat, n
      = natural, nf = naturalflat, ns = naturalsharp. ss indicates the use of 2
      sharp signs, while x indicates the use of a single double sharp. nf and ns
      are used to cancel dbflats and dblsharps, respectively. su = sharp note
      qtr. tone up, sd = sharp note qtr. tone down, fu = flat note qtr. tone up,
      fd = flat note qtr. tone down, nu = natural note qtr. tone up, nd =
      natural note quarter tone down. Quarter-tone accidentals listed in Read,
      p. 145."""
    validation = r'^(s|f|ss|ff|n)$'

class data_ARTICULATION(MeiDataType):
    """ The following list of articulations mostly corresponds to
      symbols 1D110-1D111, 1D17B-1D182, 1D185-1D189, 1D1AA-1D1AD, 1D1B3-1D1B5
      from the Western Musical Symbols portion of the Unicode Standard, v. 3.1.
      The dot and stroke values may be used in cases where interpretation is
      difficult or not desirable."""
    validation = re.compile(r"""^(acc|stacc|ten|stacciss|marc|marc-stacc|acc-marc|spicc|
      rip|doit|plop|fall|bend|flip|smear|dnbow|upbow|harm|snap|
      fingernail|ten_stacc|damp|dampall|open|stop|dbltongue|trpltongue|heel|
      toe|tap|lhpizz|dot|stroke)$""", re.X)
    
class data_ARTICULATIONS(MeiDataType):
    """ One or more values from the list given in the definition of
      data.ARTICULATION.
      
      TODO: This regex needs work: How would a correct list of articulations look?
      """
    validation = re.compile(r"""^((acc|stacc|ten|stacciss|marc|marc-stacc|acc-marc|spicc|
        rip|doit|plop|fall|bend|flip|smear|dnbow|upbow|harm|snap|
        fingernail|damp|dampall|open|stop|dbltongue|trpltongue|heel|
        toe|tap|lhpizz|dot|stroke)[ ]?){1,}""", re.X)

class data_AUGMENTDOT(MeiDataType):
    """ Dots attribute values (number of augmentation dots) (Read,
      113-119, ex. 8-21)"""
    validation = r'^([1-4]$)(?!\.)'
    
class data_BARPLACE(MeiDataType):
    """ Placement of barlines: 'mensur' = between staves only,
      'staff' = between and across staves as necessary, 'takt' = short line
      above staff or through top line. The default value is
      'staff'."""
    validation = r'^(mensur|staff|takt)$'
    
class data_BARRENDITION(MeiDataType):
    """ Renderings of barlines"""
    validation = r'^(dashed|dotted|dbl|dbldashed|dbldotted|end|invis|rptstart|rptboth|rptend|single)$'
    
class data_BEAM(MeiDataType):
    """ Beam attribute values: initial, medial, terminal. Nested
      beaming is permitted. """
    validation = r'^(i|m|t|)([1-6])$'

class data_BEAMS(MeiDataType):
    """ One or more from the list given in the definition of the
      BEAM datatype."""
    validation = r'^((i|m|t)[1-6][ ]?){1,}'

class data_BOOLEAN(MeiDataType):
    """ Boolean attribute values"""
    validation = r'^(true|false)$'

class data_CERTAINTY(MeiDataType):
    """ Values for certainty attribute"""
    validation = r'^(high|medium|low|unknown)$'

class data_CLEFLINE(MeiDataType):
    """ Clef line attribute values"""
    validation = r'^([0-9]+)(?!\.)'

class data_CLEFSHAPE(MeiDataType):
    """ Clef shape attribute values (Read, p.53-56)"""
    validation = r'^(G|GG|F|C|perc|TAB)$'

class data_CLUSTER(MeiDataType):
    """ Tone-clusters"""
    validation = r'^(whbox|blbox)$'

class data_CURVERENDITION(MeiDataType):
    """ Renderings of curves"""
    validation = r'^(medium|wide|dashed|dotted)$'
    
class data_DURATION(MeiDataType):
    """ Logical, that is, written, duration attribute values for
      the CMN repertoire. Whole note duration = '1'."""
    validation = r'^(long|breve|1|2|4|8|16|32|64|128|256|512|1024|2048)$'

class data_ENCLOSURE(MeiDataType):
    """ Enclosures for editorial notes and accidentals"""
    validation = r'^(paren|brack)$'

class data_FONTFAMILY(MeiDataType):
    """ Font family (for text) attribute values. Mup-acceptable
      values: avantgarde, bookman, courier, helvetica, newcentury, palatino,
      times."""
    validation = r'^(.*)$'

class data_FONTNAME(MeiDataType):
    """ Font name (for text) attribute values. Mup-acceptable
      values: rom, ital, bold, boldital"""
    validation = r'^(.*)$'

class data_FONTSTYLE(MeiDataType):
    """ Font style (for text) attribute values. 'normal' = 'rom' in Mup."""
    validation = r'^(ital|normal|oblique)$'

class data_FONTWEIGHT(MeiDataType):
    """ Font weight (for text) attribute values"""
    validation = r'^(bold)$'

class data_FRETNUMBER(MeiDataType):
    """ In string tablature, the fret number, i.e., [1-9]. The
      value 'o' may be used instead of a numerica value to indicate the open
      string."""
    validation = r'^([1-9]|o)$(?!\.)'

class data_GLISSANDO(MeiDataType):
    """ Analytical glissando attribute values: i(nitial), m(edial), t(erminal)"""
    validation = r'^(i|m|t)$'

class data_GRACE(MeiDataType):
    """ Do grace notes get time from the current (acc) or previous (unacc) one?"""
    validation = r'^(acc|unacc|unknown)$'

class data_HEADSHAPE(MeiDataType):
    """ Notehead shapes"""
    validation = re.compile(r"""^(quarter|half|whole|dblwhole|filldiamond|diamond|
            dwdiamond|fillisotriangle|isotriangle|dwhisotriangle|fillpiewedge|piewedge|
            dwhpiewedge|fillrectangle|rectangle|dwhrectangle|fillrtriangle|rtriangle|
            dwrtriangle|fillurtriangle|urtriangle|dwurtriangle|fillsemicircle|
            semicircle|dwsemicircle|fillslash|slash|dwslash|x|blank|circlex|cross)$""", re.X)

class data_INEUMENAME(MeiDataType):
    """ Interrupted neume, i.e. neume written as 2 or more sub-neumes"""
    validation = r'^(pessubpunctis|climacus|scandicus|bistropha|tristropha|pressusminor|pressusmaior)$'
    
class data_INEUMEFORM(MeiDataType):
    """ Interrupted neume forms"""
    validation = r'^(liquescent1|liquescent2|tied|tiedliquescent1|tiedliquescent2)$'

class data_KEYSIGTOKEN(MeiDataType):
    """ A token describing the pitch name, inflection, and octave number of an
        altered pitch in a key signature."""
    validation = r'^([a-g][s|f|ss|x|ff|n|nf|ns|su|sd|fu|fd|nu|nd][0-9])$'

class data_KEYSIGNATURE(MeiDataType):
    """ Key signature may be indicated by a value showing where the
      key is in the circle of fifths. Mixed key signatures, e.g. those
      consisting of a mixture of flats and sharps, and key signatures with
      unorthodox placement of the accidentals (Read, p. 143) must be indicated
      by setting the key.sig attribute to 'mixed' and providing explicit keysig
      info in the key.sig.mixed attribute."""
    validation = r'^(mixed|0|[1-7][f|s])$'

class data_LAYERSCHEME(MeiDataType):
    """ Indicates how stems should be drawn when more than one
      layer is present and stem directions are not indicated on the notes/chords
      themselves. '1' indicates that there is only a single layer on a staff.
      '2o' means there are two layers with opposing stems. '2f' indicates two
      'free' layers; that is, opposing stems will be drawn unless one of the
      layers has 'space'. In that case, stem direction in the remaining layer
      will be determined as if there were only one layer. '3o' and '3f' are
      analogous to '2o' and '2f' with three layers allowed. What about more than
      3 layers?"""
    validation = r'^(1|2o|2f|3o|3f)$'

class data_LIGATUREFORM(MeiDataType):
    """ Ligature forms"""
    validation = r'^(recta|obliqua)$'

class data_LINERENDITION(MeiDataType):
    """ Renderings of lines"""
    validation = r'^(narrow|medium|wide|dashed|dotted|wavy)$'

class data_MENSURATIONSIGN(MeiDataType):
    """ Mensuration attribute values

        TODO: Should this be expanded to include C. and O.?
    """
    validation = r'^(C|O)$'

class data_METERSIGN(MeiDataType):
    """ Meter.sym attribute values for CMN notation"""
    validation = r'^(common|cut)$'

class data_MIDICHANNEL(MeiDataType):
    """ MIDI channel numbers"""
    validation = r'^([0-9][1-6]?)$(?!\.)'

class data_MIDIVALUE(MeiDataType):
    """ MIDI values are in the following range
    
        TODO: Check above 127.
    """
    validation = r'^([1-9][0-9]?[0-9]?)$'

class data_MODE(MeiDataType):
    """ Modes"""
    validation = r'^(major|minor|dorian|phrygian|lydian|mixolydian|aeolian|locrian)$'

class data_MUSICFONT(MeiDataType):
    """ Music font family"""
    validation = r'^(.*)$'

class data_OCTAVE(MeiDataType):
    """Oct attribute values. The default values conform to
      Acoustical Society of America representation. Read, p.
      44."""
    validation = r'^([0-9])$'

class data_PGSCALE(MeiDataType):
    """ Page scale factor. Page.scale may be expressed as a
      percentage of a programmatically-determined "usual" size or as a ratio of
      virtual units to real-world units.
      
      We can override the base validation with our own here.
      """
    def validate(self):
        try:
            data_PERCENT(self.value)
        except MeiInvalidDataTypeError:
            try:
                data_RATIO(self.value)
            except MeiInvalidDataTypeError:
                raise MeiInvalidDataTypeError("Value is not valid for %s." % (self.__class__.__name__,))
        except Exception, e:
            MeiError("Unknown error in %s encountered when validating. Error: %s" %
                                             (self.__class__.__name__, e))

class data_PGUNITS(MeiDataType):
    """ Values for real-world unit attributes"""
    validation = r'^(in|cm|mm)$'

class data_PITCHCLASS(MeiDataType):
    """ Pclass (pitch class) attribute values"""
    validation = r'^([0-9][0-1]?)$'

class data_PITCHNAME(MeiDataType):
    """ The pitch names (gamut) used within a single octave. The
      default values conform to Acoustical Society of America
      representation."""
    validation = r'^([a-gA-G])$'

class data_PITCHNAME_GES(MeiDataType):
    """ Gestural pitch names need an additional value for when the
      notated pitch is not to be sounded."""
    validation = r'^([a-gA-G]|none)$'

class data_PITCHNUMBER(MeiDataType):
    """ Pnum (pitch number, e.g. MIDI) attribute values"""
    validation = r'^([0-9]+)$'

class data_PLIST(MeiDataType):
    """Participant list referencing method."""
    validation = r'^(.*)$'

class data_PLACE(MeiDataType):
    """ Location of symbol relative to other notational
      components."""
    validation = r'^(above|below)$'

class data_OTHERSTAFF(MeiDataType):
    """ For musical material designated to appear on another staff,
      the location of the staff relative to the current one; i.e., the staff
      above or the staff below."""
    validation = r'^(above|below)$'

class data_STAFFREL(MeiDataType):
    """ Location of musical material relative to a staff."""
    validation = r'^(above|below|within)$'

class data_SIZE(MeiDataType):
    """ Relative size attribute values"""
    validation = r'^(normal|cue)$'

class data_SLUR(MeiDataType):
    """ i=initial, m=medial, t=terminal. Number is used to match
      endpoints of the slur when slurs are nested or overlap, e.g. &lt;note
      slur='i1 i2'/&gt;&lt;note slur='t1'/&gt;&lt;note
      slur='t2'/&gt; encodes the fact that two slurs begin on note 1, one
      which terminates on note 2 and one which terminates on note
      3."""
    validation = r'^((i|m|t)[1-6])$'

class data_SLURS(MeiDataType):
    """ One or more from the list given in the definition of
      data.SLUR.
      
      TODO: Make this stricter."""
    validation = r'^(.*)'

class data_SLURDIRECTION(MeiDataType):
    """ Slur direction"""
    validation = r'^(up|down)$'

class data_STAFFLOC(MeiDataType):
    """ Staff location. Staff location includes staff lines,
      spaces, and the spaces directly above and below the staff. The value
      ranges between 0 (just below the staff) to 2 * number of staff lines
      (directly above the staff). For example, on a 5-line staff the lines would
      be numbered 1,3,5,7, and 9 while the spaces would be numbered
      0,2,4,6,8,10."""
    validation = r'^([0-9]+)$(?!\.)'

class data_STEMDIRECTION(MeiDataType):
    """ Stem direction"""
    validation = r'^(up|down)$'

class data_STEMMODIFIER(MeiDataType):
    """ Stem modification"""
    validation = r'^(1slash|2slash|3slash|4slash|5slash|6slash|sprech|z)$'

class data_STEMPOSITION(MeiDataType):
    """ Which side of stem?"""
    validation = r'^(left|center|right)$'

class data_TEMPERAMENT(MeiDataType):
    """ Temperament"""
    validation = r'^(equal|just|mean|pythagorean)$'

class data_TEXTRENDITION(MeiDataType):
    """ Text rendition values"""
    validation = r'^(box|circle|dblunderline|none|quote|slash|smcaps|strike|sub|sup|underline)$'

class data_TIE(MeiDataType):
    """ Tie attribute values: initial, medial, terminal"""
    validation = r'^(i|m|t)$'

class data_TIEDIRECTION(MeiDataType):
    """ Tie Direction"""
    validation = r'^(up|down)$'

class data_TIES(MeiDataType):
    """ TODO """
    pass

class data_TUPLET(MeiDataType):
    """Tuplet attribute values: initial, medial, terminal"""
    validation = r'^(i|m|t)[1-6]$'

class data_TUPLETS(MeiDataType):
    """ TODO """
    pass

class data_UNEUMENAME(MeiDataType):
    """ Basic, i.e., single, uninterrupted, neume names"""
    valiation = re.compile(r"""^(punctum|virga|pes|clivis|torculus|
            torculusresupinus|porrectus|porrectusflexus|apostropha|
            oriscus|pressusmaior|pressusminor|virgastrata)$""", re.X)

class data_UNEUMEFORM(MeiDataType):
    """ Basic, i.e., single, uninterrupted, neume forms"""
    validation = r'^(liquescent1|liquescent2|liquescent3|quilismatic|rectangular|rhombic|tied)$'

class data_INTERLINE(MeiDataType):
    """ Distance expressed in terms of staff interline distance;
      that is, units of 1/2 the distance between adjacent
      staves."""
    validation = r'^([\d]+\.[\d]+)$'
    
    
###### PyMEI-specific datatypes. Used where a datatype is defined inline.
###### We define it here so we can refer to it easily.

class data_BEAM_REND(MeiDataType):
    """ encodes whether a beam is feathered and in which direction."""
    validation = r'^(acc|rit|norm)$'

class data_HALIGN(MeiDataType):
    """ a horizontal alignment value."""
    validation = r'^(left|right|center|justify)$'

class data_POSITIVEINTEGER(MeiDataType):
    """ a positive integer """
    validation = r'^([0-9]+)$(?!\.\-)'

class data_INTEGER(MeiDataType):
    validation = r'^([0-9]+)$(?!\.)'

class data_DECIMAL(MeiDataType):
    validation = r'^([0-9]+[\.]?([0-9]+)?)$'

class data_STAFFGROUPINGSYM(MeiDataType):
    """ a staff grouping indicator """
    validation = r'^(brace|bracket|line|none)$'

class data_CURVEDIR(MeiDataType):
    """ a curve direction"""
    validation = r'^(above|below)$'

class data_ACTUATE(MeiDataType):
    """ automatic link actuation. """
    validation = r'^(onLoad|onRequest|other|none)$'
    
class data_SHOW(MeiDataType):
    """ show something?"""
    validation = r'^(new|replace|other|none)$'

class data_METERBAR_COMPLETE(MeiDataType):
    """ a value of 'c' (complete) indicates a
      metrically complete measure, 'i' (incomplete) indicates a measure with
      not enough beats, while 'o' (overfull) is for measures with too many
      beats."""
    validation = r'^(c|i|o)$'

class data_METERRENDITION(MeiDataType):
    """ contains indication of how the meter
      signature should be rendered."""
    validation = r'^(denomsym|norm|invis)$'

class data_ACCID_FUNC(MeiDataType):
    """ records whether the accidental has an
      editorial or cautionary function."""
    validation = r'^(caution|edit)$'

class data_ACCID_PLACE(MeiDataType):
    """ captures the placement of the accidental
      relative to the staff."""
    validation = r'^(above|below|staff)$'

class data_DOT_FUNCTION(MeiDataType):
    """ records the function of a dot: augmentation or division"""
    validation = r'^(aug|div)$'

class data_SYSTEMHASH(MeiDataType):
    """ indicates whether hash marks should be
      rendered between systems. See Read, p. 436, ex.
      26-3."""
    validation = r'^(hash)$'

class data_ENDINGRENDITION(MeiDataType):
    """ describes where ending marks should be displayed."""
    validation = r'^(top|barred|grouped)$'
