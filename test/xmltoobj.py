
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
        if children:
            map(xml_to_obj, children)
    return obj