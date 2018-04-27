import unittest
import waytwo


class TestWayTwoVersionCheck(unittest.TestCase):
    "WayTwo Package"
    def test_version(self):
        "it should have a version defined"
        self.assertIsNotNone(waytwo.__version__)


class TestWayTwoInitalisation(unittest.TestCase):
    "WayTwo Initalisation"

    def setUp(self):
        self.username = '1234567890'
        self.password = 'password'
        self.waytwo = waytwo.WayTwo(self.username, self.password)

    def test_init(self):
        "should accept only username and password when initialising"
        self.assertRaises(TypeError, waytwo.WayTwo, self.username)
        self.assertRaises(TypeError, waytwo.WayTwo, self.password)
        self.assertTrue(isinstance(self.waytwo, waytwo.WayTwo))
