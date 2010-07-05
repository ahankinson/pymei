#import lxml #GVM
from lxml import etree #AH
from lxml import objectify #AH

from pymei.Components import MeiDocument, MeiElement
from pymei.Components import Modules as mod

from pymei import NS_TO_PREFIX

import logging
lg = logging.getLogger('pymei')


def xmltomei(meifile):
    """ Open and parse a MEI XML file to a MeiDocument object. """
    f = open(meifile, 'r')
    p = etree.XMLParser(ns_clean=True, remove_comments=True)
    t = etree.parse(f, p)
    r = t.getroot()
    d = _xml_to_mei(r)
    doc = MeiDocument.MeiDocument()
    doc.addelement(d)
    lg.debug(doc)
    return doc
    
def _xml_to_mei(el):
    """ Helper function for converting etree-parsed XML objects to a nested set of
        MeiElements.
    """
    
    # etree automatically appends the namespace to every element. We need to 
    # strip that off.
    ns_tag = el.tag.split('}')
    tagname = ns_tag[-1]
    ns = ns_tag[0].strip('{')
    
    # create the object name.
    objname = "{0}_".format(tagname)
    obj = getattr(mod, objname)(namespace=ns)
    
    if el.text and el.text.strip() != '':
        # if we strip the blanklines and line endings and do not end up with an
        # empty string, we have inline text that we need to deal with.
        # For now, we will strip out *any* child tags to set the text value. We'll 
        # still store them as children tags elements, but they will be taken 
        # out of context. It's the best we can do for now.
        tx = ""
        for n in el.itertext():
            tx += " ".join(n.split())
            tx += " "
        obj.setvalue(tx)
        
    # set the attributes
    if el.items():
        attrs = dict(el.items())
        obj.setattributes(attrs)
    
    # add any children.
    c = list(el)
    if len(c) > 0:
        # loopdy-loopdy!
        m = map(_xml_to_mei, c)
        obj.addchildren(m)
        
    return obj

    