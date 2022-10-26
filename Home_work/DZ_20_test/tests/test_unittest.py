import unittest
from work.buhgalteria_class import Buhgalteria

class TestBuhgalteria(unittest.TestCase):
    
    def setUp(self):
        self.func = Buhgalteria()

    def test_comand_p1(self):
        self.assertEqual(self.func.get_people_name('11-2'), 'Иерофан Покемонов')
    def test_comand_p2(self):
        self.assertEqual(self.func.get_people_name('2207 876234'), 'Василий Питонов')
    def test_comand_p3(self):
        self.assertEqual(self.func.get_people_name('10006'), 'Эдуард Шевелюров') 
    def test_comand_s1(self):
        self.assertEqual(self.func.get_shelf_number('11-2'), 'Документ находится на полке № 1')
    def test_comand_s2(self):
        self.assertEqual(self.func.get_shelf_number('2207 876234'), 'Документ находится на полке № 1')
    def test_comand_s3(self):
        self.assertEqual(self.func.get_shelf_number('10006'), 'Документ находится на полке № 2')
    def test_comand_s4(self):
        self.assertEqual(self.func.get_shelf_number('0123456'), 'Документ находится на полке № 3')   
    def test_comand_l(self):
        self.assertEqual(self.func.get_list(),
            ['passport 2207 876234 Василий Питонов',
            'invoice 11-2 Иерофан Покемонов',
            'insurance 10006 Эдуард Шевелюров',
            'document type 0123456 Name Surname']
            )
    def test_comand_a(self):
        self.assertEqual(self.func.add_doc(
            {
                'type':'document type',
                'number':'0123456',
                'name':'Name Surname'
                }, '3'),
            ([
                'passport 2207 876234 Василий Питонов',
                'invoice 11-2 Иерофан Покемонов',
                'insurance 10006 Эдуард Шевелюров',
                'document type 0123456 Name Surname'
                ],
            {
                '1': ['2207 876234', '11-2', '5455 028765'],
                '2': ['10006'],
                '3': ['0123456']
                }))
        
if __name__ == '__main__':
    unittest.main()