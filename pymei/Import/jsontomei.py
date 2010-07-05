from lxml import etree #AH
from lxml import objectify #AH
# import lxml #GVM

from pymei.Components import MeiAttribute, MeiElement, MeiDocument
from pymei.Components import Modules as mod

import types
import logging

lg = logging.getLogger('pymei')

def jsontomei(js, docname):
    """ Takes an incoming JSON stream and returns a MeiDocument object.
        
        Requires that you pass it a name.
    """
    doc = MeiDocument.MeiDocument('jsonstream')
    j = _json_to_mei(js)
    doc.addelement(j)

def _json_to_mei(el):
    """ Takes a JSON-structured MEI file and converts it to a set of nested Python
        MEI objects.
        
        See test/meijson.py for an example of how JSON-structured MEI looks.
    """
    
    # Strings are interpreted as values.
    if type(el) is types.StringType:
        return el
    
    # attributes have a special attribute dictionary key.
    if type(el) is types.DictType and "@attributes" in el.keys():
        return el
    
    # don't pop from an empty dict!
    if len(el.keys()) < 1:
        return
    
    # convert the dict key name to an MEI object name.
    tagname = el.keys().pop()
    objname = "{0}_".format(tagname)
    obj = getattr(mod, objname)()
    
    # map this on to the object
    if type(el[tagname]) is types.ListType:
        
        # loopdy-loopdy!
        m = map(_json_to_mei, el[tagname])
        
        # our map operation will return a number of things. Depending on what 
        # is in our map result, we put that it the MeiElement object accordingly.
        for d in m:
            if type(d) is types.DictType and "@attributes" in d.keys():
                obj.setattributes(dict(d['@attributes']))
            elif type(d) is types.StringType:
                obj.setvalue(d)
            else:
                obj.addchildren([d])
    return obj