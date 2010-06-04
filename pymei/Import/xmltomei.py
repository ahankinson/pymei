from lxml import etree
from lxml import objectify

from pymei.Components import MeiDocument, MeiElement
from pymei.Components import Modules as mod


def xmltomei(meifile):
    """ Open and parse a MEI XML file to a MeiDocument object. """
    f = open(meifile, 'r')
    t = etree.parse(f)
    r = t.getroot()
    d = _xml_to_mei(r)
    doc = MeiDocument()
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

    if el.text:
        obj.setvalue(el.text)
    elif el.getchildren():
        c = el.getchildren()
        m = map(xml_to_mei, c)
        obj.addchildren(m)
    return obj

    