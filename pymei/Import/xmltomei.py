import time
#import lxml #GVM
from lxml import etree #AH
#from lxml import objectify #AH
import uuid
import codecs

from pymei.Components import MeiDocument, MeiElement, MeiComment
from pymei.Components import Modules as mod
from pymei.Helpers import ns_to_prefix, generate_mei_id

#from pymei import NS_TO_PREFIX

import logging
lg = logging.getLogger('pymei')


def xmltomei(meifile):
    """ Open and parse a MEI XML file to a MeiDocument object. """
    f = codecs.open(meifile, 'r', encoding='utf-8')
    p = etree.XMLParser(ns_clean=True, no_network=False, encoding="utf-8")
    t = etree.parse(f, p)
    f.close()
    
    t.xinclude() # run xinclude
    r = t.getroot()
    d = _xml_to_mei(r)
    doc = MeiDocument.MeiDocument()
    doc.root = d
    return doc

def _xml_to_mei(el):
    """ Helper function for converting etree-parsed XML objects to a nested 
        set of MeiElements.
    """
    
    # etree automatically appends the namespace to every element. We need to 
    # strip that off.
    if isinstance(el, etree._Comment):
        obj = MeiComment.MeiComment(el.text)
        return obj
    
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
        obj.svalue = tx
    
    if el.text is not None:
        obj.value = el.text
    
    if el.tail is not None:
        obj.tail = el.tail
    
    # set the attributes
    d = {}
    if el.items():
        for k,v in el.items():
            # if the attribute has a namespace, be sure to convert it to its
            # prefix
            d[ns_to_prefix(k)] = v        
    
    # importing should *always* implement something like this.
    # This preserves existing XML:IDs, but also supplies them if they do not exist.
    # We set them as an attribute to support their existence as an XML attribute, but
    # the MeiElement catches this and also sets it to that item's ID.
    if "xml:id" not in d.keys():
        d['xml:id'] = generate_mei_id()
        
    obj.attributes = d
    
    # add any children.
    c = list(el)
    if len(c) > 0:
        # lg.debug("Adding children: {0}".format(tagname))
        # loopdy-loopdy! This calls itself for any children components found.
        m = map(_xml_to_mei, c)
        #lg.debug('Object: {0}; children {1}'.format(obj, m))
        obj.add_children(m)
        
    return obj

    