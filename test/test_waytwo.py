import unittest
import waytwo


class TestLoginModuleCheck(unittest.TestCase):
    "WayTwo Package"
    def test_version(self):
        "it should have a version defined"
        self.assertIsNotNone(waytwo.__version__)
