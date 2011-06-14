"""
    All elements that have a duration should inherit from this class.
"""
class DurationElementType(object):
    duration_attr = None
    is_dotted_attr = None
    dots_attr = None
    
    def __init__():
        # raise a warning if this is inited directly.
        pass
        
    @property
    def duration(self):
        self._duration()
        return self.duration_attr
    @duration.setter
    def duration(self, value):
        self.attributes = {'dur': value}
        self._duration()

    @property
    def is_dotted(self):
        """ Returns True if dotted; False if not"""
        # the existence of dots is computed when we check the duration. 
        # therefore, if there is no duration, we may also have not checked
        # for dots yet. We'll double check now.
        self._duration()
        return self.is_dotted_attr

    @property
    def dots(self):
        self._duration()
        return self.dots_attr
    @dots.setter
    def dots(self, value):
        self.attributes = {'dots': value}
        self._duration()
        
    # protected
    def _duration(self):
        dur = self.attribute_by_name("dur")
        if dur:
            self.duration_attr = dur.value
        else:
            self.duration_attr = None
            self.remove_attribute('dur')
        # a dot can affect the duration. We won't compute the absolute duration,
        # but rather we'll just set a flag that this note is dotted.
        self._is_dotted()

    def _is_dotted(self):
        if self.has_attribute('dots') and self.attribute_by_name('dots').value is not '0':
            self.is_dotted_attr = True
            self.dots_ = self.attribute_by_name('dots').value
        else:
            self.is_dotted_attr = False
            self.dots_attr = None
            self.remove_attribute('dots')

