__version__ = '0.0.1'
__all__ = ['WayTwo']

import mechanize
import cookielib


class WayTwo(object):
    def __init__(self, username, password):
        self._browser = mechanize.Browser()
        cookie_jar = cookielib.LWPCookieJar()
        self._browser.set_cookiejar(cookie_jar)
        self._browser.set_handle_equiv(True)
        self._browser.set_handle_redirect(True)
        self._browser.set_handle_referer(True)
        self._browser.set_handle_robots(False)
        self._browser.set_handle_refresh(
            mechanize._http.HTTPRefreshProcessor(), max_time=1)
        self._browser.addheaders = [(
            'User-agent',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1)'
            + ' Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1'
            )]
