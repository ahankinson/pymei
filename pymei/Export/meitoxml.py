# helper functions to output to XML
from lxml import etree
from pymei import MEI_NS, XLINK_NS, MEI_VERSION
from pymei.Helpers import prefix_to_ns
from pymei.Components import MeiComment

import logging
lg = logging.getLogger('pymei')

def meitoxml(meidocument, filename=None):
    """ Prints XML to the screen, or writes out an MeiDocument object to a file."""
    r = meidocument.root
    d = _mei_to_xml(r)
    
    d.set('xmlns', MEI_NS)
    d.set('meiversion', MEI_VERSION)
    # d.set('xlink', XLINK_NS)
    
    t = etree.ElementTree(d)
    
    if filename:
        t.write(filename, 
                pretty_print=True, 
                xml_declaration=True,
                encoding=meidocument.encoding,
                standalone=meidocument.standalone)
    else:
        print(etree.tostring(t, 
                pretty_print=True,
                xml_declaration=True,
                encoding=meidocument.encoding,
                standalone=meidocument.standalone))

def _mei_to_xml(el):
    el_x = el.as_xml_object()
    if isinstance(el, MeiComment.MeiComment):
        return el_x
        
    if len(el.children) > 0:
        children = map(_mei_to_xml, el.children)
        
        for child in children:
            el_x.append(child)
    return el_x
    