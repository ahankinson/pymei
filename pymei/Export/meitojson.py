import json
import types

import logging
lg = logging.getLogger('pymei')

def meitojson(meidocument, filename=None, prettyprint=True):
    r = meidocument.gettoplevel()
    d = _mei_to_json(r)

    if prettyprint is True:
        j = json.dumps(d, sort_keys=True, indent=2)
    else:
        j = json.dumps(d)
        
    if not isinstance(filename, types.NoneType):
        f = open(filename, 'w')
        f.write(j)
        f.close()
    else:
        print(j)

def _mei_to_json(el):
    el_name = el.getname()
    el_j = {el_name: []}

    if el.getattributes() is not None:
        attb = el.getattributes()
        el_attb = {"@attributes": {}}
        for it in attb:
            if it.getname() is "namespace":
                continue
            el_attb['@attributes'][it.getname()] = it.getvalue()
        
        # add a little check here. We don't want to add it if our attributes are empty.
        if el_attb['@attributes'].values():
            el_j[el_name].append(el_attb)
    
    if el.getvalue() is not None:
        if el.getvalue().strip() != "":
            el_j[el_name].append({"@value": el.getvalue()})
    if el.gettail() is not None:
        if el.gettail().strip() != "":
            el_j[el_name].append({"@tail": el.gettail()})
    
    if len(el.getchildren()) > 0:
        children = map(_mei_to_json, el.getchildren())
        for child in children:
            el_j[el_name].append(child)
    
    return el_j
    
    
    