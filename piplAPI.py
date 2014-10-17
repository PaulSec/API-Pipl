"""
This is the (unofficial) Python API for Pipl.com Website.
Using this code, you can manage to retrieve info on a specific person with his name.

"""
import requests
import re
import urllib


class PiplAPI(object):

    """
        PiplAPI Main Handler
    """

    _instance = None
    _verbose = False

    def __init__(self, arg=None):
        pass

    def __new__(cls, *args, **kwargs):
        """
            __new__ builtin
        """
        if not cls._instance:
            cls._instance = super(PiplAPI, cls).__new__(
                cls, *args, **kwargs)
            if (args and args[0] and args[0]['verbose']):
                cls._verbose = True
        return cls._instance

    def display_message(self, s):
        if (self._verbose):
            print '[verbose] %s' % s

    def get_info(self, name):
        url = 'https://pipl.com/search/?q=%s&l=&sloc=&in=5' % (name)
        self.display_message(url)
        req = requests.get(url)
        res = []

        results = re.findall(r"U=(http[a-zA-Z0-9%!/.?!]+)&P=", req.content)
        for result in results:
            url = urllib.unquote(result).decode('utf8')
            res.append(url)
            self.display_message('Profile found: %s' % (url))
        return res
