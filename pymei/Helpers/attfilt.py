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