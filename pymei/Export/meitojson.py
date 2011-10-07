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
    else:
        print(j)

def _mei_to_json(el):
    # at this point we're still working on a python dictionary.
    el_j = __todictionary(el)
    if len(el.children) > 0:
        c = [_mei_to_json(j) for j in el.children]
        for child in c:
            el_j[el.name].append(child)
    return el_j

def todictionary(meielement):
    return __todict(meielement)

def tojson(meielement):
    return json.dumps(__todict(meielement))

def __todict(meielement):
    d = {meielement.name:[]}
    if meielement.attributes is not None:
        el_attb = {"@a": {}}
        for at in meielement.attributes:
            if at.name is "namespace":
                continue
            el_attb["@a"][at.name] = at.value
        if el_attb["@a"].values():
            d[meielement.name].append(el_attb)
    if meielement.value is not None:
        if meielement.value.strip() != "":
            d[meielement.name].append({"@v": meielement.value})
    if meielement.tail is not None:
        if meielement.tail.strip() != "":
            d[meielement.name].append({"@t": meielement.tail})
    return d
