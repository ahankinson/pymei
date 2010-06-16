#import lxml #GVM
from lxml import etree #AH
from lxml import objectify #AH

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
    if el.items():
        attrs = dict(el.items())
        obj.setattributes(attrs)
        
    c = list(el)
    if c is True:
        m = map(_xml_to_mei, c)
        obj.addchildren(m)
    else:
        obj.setvalue(el.text)
    return obj

    