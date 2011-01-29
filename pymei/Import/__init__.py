""" Generic converter. """
import os
from pymei.Import import xmltomei, jsontomei
from pymei.Components.MeiExceptions import MeiNotYetImplementedError

import logging
lg = logging.getLogger('pymei')

def convert(filename):
    name,extension = os.path.splitext(filename)
    if extension in ('.xml', '.mei'):
        return xmltomei.xmltomei(filename)
    elif extension in ('.json', '.meij'):
        return jsontomei.jsontomei(filename)
    else:
        raise MeiNotYetImplementedError("Support for that file type is not yet implemented.")
        return None

def parse_mei(string):
    """ Takes a structured string and returns a parsed MeiDocument """
    if string.startswith("{"):
        return jsontomei.jsonstringtomei(string)
    elif string.startswith("<"):
        raise MeiNotYetImplementedError("Haven't gotten around to this yet...")
    else:
        raise MeiNotYetImplementedError("Unknown data format.")
        return None
    