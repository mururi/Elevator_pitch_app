from datetime import date
import unittest
from app.models import Pitch


class PitchModelTest(unittest.TestCase):
    '''
    Test class to test the behaviour og the Pitch class
    '''

    def setUp(self):
        self.new_pitch = Pitch(id = 1, category = 'business', date_created = date.today() , content = 'My awesome pitch', upvotes = 100, downvotes = 0)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))