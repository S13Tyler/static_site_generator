#

import unittest
from leafnode import LeafNode


test_cases = [
    {
        'obj_params': [
            "This is a paragraph of text.",
            "p",
        ],
        'expected': "<p>This is a paragraph of text.</p>",
    },
    {
        'obj_params': [
            "Click me!",
            "a",
            {"href": "https://www.google.com"},
        ],
        'expected': "<a href=\"https://www.google.com\">Click me!</a>"
    },
]



class TestLeafNode(unittest.TestCase):
    def test_no_props_(self):
        test_node = LeafNode(*test_cases[0]['obj_params'])
        self.assertEqual(test_node.to_html(), test_cases[0]['expected'])

    def test_with_props_(self):
        test_node = LeafNode(*test_cases[1]['obj_params'])
        self.assertEqual(test_node.to_html(), test_cases[1]['expected'])
