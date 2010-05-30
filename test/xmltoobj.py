
def xml_to_obj(el):
    ns_tag = el.tag.split('}')
    tagname = ns_tag[-1] # strip the ns off the tagname.
    print(tagname)
    ns = ns_tag[0].strip('{')
    
    objname = "{0}_".format(tagname)
    obj = getattr(mod, objname)(namespace=ns)
    
    if el.getparent():
        obj.setparent(el.getparent())
    
    if el.items():
        attrs = dict(el.items())
        obj.setattributes(attrs)
        
    if el.text:
        # tag with text
        obj.setvalue(el.text)
    else:
        # tag with children
        children = el.getchildren()
        for
            map(xml_to_obj, children)
    return obj
    
def convert_to_obj(el):
    o = MeiElement()
    if el.items():
        attrs = dict(el.items())
        o.setattributes(attrs)
    
    if el.getchildren():
        children = el.getchildren()
        for c in children:
            o.addchild(c, parent=o)
    
    return o
    
    



def xml_to_mei(el):
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












