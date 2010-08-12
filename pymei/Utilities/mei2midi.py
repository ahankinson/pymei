from pymei.Export import meitomidi

from optparse import OptionParser

if __name__ == "__main__":
    usage = "usage: %prog [options]"
    desc = """ This file takes an MEI file and converts it to MIDI output."""
    p.add_option("-i", "--input", action="store", help="The Input file. Default is XML; use the -j switch to specify JSON")
    p.add_option("-o", "--output", action="store", help="The output filename")
    p.add_option("-j", "--json", action="store_true", help="specify JSON as the input type.")
    (options, args) = p.parse_args()
    
    # create a new MIDI file output class.
    
    
    
    