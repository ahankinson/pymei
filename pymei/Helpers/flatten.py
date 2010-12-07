def flatten(object):
    """ 
        Flattens the child elements into a single list.
    """
    def __fl(ls):            
        for ch in ls.children:
            if len(ch.children) > 0:
                for cd in __fl(ch):
                    yield cd
            yield ch
            
    return list(__fl(object))
