def flatten(mei_obj):
    """ 
        Flattens the nested descendent elements into a single list.
        Caches the result in the object for future lookups.
    """
    def __fl(ls):            
        for ch in ls.getchildren():
            if len(ch.getchildren()) > 0:
                for cd in __fl(ch):
                    yield cd
            yield ch
    return list(__fl(mei_obj))