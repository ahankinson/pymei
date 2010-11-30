from lxml import etree #AH
from lxml import objectify #AH
from pymei.Components.MeiExceptions import MeiNotYetImplementedError
from pymei.Components import MeiDocument, MeiElement
from pymei.Components import Modules as mod
from pymei.Helpers import attfilt as af

from music21 import metadata
from music21 import stream
from music21 import duration
from music21 import note
from music21 import meter
from music21 import key
from music21 import chord

import logging
lg = logging.getLogger('pymei')


def xmltomusic21(meifile):
    """ Open and parse a MEI XML file to a MeiDocument object. """
    f = open(meifile, 'r')
    p = etree.XMLParser(ns_clean=True, remove_comments=True, no_network=False)
    t = etree.parse(f, p)
    f.close()
    r = t.getroot()
    d = _xml_to_music21(r)

def _xml_to_music21(el):
    # for now, let's just parse a few tags
    tags_to_parse = (
        'note',
        # 'chord',
        # 'measure',
        # 'beam',
        # 'dynam',
        # 'staff'
    )
    
    ns_tag = el.tag.split('}')
    tagname = ns_tag[-1]
    ns = ns_tag[0].strip('{')
    lg.debug(tagname)
    if tagname == 'note':
        lg.debug('parsing a note')
        # first thing's first
        d = {}
        for k,v in el.items():
            # grab the pitch name
            d[af.ns_to_prefix(k)] = v
        
        lg.debug("{0}".format(d))
        p = d['pname']
        #octave
        o = d['oct']
        if 'accid.ges' in d:
            a = _convert_accidentals(d['accid.ges'])
        else:
            a = ""
        nt = "{0}{1}{2}".format(p,o,a)
        
        n = note.Note(nt)        
        notelen = int(d['dur']) # this will break if it encounters "long" or "breve!"
        n.duration = duration.Duration(notelen)
        
        lg.debug("{0}".format(dir(n)))
        
        return n
    
    # add any children.
    c = list(el)
    if len(c) > 0:
        # loopdy-loopdy! This calls itself for any children components found.
        m = map(_xml_to_music21, c)
    
    
def _convert_accidentals(accid):
    """
    Accidental attribute values: s = sharp, f = flat, ss =
      dblsharp, x=dblsharp, ff = dblflat, xs = triple sharp, tb = triple flat, n
      = natural, nf = naturalflat, ns = naturalsharp. ss indicates the use of 2
      sharp signs, while x indicates the use of a single double sharp. nf and ns
      are used to cancel dbflats and dblsharps, respectively. su = sharp note
      qtr. tone up, sd = sharp note qtr. tone down, fu = flat note qtr. tone up,
      fd = flat note qtr. tone down, nu = natural note qtr. tone up, nd =
      natural note quarter tone down.
    
    
    """
    if accid is "s":
        return "#"
    elif accid is "f":
        return "-"
    elif accid is "n":
        return "n"
    elif accid in ("ds", "x", "ss"):
        return "##"
    elif accid is "ff":
        return "--"
    elif accid is "xs":
        return "###"
    elif accid is "tb":
        return "---"
    else:
        raise MeiNotYetImplementedError("That accidental is not known!")