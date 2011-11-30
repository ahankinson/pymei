import json
import types
import codecs

import logging
lg = logging.getLogger('pymei')

def meitojson(meidocument, filename=None, prettyprint=True):
    r = meidocument.root
    d = _mei_to_json(r)

    if prettyprint:
        j = json.dumps(d, sort_keys=True, indent=2)
    else:
        j = json.dumps(d)
        
    if not isinstance(filename, types.NoneType):
        f = codecs.open(filename, 'w', encoding='utf-8')
        f.write(j)
        f.close()
        return None
    else:
        return j

def _mei_to_json(el):
    # at this point we're still working on a python dictionary.
    el_j = el.as_dictionary()
    if len(el.children) > 0:
        c = map(_mei_to_json, el.children)
        for child in c:
            el_j[el.name].append(child)
    return el_j
    
    
    