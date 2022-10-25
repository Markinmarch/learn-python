import unittest
from unittest.mock import patch
import buhgalteria_class

class TestBuhgalteria(unittest.TestCase):
    
    def setUp(self):
        self.func = buhgalteria_class.Buhgalteria()
        
    # @patch('buhgalteria_class.Buhgalteria')
    def test_comand_p(self):
        self.assertEqual(self.func.get_people_name('11-2'), 'Иерофан Покемонов')
        self.assertEqual(self.func.get_people_name('2207 876234'), 'Василий Питонов')
        self.assertEqual(self.func.get_people_name('10006'), 'Эдуард Шевелюров')
        
    def test_comand_s(self):
        self.assertEqual(self.func.get_shelf_number('11-2'), 'Документ находится на полке № 1')
        self.assertEqual(self.func.get_shelf_number('2207 876234'), 'Документ находится на полке № 1')
        self.assertEqual(self.func.get_shelf_number('10006'), 'Документ находится на полке № 2')
        
    def test_comand_l(self):
        self.assertEqual(self.func.get_list(), [
            'passport 2207 876234 Василий Питонов',
            'invoice 11-2 Иерофан Покемонов',
            'insurance 10006 Эдуард Шевелюров'
            ])
        
        
            
    
    # def test_Buh(self):
    #     self.assertEqual(self.func.huef(), 'Иерофан Покемонов')


if __name__ == '__main__':
    unittest.main()