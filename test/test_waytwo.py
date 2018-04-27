import unittest

import mock

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


class TetLogin(unittest.TestCase):
    "WayTwo Login"

    def setUp(self):
        self.username = '1234567890'
        self.password = 'password'
        self.mocked_browser = mock.patch(
            'waytwo.mechanize.Browser', autospec=True).start()
        self.addCleanup(mock.patch.stopall)

    def test_browser_should_mask_as_user(self):
        mocked_browser = self.mocked_browser.return_value
        waytwo.WayTwo(self.username, self.password)
        mocked_browser.assert_called_once
        mocked_browser.set_cookiejar.assert_called_once
        mocked_browser.set_handle_equiv.assert_called_once
        mocked_browser.set_handle_redirect.assert_called_once
        mocked_browser.set_handle_referer.assert_called_once
        mocked_browser.set_handle_robots.assert_called_once
        mocked_browser.set_handle_refresh.assert_called_once
        self.assertEqual(mocked_browser.addheaders, [(
            'User-agent',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1)'
            + ' Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1'
            )])
