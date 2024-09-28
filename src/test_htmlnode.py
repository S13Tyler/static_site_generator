#

import unittest
from htmlnode import HTMLNode


test_cases = [
    {
        'obj_params': [
            "Test case #1: test object tag & value",
            "a",
        ],
        'expected': ["Test case #1: test object tag & value", "a", None, None],
    },
    {
        'obj_params': [
            "Test case #2: props_to_html",
            "p",
            [],
            {"href": "https://www.google.com", "target": "_blank",},
        ],
        'expected': "href=\"https://www.google.com\" target=\"_blank\"",
    },
    {
        'obj_params': [
            "Test case #3: test __repr__",
            "h1",
        ],
        'expected': "value: Test case #3: test __repr__\ntag: h1\nchildren: None\nprops: None",
    },
]


class TestHTMLNode(unittest.TestCase):
    def test_object_params_(self):
        # Test that object has correct object params
        test_node = HTMLNode(*test_cases[0]['obj_params'])
        test_node_1_params = [test_node.value, test_node.tag, test_node.children, test_node.props]
        self.assertEqual(test_node_1_params, test_cases[0]['expected'], f"Failed: {test_node.value}")

    def test_repr_(self):
        # Test output of __repr__
        test_node = HTMLNode(*test_cases[2]['obj_params'])
        self.assertEqual(repr(test_node), test_cases[2]['expected'], f"Failed: {test_node.value}")

    def test_props_to_html_(self):
        # Test output of props_to_html
        test_node = HTMLNode(*test_cases[1]['obj_params'])
        self.assertEqual(test_node.props_to_html(), test_cases[1]['expected'], f"Failed: {test_node.value}")



if __name__ == "__main__":
    unittest.main(1)
