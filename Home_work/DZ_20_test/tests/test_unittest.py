import unittest
from unittest import result
from unittest.mock import patch

from DZ_5_dict_def import Zadacha_1

class TestFunc(unittest.TestCase):
    
    # def setUp(self) -> None:
    #     print('setUp ==>')
        
    @patch('Zadacha_1.')
    # def tearDown(self) -> None:
    #     print('tearDown')
        
    def test_Zadacha_1(self):

        self.assertEqual(etalon, result)
        