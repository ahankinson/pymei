"""
These elements have a spatial representation on a page, and thus may have 
coordinates. These methods are used to work with the spatial information.
"""

class SpatialElementType(object):
    def __init__():
        pass
        
    @property
    def facs(self):
        return self.attribute_by_name('facs').value
    @facs.setter
    def facs(self, value):
        self.attributes = {'facs': value}
    
