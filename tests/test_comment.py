from datetime import date
import unittest
from app.models import Comment


class CommentModelTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Comment class
    '''

    def setUp(self):
        self.new_comment = Comment(id = 1, date_created = date.today() , content = 'My test comment')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))