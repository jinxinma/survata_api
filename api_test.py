import httplib
import unittest
import pandas as pd
from helper_function import *

# Survata Data Challenge API
# Authors: Jinxin Ma

SERVER = '0.0.0.0:5000'


class Test_API(unittest.TestCase):
    ########## TEST FOR API ##########
    # test API homepage
    def test_home(self):
        h = httplib.HTTPConnection(SERVER)
        h.request('GET', 'http://' + SERVER + '/')
        resp = h.getresponse()
        out = resp.read()

        # The jsonify() function in flask returns flask.Response() object that
        # already has the appropriate content-type header 'application/json' for use
        # with json responses. So "out" has new line characters. As a result, I needed
        # to also add '\n' in the second parameter of self.assertEqual ensure consistency
        self.assertEqual(out, '{\n  "message": "Welcome to Survata API for data retrieval"\n}\n')

    # test the if the first row of data can be returned
    def test_head(self):
        h = httplib.HTTPConnection(SERVER)
        h.request('GET', 'http://' + SERVER + '/head')
        resp = h.getresponse()
        out = resp.read()
        self.assertEqual(out, '[\n  {\n    "Country": "US", \n    "Exposure Stamps": NaN, \n ' +
                         '   "Gender": "female", \n    "Survata Interview ID": "1a"\n  }\n]\n')

    # test if query can take multiple id's
    def test_query1(self):
        h = httplib.HTTPConnection(SERVER)
        h.request('GET', 'http://' + SERVER + '/query?%s' % 'id=1a&id=2b&col=Gender')
        resp = h.getresponse()
        out = resp.read()
        self.assertEqual(out, '[\n  {\n    "Gender": "female", \n    "Survata Interview ID": "1a"\n  }, \n  {\n  ' +
                         '  "Gender": "male", \n    "Survata Interview ID": "2b"\n  }\n]\n')

    # test if API can return correct number of exposure ID's for each interview ID
    def test_query2(self):
        h = httplib.HTTPConnection(SERVER)
        h.request('GET', 'http://' + SERVER + '/query?%s' % 'id=4d&exp_id=403060619')
        resp = h.getresponse()
        out = resp.read()
        self.assertEqual(out, '[\n  {\n    "Exposure ID Count": 2, \n  ' +
                         '  "Survata Interview ID": "4d"\n  }\n]\n')

    # test if API can return correct response when no value is provided from "col"
    def test_query3(self):
        h = httplib.HTTPConnection(SERVER)
        h.request('GET', 'http://' + SERVER + '/query?%s' % 'id=4d&col')
        resp = h.getresponse()
        out = resp.read()
        self.assertEqual(out, '{\n  "error": "Bad request"\n}\n')


    ########## TEST FOR HELPER FUNCTIONS ##########
    def test_split_exposure_stamps(self):
        exposure_stamp = '2017-09-07 09:21:47.0 : 403060619,20184888,91495470,203266115,4101327' + \
                         ' | 2017-09-15 07:32:42.0 : 403060619,20184888,91495470,203266973,4101327'
        self.assertEqual(split_exposure_stamps(exposure_stamp, '20184888'), 2)


if __name__ == '__main__':
    unittest.main()








