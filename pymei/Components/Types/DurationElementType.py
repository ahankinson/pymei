"""
    All elements that have a duration should inherit from this class.
"""
class DurationElementType(object):
    def __init__():
        self.__duration = None
        self.__is_dotted = False
        self.__dots = None
    
    @property
    def duration(self):
        self._duration()
        return self.__duration
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
        return self.__is_dotted

    @property
    def dots(self):
        self._duration()
        return self.__dots
    @dots.setter
    def dots(self, value):
        self.attributes = {'dots': value}
        self._duration()
        
    # protected
    def _duration(self):
        dur = self.attribute_by_name("dur")
        if dur:
            self.__duration = dur.value
        else:
            self.__duration = None
            self.remove_attribute('dur')
        # a dot can affect the duration. We won't compute the absolute duration,
        # but rather we'll just set a flag that this note is dotted.
        self._is_dotted()

    def _is_dotted(self):
        if self.has_attribute('dots') and self.attribute_by_name('dots').value is not '0':
            self.__is_dotted = True
            self.__dots = self.attribute_by_name('dots').value
        else:
            self.__is_dotted = False
            self.__dots = None
            self.remove_attribute('dots')

