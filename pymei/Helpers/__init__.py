from pymei import NS_TO_PREFIX, PREFIX_TO_NS

def ns_to_prefix(att):
    """ Helper function to convert a full namespace into its prefix."""
    if att.startswith("{"):
        full = att.split("}")
        a = full[-1]
        n = NS_TO_PREFIX[full[0].strip("{")]
        return "{0}:{1}".format(n,a)
    else:
        return att

def prefix_to_ns(att):
    if len(att.split(":")) > 1:
        p = PREFIX_TO_NS[att.split(":")[0]]
        a = "{{{0}}}{1}".format(p, att.split(":")[-1])
        return str(a)
    else:
        return str(att)

def flatten(mei_obj):
    """ 
        Flattens the nested descendent elements into a single list.
    """
    def __fl(ls):            
        for ch in ls.getchildren():
            if len(ch.getchildren()) > 0:
                for cd in __fl(ch):
                    yield cd
            yield ch
    return tuple(__fl(mei_obj))