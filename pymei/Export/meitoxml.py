# helper functions to output to various representations.
from lxml import etree



def meitoxml(meidocument, filename):
    """ Write out an MeiDocument object to a file."""
    r = meidocument.gettoplevel()
    d = _mei_to_xml(r)


def _mei_to_xml(el):
    a = {}
    el_attb = el.getattributes()
    for it in el_attb:
        a[it.getname()] = it.getvalue()
    
    el_name = el.getname()
    el_valu = el.getvalue()
    
    el_x = etree.Element(el_name, **a)
    if el_value is True:
        el_x.text = el_value
    
    if len(el.getchildren()) > 0:
        children = map(_mei_to_xml, el.getchildren())
        for child in children:
            ca = {}
            ch_att = child.getattributes()
            for cit in ch_att:
                ca[cit.getname()] = cit.getvalue()
                
            el_x.append(etree.Element(child.getname(), **ca))
            if child.getvalue() is True:
                child.text = child.getvalue()
    
    return el_x
    