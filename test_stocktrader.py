# coding: utf-8

import unittest
import guotai
import helpers

class Tests_stocktrader(unittest.TestCase):
    def setUp(self):
        print("something prepared")

    def tearDown(self):
        print ( "end the session")

    def test_guotai(self):
        account = helpers.file2dict ( "./config/desired_caps.json" )
        print(account)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Tests_stocktrader)
    unittest.TextTestRunner(verbosity=2).run(suite)