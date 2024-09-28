#

from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self,
                 value: str,
                 tag: str = None,
                 props: dict = None):
        """
        A LeafNode is a type of HTMLNode that represents a single HTML tag with no children

        :param value:       string representing the value of the HTML tag (e.g. the text inside a paragraph)
        :param tag:         string representing the HTML tag name (e.g. "p", "a", "h1", etc.)`
        :param props:       dictionary of key-value pairs representing the attributes of the HTML tag
        """

        super().__init__(value, tag, [], props)
        delattr(self, 'children')


    def to_html(self):
        if not self.value:
            raise ValueError("No value")
        if not self.tag:
            return self.value
        if self.props:
            return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
