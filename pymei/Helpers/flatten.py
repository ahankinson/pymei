def flatten(object):
    """ 
        Flattens the child elements into a single list.
    """
    def __fl(ls):            
        for ch in ls.getchildren():
            if len(ch.getchildren()) > 0:
                for cd in __fl(ch):
                    yield cd
            yield ch
            
    return list(__fl(object))
