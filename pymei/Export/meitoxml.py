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
    a = {}
    el_attb = el.getattributes()
    for it in el_attb:
        filtname = af.prefix_to_ns(it.getname())
        if filtname is "namespace":
            # @TODO: check if 'namespace' is the default document namespace; if not, 
            #   allow it to pass, otherwise, strip it out.
            #
            # Without this, it will append the namespace to every single freakin'
            # element that is output. This should be more intelligently omitted
            # so that the namespaces that are not the default namespace is
            # maintained, but for now we'll keep this as is.
            continue
        a[str(filtname)] = str(it.getvalue())
    
    el_name = el.getname()
    el_value = el.getvalue()
    el_tail = el.gettail()    
    el_x = etree.Element(el_name, **a)
    
    if el_value is not None:
        el_x.text = el_value
    
    if el_tail is not None:
        el_x.tail = el_tail
    
    if len(el.getchildren()) > 0:
        children = map(_mei_to_xml, el.getchildren())
        
        for child in children:
            el_x.append(child)
            
    return el_x
    