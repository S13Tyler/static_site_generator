#

import unittest
from textnode import TextNode


test_cases = [
    (["This is a text node", "bold"],   ["This is a text node", "bold"],    True),
    (["This is a text node", "italic"], ["This is a text node", "bold"],    False),
    (["This is a txt node", "normal"],  ["This is a text node", "normal"],  False),
]



class TestTextNode(unittest.TestCase):
    def test_eq_(self):
        for item in test_cases:
            if item[2]:
                self.assertEqual(TextNode(*item[0]), TextNode(*item[1]))
            else:
                self.assertNotEqual(TextNode(*item[0]), TextNode(*item[1]))


if __name__ == "__main__":
    unittest.main(1)
