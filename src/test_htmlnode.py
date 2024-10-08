#

import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode



class TestHTMLNode(unittest.TestCase):
    #
    # HTML Node Tests
    #
    def test_htmlnode_values(self):
        # Test that object has correct object params
        test_node = HTMLNode(
            "a",
            "Test case #1: test object tag & value"
        )
        self.assertEqual(
            [test_node.tag, test_node.value, test_node.children, test_node.props],
            ["a", "Test case #1: test object tag & value", None, None],
            "Failed: htmlnode_values"
        )

    def test_htmlnode_repr(self):
        # Test output of __repr__
        test_node = HTMLNode(
            "h1",
            "Test case #3: test __repr__"
        )
        self.assertEqual(
            test_node.__repr__(),
            "HTMLNode(h1, Test case #3: test __repr__, children: None, props: None)",
            "Failed: htmlnode_repr"
        )

    def test_htmlnode_tohtml_wprops(self):
        # Test output of props_to_html
        test_node = HTMLNode(
            "p",
            "Test case #2: props_to_html",
            None,
            {'href': "https://www.google.com", 'target': "_blank"}
        )
        self.assertEqual(
            test_node.props_to_html(),
            "href=\"https://www.google.com\" target=\"_blank\"",
            "Failed: htmlnode_tohtml_wprops"
        )

    def test_textnode_to_htmlnode_text(self):
        text_node = TextNode("I'm a TextNode of type: text", "text")
        expected = LeafNode(None, "I'm a TextNode of type: text")
        self.assertEqual(
            HTMLNode.textnode_to_htmlnode(text_node).__repr__(),
            expected.__repr__(),
            "Failed: textnode_to_htmlnode_text"
        )

    def test_textnode_to_htmlnode_bold(self):
        text_node = TextNode("I'm a TextNode of type: bold", "bold")
        expected = LeafNode("b", "I'm a TextNode of type: bold")
        self.assertEqual(
            HTMLNode.textnode_to_htmlnode(text_node).__repr__(),
            expected.__repr__(),
            "Failed: textnode_to_htmlnode_bold"
        )

    def test_textnode_to_htmlnode_italic(self):
        text_node = TextNode("I'm a TextNode of type: italic", "italic")
        expected = LeafNode("i", "I'm a TextNode of type: italic")
        self.assertEqual(
            HTMLNode.textnode_to_htmlnode(text_node).__repr__(),
            expected.__repr__(),
            "Failed: textnode_to_htmlnode_italic"
        )

    def test_textnode_to_htmlnode_code(self):
        text_node = TextNode("I'm a TextNode of type: code", "code")
        expected = LeafNode("code", "I'm a TextNode of type: code")
        self.assertEqual(
            HTMLNode.textnode_to_htmlnode(text_node).__repr__(),
            expected.__repr__(),
            "Failed: textnode_to_htmlnode_code"
        )

    def test_textnode_to_htmlnode_link(self):
        text_node = TextNode("I'm a TextNode of type: link", "link", "https://www.google.com/")
        expected = LeafNode("a", "I'm a TextNode of type: link", {"href": "https://www.google.com/"})
        self.assertEqual(
            HTMLNode.textnode_to_htmlnode(text_node).__repr__(),
            expected.__repr__(),
            "Failed: textnode_to_htmlnode_link"
        )

    def test_textnode_to_htmlnode_image(self):
        text_node = TextNode("I'm a TextNode of type: image", "image", "https://www.google.com/")
        expected = LeafNode("img", None, {"src": "https://www.google.com/", "alt": "I'm a TextNode of type: image"})
        self.assertEqual(
            HTMLNode.textnode_to_htmlnode(text_node).__repr__(),
            expected.__repr__(),
            "Failed: textnode_to_htmlnode_image"
        )

    def test_textnode_to_htmlnode_none(self):
        text_node = TextNode("I'm a TextNode of type: none", "none")
        with self.assertRaises(Exception):
            HTMLNode.textnode_to_htmlnode(text_node)





    #
    # Lead Node Tests
    #
    def test_leafnode_tohtml_noprops(self):
        test_node = LeafNode(
            "p",
            "This is a paragraph of text."
        )
        self.assertEqual(
            test_node.to_html(),
            "<p>This is a paragraph of text.</p>",
            "Failed: leafnode_tohtml_noprops"
        )

    def test_leafnode_tohtml_wprops(self):
        test_node = LeafNode(
            "a",
            "Click me!",
            {"href": "https://www.google.com"}
        )
        self.assertEqual(
            test_node.to_html(),
            "<a href=\"https://www.google.com\">Click me!</a>",
            "Failed: leafnode_tohtml_wprops"
        )


    #
    # Parent Node Tests
    #
    def test_parentnode_tohtml_wchildren(self):
        child_node = LeafNode("b", "I'm a child!")
        test_node = ParentNode("div", [child_node,])
        self.assertEqual(
            test_node.to_html(),
            "<div><b>I'm a child!</b></div>",
            "Failed: parentnode_tohtml_wchildren"
        )

    def test_parentnode_tohtml_wsubchildren(self):
        sub_child_node = LeafNode("p", "I'm a child's child!")
        child_node = ParentNode("b", [sub_child_node,])
        test_node = ParentNode("div", [child_node,])
        self.assertEqual(
            test_node.to_html(),
            "<div><b><p>I'm a child's child!</p></b></div>",
            "Failed: parentnode_tohtml_wsubchildren"
        )

    def test_parentnode_tohtml__manychildren(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
            "Failed: parentnode_tohtml__manychildren"
        )

    def test_parentnode_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
            "Failed: parentnode_headings"
        )


if __name__ == "__main__":
    unittest.main(1)
