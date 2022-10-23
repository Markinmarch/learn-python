import unittest
from work_ import main_work

class Test(unittest.TestCase):
    
    def setUp(self):
      
      self.func = main_work   
    
    def test_Zadacha_1(self):
        
        result = self.func
        etalon = 'Василий Питонов'
        self.assertEqual(result, etalon)
        
if __name__ == '__main__':
    unittest.main()