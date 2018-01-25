import unittest
from waytwo import base

class TestBase(unittest.TestCase):
  "WayTwo Base"
  def setUp(self):
      self.username = '1234567890'
      self.password = 'password'
      self.waytwo = base.WayTwo(self.username, self.password)

  def test_init(self):
    "should accept only username and password"
    self.assertRaises(TypeError, base.WayTwo, self.username)
    self.assertRaises(TypeError, base.WayTwo, self.password)
    self.assertTrue(isinstance(self.waytwo, base.WayTwo))
