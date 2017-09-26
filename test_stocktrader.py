# coding: utf-8

import unittest
from guotai import trader
import helpers


class Tests_stocktrader ( unittest.TestCase ):
    @classmethod
    def setUpClass(cls):
        print ( "something prepared" )
        cls._trader = trader()

    def tearDown(self):
        print ( "end the session" )

    def test_guotai(self):
#        account = helpers.file2dict ( "./config/desired_caps.json" )
#        print ( account )
        self._trader.stock_buy(600001,12,200)

if __name__ == '__main__':
    suite = unittest.TestLoader ( ).loadTestsFromTestCase ( Tests_stocktrader )
    unittest.TextTestRunner ( verbosity=2 ).run ( suite )
