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
    el_x = toxmlobj(el)
    if isinstance(el, MeiComment.MeiComment):
        return el_x
        
    if len(el.children) > 0:
        children = [_mei_to_xml(c) for c in el.children]
        
        for child in children:
            el_x.append(child)
    return el_x

def __toxml(meielement):
    a = {}
    for at in meielement.attributes:
        filtname = prefix_to_ns(at.name)
        if filtname == "namespace":
            continue
        a[str(filtname)] = at.value
    el = etree.Element(meielement.name, **a)
    if meielement.value is not None:
        el.text = meielement.value
    if meielement.tail is not None:
        el.tail = meielement.tail
    return el

def toxmlobj(meielement):
    return __toxml(meielement)

def toxmlstr(meielement):
    obj = __toxml(meielement)
    return etree.tostring(obj, pretty_print=True)

    