from pymei.Import import meixml, meijson


def open(file, type="meixml"):
    """ 
        Opens a MEI file. Currently only supports meixml.
        
        Returns a MEI Document Object.
        
    """
    if type == "meixml":
        # import using the meixml library. return
        doc = _parse_from_meixml(file)
        return doc
    elif type == "meijson":
        raise MeiNotYetImplementedError("JSON Import is not yet implemented.")
        return
        

# private.
def _parse_from_meixml(file):
    pass