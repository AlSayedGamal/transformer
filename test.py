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


if __name__ == '__main__':
    unittest.main()
