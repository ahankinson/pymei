from pymei.Import.meixml import meixml_import
from pymei.Import.meijson import meijson_import
from pymei.Components.MeiDocument import MeiDocument

from pymei.exceptions import MeiXMLParsingError

def load(meifile, parse="meixml"):
    """ 
        Opens a MEI file. Currently only supports meixml.
        
        Returns a MEI Document Object.
        
    """
    if parse == "meixml":
        # import using the meixml library. return
        try:
            meiobj = meixml_import(meifile)
            doc = MeiDocument()
            doc.addelement(meiobj)
            return doc
        except Exception, e:
            raise MeiXMLParsingError("Problem parsing the MEIXML file: {0}".format(e))
            return
    elif parse == "meijson":
        raise MeiNotYetImplementedError("JSON Import is not yet implemented.")
        return