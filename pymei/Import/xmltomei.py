#import lxml #GVM
from lxml import etree #AH
from lxml import objectify #AH
import uuid


from pymei.Components import MeiDocument, MeiElement
from pymei.Components import Modules as mod
from pymei.Helpers import attfilt as af

#from pymei import NS_TO_PREFIX

import logging
lg = logging.getLogger('pymei')


def xmltomei(meifile):
    """ Open and parse a MEI XML file to a MeiDocument object. """
    f = open(meifile, 'r')
    p = etree.XMLParser(ns_clean=True, remove_comments=True, no_network=False)
    t = etree.parse(f, p)
    f.close()
    r = t.getroot()
    d = _xml_to_mei(r)
    doc = MeiDocument.MeiDocument()
    doc.addelement(d)
    return doc
    
def _xml_to_mei(el):
    """ Helper function for converting etree-parsed XML objects to a nested 
        set of MeiElements.
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
        tx = ""
        for n in el.itertext():
            tx += " ".join(n.split())
            tx += " "
        obj.setsvalue(tx)
    
    if el.text is not None:
        obj.setvalue(el.text)
    
    if el.tail is not None:
        obj.settail(el.tail)
    
    # set the attributes
    d = {}
    if el.items():
        for k,v in el.items():
            # if the attribute has a namespace, be sure to convert it to its
            # prefix
            d[af.ns_to_prefix(k)] = v        
    
    # importing should *always* implement something like this.
    # This preserves existing XML:IDs, but also supplies them if they do not exist.
    # We set them as an attribute to support their existence as an XML attribute, but
    # the MeiElement catches this and also sets it to that item's ID.
    if "xml:id" not in d.keys():
        d['xml:id'] = str(uuid.uuid4())
        
    obj.setattributes(d)
    
    # add any children.
    c = list(el)
    if len(c) > 0:
        # loopdy-loopdy! This calls itself for any children components found.
        m = map(_xml_to_mei, c)
        #lg.debug('Object: {0}; children {1}'.format(obj, m))
        obj.addchildren(m, obj)
        
    return obj

    