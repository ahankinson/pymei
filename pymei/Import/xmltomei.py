#import lxml #GVM
from lxml import etree #AH
from lxml import objectify #AH
import type

from pymei.Components import MeiDocument, MeiElement
from pymei.Components import Modules as mod


def xmltomei(meifile):
    """ Open and parse a MEI XML file to a MeiDocument object. """
    f = open(meifile, 'r')
    p = etree.XMLParser(remove_comments = True)
    t = etree.parse(f)
    r = t.getroot()
    d = _xml_to_mei(r)
    doc = MeiDocument.MeiDocument()
    return doc.addelement(d)
    
def _xml_to_mei(el):
    ns_tag = el.tag.split('}')
    tagname = ns_tag[-1] # strip the ns off the tagname.
    ns = ns_tag[0].strip('{')
    objname = "{0}_".format(tagname)
    obj = getattr(mod, objname)(namespace=ns)
    
    if el.text.strip() != '':
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
        
    if el.items():
        attrs = dict(el.items())
        obj.setattributes(attrs)
    
    c = list(el)
    if c is True:
        m = map(_xml_to_mei, c)
        obj.addchildren(m)
        
    return obj

    