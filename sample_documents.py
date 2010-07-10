import os
import sys
from optparse import OptionParser

from pymei.Import import xmltomei

import logging
lg = logging.getLogger('pymei')

if __name__ == "__main__":
    usage = "usage: %prog [options] path_to_documents"
    desc = """ This test script runs against the sample MEI documents in a folder
            and determines whether it can parse them or not. Used to make sure
            our script is able to handle "real-world" MEI."""
    p = OptionParser(usage=usage, description=desc, version="%prog 0.1a")
    p.add_option("-f", "--folder", action="store", help="Path to folder containing the sample documents")
    p.add_option("-s", "--stop", action="store_true", help="Stop on errors.")
    (options, args) = p.parse_args()
    
    for f in os.listdir(options.folder):
        
        if os.path.isdir(os.path.join(options.folder, f)):
            continue
        if os.path.splitext(f)[-1] != ".mei":
            continue
        
        try:
            x = xmltomei.xmltomei(os.path.join(options.folder, f))
            del x
        except Exception, e:
            lg.debug("*** OH NOES! Failz. ***")
            lg.debug("The filename was: {0}".format(f))
            lg.debug("The error was {0}: {1}".format(Exception, e))
            lg.debug("(((((((((((((((())))))))))))))))")
            if options.stop:
                lg.debug("Stopping!")
                sys.exit()
            else:
                continue
        
            
    