import unittest
from vendingMachine import *

class TestVendingMachine(unittest.TestCase):
   def test_return_change(self):
       coins = give_change(17)
       self.assertEqual(coins, [10, 5, 2], 'wrong change given')

    def test_use_same_coin(self):
        coins = give_change(4)
        self.assertEqual(coins, [2, 2], 'same coin not used twice')