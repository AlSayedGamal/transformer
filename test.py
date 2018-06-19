import unittest
from transformer import Transformer


class TestBasicDictTemplates(unittest.TestCase):
    def setUp(self):
        class Foo(object):
            def __init__(self):
                self.first_name = "Hassan"
                self.last_name = "Ali"
                self.age = 21
        self.source = Foo()
        self.sourceDict = {
            "first_name": "Hassan",
            "last_name": "Ali",
            "age": 21
        }

    def testSimpleValues(self):
        template = {
            'foo': 'bar',
            'first_name': 'Ahmed',
            'last_name': 'Gamal',
            'age': 31
        }
        t = Transformer(template=template)
        self.assertEqual(t(self.source), template)

    def testCalculatedValues(self):
        template = {
            'name': '${first_name} + " " + ${last_name}',
            'years_old': '"%d years old" %${age}'
        }
        t = Transformer(template)
        self.assertEqual(t(self.source), {'name': 'Hassan Ali', 'years_old': '21 years old'})

    def testWrongTemplateAttributes(self):
        template = {
            'name': '${first_name} + " " + ${not_attribute}',
            'age': '${age}'
        }
        t = Transformer(template)
        with self.assertRaises(Exception):
            t(self.source)


    def testWrongTemplates(self):
        template = {
            'name': '+ 1 ${age}', #invalid python syntax
            'age': '${age}'
        }
        t = Transformer(template)
        with self.assertRaises(Exception):
            t(self.source)

    
    def testDictSimpleValues(self):
        template = {
            'foo': 'bar',
            'first_name': 'Ahmed',
            'last_name': 'Gamal',
            'age': 31
        }
        t = Transformer(template=template)
        self.assertEqual(t(self.sourceDict), template)

    def testDictCalculatedValues(self):
        template = {
            'name': '${first_name} + " " + ${last_name}',
            'years_old': '"%d years old" %${age}'
        }
        t = Transformer(template)
        self.assertEqual(t(self.sourceDict), {'name': 'Hassan Ali', 'years_old': '21 years old'})


    def testDictWrongTemplateAttributes(self):
        template = {
            'name': '${first_name} + " " + ${not_attribute}',
            'age': '${age}'
        }
        t = Transformer(template)
        with self.assertRaises(Exception):
            t(self.sourceDict)
    

    def testDictWrongTemplates(self):
        template = {
            'name': '+ 1 ${age}', #invalid python syntax
            'age': '${age}'
        }
        t = Transformer(template)
        with self.assertRaises(Exception):
            t(self.sourceDict)


if __name__ == '__main__':
    unittest.main()
