from lxml import etree
from lxml import objectify

from pymei.Components import MeiDocument, MeiElement
from pymei.Components import Modules as mod


def import_meixml(file):
    """ Open and parse a MEI XML file to a MeiDocument object. """
    mxml = objectify.parse
    