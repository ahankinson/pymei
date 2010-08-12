from midiutil.MidiFile import MIDIFile

class Mlts:
    """ Conversion lookup tables."""
    kacc = ['f', 'c', 'g', 'd', 'a', 'e', 'b']
    circ5 = {"0": [],
                "1s": kacc[0:1],
                "2s": kacc[0:2],
                "3s": kacc[0:3],
                "4s": kacc[0:4], 
                "5s": kacc[0:5],
                "6s": kacc[0:6],
                "7s": kacc[0:7],
                "7f": kacc[0:7],
                "6f": kacc[1:7],
                "5f": kacc[2:7],
                "4f": kacc[3:7],
                "3f": kacc[4:7],
                "2f": kacc[5:7],
                "1f": kacc[6:7]
            }
    acc = {'f': -1, 's': 1, 'ff': -2, 'ss': 2, 'n': 0}

class MidiOutput:
    """ An empty place to store the MEI data we accumulate so that we can 
        compile the MIDI file.
    """
    pass

def _dur_to_ticks(dur):
    """ Converts note durations to MIDI ticks """
    pass

def _pname_to_note(ksig, pname, octave, accidental=None):
    """ Converts a pitchname and an octave to a MIDI pitch.
        
        The key sig argument modifies the pitches appropriately. If we're in the key of F
        and the pname "b" is passed in, it is in fact a Bb.
        
        The optional accidental argument accepts the MEI notation for accidentals, namely
        f, s, ff, ss, n
        
        These will raise or lower the final pitch by the appropriate amount.
        
    """
    # the default mapping. We define a C Major scale with the appropriate numerical values.
    pnum = { 'c': 0, 'd': 2, 'e': 4, 'f': 5, 'g': 7, 'a': 9, 'b': 11 }
    
    # If the key signature has sharps or flats, modify the scale according to the Circle of 5ths.
    if pname in Mlts.circ5[ksig]:
        if ksig.endswith("f"):
            for n in Mlts.circ5[ksig]:
                pnum[n] = pnum[n] - 1
        elif ksig.endswith("s"):
            for n in Mlts.circ5[ksig]:
                pnum[n] = pnum[n] + 1
    
    midi_pitch = pnum[pname] + (int(octave) + 1) * 12
    
    if accidental is not None:
        midi_pitch = midi_pitch + Mlts.acc[accidental]
    
    return midi_pitch

def convert(meifile, typ):
    if typ == "json":
        from pymei.Import.jsontomei import jsontomei as m_in
    elif typ == "xml":
        from pymei.Import.xmltomei import xmltomei as m_in
    
    mdoc = m_in(meifile)
    
    # We'll iterate through the doc a few times to gather up the needed information
    