#

class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        eq1 = self.text == other.text
        eq2 = self.text_type == other.text_type
        eq3 = self.url == other.url
        return eq1 and eq2 and eq3

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
