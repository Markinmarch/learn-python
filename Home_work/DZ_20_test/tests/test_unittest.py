from unittest import TestCase
from DZ_5_dict_def import Zadacha_1

class Test(TestCase):
    
    def setUp(self):
        self.test_func = Zadacha_1
        
    # def tearDown(self) -> None:
    #     print('tearDown') 
    def test_Zadacha_1(self):
        
        result = self.test_func.get_people_name('2207 876234')
        etalon = 'Василий Питонов'
        self.assertEqual(result, etalon)
        
if __name__ == '__main__':
    unittest.main()