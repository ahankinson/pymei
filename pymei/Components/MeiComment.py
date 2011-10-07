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