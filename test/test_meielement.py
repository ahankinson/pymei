import unittest
import os
import shutil
from pymei.Components.MeiElement import MeiElement

class MeiElementTest(unittest.TestCase):
    
    def setUp(self):
        print "Setting up MEI Document Test"

    def tearDown(self):
        pass

    def test_create_element(self):
        m = MeiElement("note")
        self.assertEquals(m.name, "note")
    
    def test_generate_id(self):
        m = MeiElement("note")
        self.assertTrue(m.id)

