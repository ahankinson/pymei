from pymei.Export import meitomidi
from midiutil.MidiFile import MIDIFile

from optparse import OptionParser

class Mlts:
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
    # the default mapping
    pnum = { 'c': 0, 'd': 2, 'e': 4, 'f': 5, 'g': 7, 'a': 9, 'b': 11 }
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


if __name__ == "__main__":
    usage = "usage: %prog [options]"
    desc = """ This file takes an MEI file and converts it to MIDI output."""
    p.add_option("-i", "--input", action="store", help="The Input file. Default is XML; use the -j switch to specify JSON")
    p.add_option("-o", "--output", action="store", help="The output filename")
    p.add_option("-j", "--json", action="store_true", help="specify JSON as the input type.")
    (options, args) = p.parse_args()
    
    
    