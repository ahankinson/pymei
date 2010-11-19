import os
import sys
from optparse import OptionParser
from lxml import etree

import pymei.Components.Modules as mod


if __name__ == "__main__":
    usage = "usage: %prog -f path_to_rng_modules"
    desc = """ This test script runs against the defined RelaxNG modules and verifies that 
                a defined python class exists for each element defined in the modules."""
    p = OptionParser(usage=usage, description=desc, version="%prog 0.1a")
    p.add_option("-f", "--folder", action="store", help="Path to folder containing the modules")
    (options, args) = p.parse_args()
    
    difference = []
    problems = False
    # get python modules
    p = filter(lambda x: x.endswith("_") and not x.endswith("__"), dir(mod))
    v = set(map(lambda x: x.rstrip("_"), p))
    
    # get XML module files
    m = [r for r in os.listdir(options.folder) if os.path.splitext(r)[-1] == ".rng" and r != "mei-all.rng"]
    for fl in m:
        print "Processing {0}".format(fl)
        f = open(os.path.join(options.folder, fl), 'r')
        t = etree.parse(f)
        f.close()
        els = set([dict(e.items()).values()[0] for e in t.xpath("/r:grammar//r:element", namespaces={'r':'http://relaxng.org/ns/structure/1.0'})])
        if not els.issubset(v):
            problems = True
            print "In file {0}: ".format(fl)
            print "\t we found these elements that were not common to the schema and the python library: {0}".format(list(els.difference(v)))
    if not problems:
        print "No problems were found. The Python library and the RelaxNG schema are in sync."
    else:
        print "\nProblems were found. Please correct them and try again."
        