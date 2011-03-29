"""
This is a temporary class for the purposes of adding layout information to
an MEI file.

Assuming a structure like this:

<graphic>
    <zone xml:id="098" ulx=1, uly=2, lrx=3, lry=4 />
</graphic>

<mdiv>
    <score>
        <pb xml:id="789" />
        <staff n=1>
            <layer>
                <sb xml:id="" /> # for everything until the next system break.
                <note>
                <note>
                <note>
                <sb xml:id="" />
                <note>
                <note>
            </layer>
        </staff>
    </score>
</mdiv>

<layout>
    <page corresp="789">
        <system corresp="123 456" facs="098" />
    </page>
</layout>



"""
from pymei.Components.MeiElement import MeiElement
from pymei.Components.MeiAttribute import MeiAttribute

class layout_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"layout", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class page_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"page", value=value, parent=parent)
        if attrs:
            self.attributes = attrs

class staff_(MeiElement):
    def __init__(self, value=None, parent=None, **attrs):
        MeiElement.__init__(self, name=u"staff", value=value, parent=parent)
        if attrs:
            self.attributes = attrs
