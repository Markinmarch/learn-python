import unittest
from work_ import buhgalteria

class Test(unittest.TestCase):
    
    def setUp(self):
      
      self.func = buhgalteria.get_people_name('2207 876234')   
    
    def test_Zadacha_1(self):
        
        result = self.func
        etalon = 'Василий Питонов'
        self.assertEqual(result, etalon)
        
if __name__ == '__main__':
    unittest.main()