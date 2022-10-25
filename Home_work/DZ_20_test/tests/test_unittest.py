import unittest
import buhgalteria_class, data

class Test(unittest.TestCase):
    
    def setUp(self):
        self.func = buhgalteria_class.Buhgalteria.get_people_name()

    def test_Zadacha_1(self):
        self.assertEqual(self.func, 'Иерофан Покемонов')

if __name__ == '__main__':
    unittest.main()
# if __name__ == '__main__':
#     unittest.main()