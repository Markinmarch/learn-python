import unittest
from unittest import result

from DZ_5_dict_def import Zadacha_1

class TestFunc(unittest.TestCase):
    
    def setUp(self) -> None:
        print('setUp ==>')
        
    def tearDown(self) -> None:
        print('tearDown')
        
    def test_Zadacha_1(self):
        
        result = 'Возможные команды: p, s, l, a'
        etalon = 'Возможные команды: p, s, l, a'
        self.assertEqual(etalon, result)
        