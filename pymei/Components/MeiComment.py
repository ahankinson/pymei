# ================================================================
#   MeiComment.py
#
#   An abstract class representing an MEI comment.
#
#   Author:     Andrew Hankinson
#   License:    MIT
#
# ================================================================
from lxml import etree


class MeiComment(object):
    def __init__(self, comment=None):
        self.__comment = comment
    
    def as_xml_object(self):
        self._xml()
        return self.__xml_obj
            
    def as_xml_string(self):
        self._xml()
        return self.__xml_str
    
    def _xml(self):
        el = etree.Comment(self.__comment)
        self.__xml_obj = el
        self.__xml_str = etree.tostring(el)
        