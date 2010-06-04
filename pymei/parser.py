from pymei.Import.xmltomei import xmltomei
from pymei.Import.jsontomei import jsontomei

from pymei.exceptions import MeiXMLParsingError

def load(meifile, parse="meixml"):
    """ 
        Opens a MEI file. Currently only supports meixml.
        
        Returns a MEI Document Object.
        
    """
    if parse == "meixml":
        # import using the meixml library. return
        try:
            meidoc = xmltomei(meifile)
            return meidoc
        except Exception, e:
            raise MeiXMLParsingError("Problem parsing the MEIXML file: {0}".format(e))
            return
    elif parse == "meijson":
        raise MeiNotYetImplementedError("JSON Import is not yet implemented.")
        return