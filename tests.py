#! /usr/bin/env python


import unittest

from red4emacs import sort_arguments

class TestRed4Emacs(unittest.TestCase):

    def setUp(self):
        pass

    def test_nominal(self):
        txt = "def foo(bar): pass"
        out = sort_arguments(txt=txt)
        self.assertTrue(out in txt)

    def test_order(self):
        txt = "def foo(**kwargs, first): pass"
        out = sort_arguments(txt=txt)
        self.assertEqual(out, "def foo(first, **kwargs):")

        txt = "def foo(**kwargs, key=val): pass"
        out = sort_arguments(txt=txt)
        self.assertEqual(out, "def foo(key=val, **kwargs):")

        txt = "def foo(**kwargs, key=val, first): pass"
        correct = "def foo(first, key=val, **kwargs):"
        self.assertEqual(correct, sort_arguments(txt=txt))

    def test_insert_last(self):
        txt = "def foo(self, key=val, second): pass"
        correct = "def foo(self, second, key=val):"
        self.assertEqual(correct, sort_arguments(txt=txt))

if __name__ == "__main__":
    unittest.main()
