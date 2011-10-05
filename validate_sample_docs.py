import os
import sys
from optparse import OptionParser

# from pymei.Import import xmltomei
from lxml import etree

import logging
lg = logging.getLogger('pymei')

if __name__ == "__main__":
    usage = "usage: %prog [options] path_to_rng path_to_documents"
    desc = """ This test script runs against the sample MEI documents in a folder
            and determines whether it can parse them or not. Used to make sure
            our script is able to handle "real-world" MEI."""
    p = OptionParser(usage=usage, description=desc, version="%prog 0.1a")
    # p.add_option("-f", "--folder", action="store", help="Path to folder containing the sample documents")
    p.add_option("-s", "--stop", action="store_true", help="Stop on errors.")
    (options, args) = p.parse_args()
    
    print "Starting parsing..."
    
    f = open(args[0], 'r')
    rdoc = etree.parse(f)
    relaxng = etree.RelaxNG(rdoc)
    
    lg.debug("Walking through the directories.")
    for dp,dn,fn in os.walk(args[1]):
        if dp.startswith("."):
            print 'Skipping {0}'.format(dp)
            continue
        for f in fn:
            print "Processing {0}".format(f)
            if os.path.splitext(f)[-1] != ".mei":
                continue
            try:
                fdoc = open(os.path.join(dp, f), 'r')
                doc = etree.parse(fdoc)
                valid = relaxng.assertValid(doc)
                
                print "{0}: {1}".format(f, valid)
                
            except Exception, e:
                print "********************************************"
                print "*** Failure on {0} ***".format(f)
                print "The error was: {0}".format(e)
                print "********************************************"
                if options.stop:
                    print "Stopping!"
                    sys.exit()
                else:
                    continue
        
            
    