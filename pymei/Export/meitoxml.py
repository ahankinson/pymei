# helper functions to output to various representations.
from lxml import etree

from pymei import MEI_NS
from pymei.Helpers import attfilt as af

import logging
lg = logging.getLogger('pymei')



def meitoxml(meidocument, filename):
    """ Write out an MeiDocument object to a file."""
    r = meidocument.gettoplevel()
    d = _mei_to_xml(r)
    d.set('xmlns', MEI_NS)
    t = etree.ElementTree(d)
    t.write(filename, 
            pretty_print=True, 
            xml_declaration=True,
            encoding=meidocument.getencoding(),
            standalone=meidocument.getstandalone())


def _mei_to_xml(el):
    lg.debug('el {0}'.format(el))
    a = {}
    el_attb = el.getattributes()
    for it in el_attb:
        filtname = af.prefix_to_ns(it.getname())
        if filtname is "namespace":
            continue
        a[filtname] = it.getvalue()
    
    el_name = el.getname()
    el_value = el.getvalue()
    
    el_x = etree.Element(el_name, **a)
    if el_value is not None:
        el_x.text = el_value
    
    if len(el.getchildren()) > 0:
        children = map(_mei_to_xml, el.getchildren())
        
        lg.debug('children {0}'.format(children))
        for child in children:
            el_x.append(child)
            
    return el_x
    