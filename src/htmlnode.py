#


class HTMLNode():
    def __init__(self,
                 tag: str = None,
                 value: str = None,
                 children: list = list(),
                 props: dict = dict()):
        """
        :param tag:  string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        :param value: string representing the value of the HTML tag (e.g. the text inside a paragraph)
        :param children: list of HTMLNode objects representing the children of this node
        :param props: dictionary of key-value pairs representing the attributes of the HTML tag.
                        For example, a link (<a> tag) might have {"href": "https://www.google.com"}
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def __repr__(self):
        tag_str = f"tag: {self.tag}"
        value_str = f"value: {self.value}"
        children_str = f"children: {str(self.children)}"
        props_str = f"props: {str(self.props)}"
        return "\n".join([tag_str, value_str, children_str, props_str])


    def to_html(self):
        raise NotImplementedError("Not implemented")


    def props_to_html(self):
        """
        Returns a string that represents the HTML attributes of the node
        """
        prop_strings = []
        for k, v in self.props.items():
            prop_strings.append(f"{k}=\"{v}\"")
        return " ".join(prop_strings)
