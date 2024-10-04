#

import unittest
from textnode import TextNode



class TestTextNode(unittest.TestCase):
    def test_eq_(self):
        self.assertEqual(TextNode("This is a text node", "bold"), TextNode("This is a text node", "bold"))

    def test_not_eq_(self):
        self.assertNotEqual(TextNode("This is a text node", "italic"), TextNode("This is a text node", "bold"))
        self.assertNotEqual(TextNode("This is a txt node", "normal"), TextNode("This is a text node", "normal"))


if __name__ == "__main__":
    unittest.main(1)
