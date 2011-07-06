from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute

class meiCorpus_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"meiCorpus", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

