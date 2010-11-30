""" Generic converter. """
import os
from pymei.Import import xmltomei, jsontomei
from pymei.Components.MeiExceptions import MeiNotYetImplementedError

import logging
lg = logging.getLogger('pymei')

def convert(filename):
    name,extension = os.path.splitext(filename)
    lg.debug("Extension: {0}".format(extension))
    if extension in ('.xml', '.mei'):
        return xmltomei.xmltomei(filename)
    elif extension in ('.json', '.meij'):
        return jsontomei.jsontomei(filename)
    else:
        raise MeiNotYetImplementedError("Support for that file type is not yet implemented.")
        return None