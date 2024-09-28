#


class HTMLNode():
    def __init__(self,
                 value: str = None,
                 tag: str = None,
                 children: list = None,
                 props: dict = None):
        """
        HTMLNode represents a "node" in an HTML document tree and is purpose-built to render itself as HTML

        :param value: string representing the value of the HTML tag (e.g. the text inside a paragraph)
        :param tag:  string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        :param children: list of HTMLNode objects representing the children of this node
        :param props: dictionary of key-value pairs representing the attributes of the HTML tag
        """
        self.value = value
        self.tag = tag
        self.children = children
        self.props = props


    def __repr__(self):
        value_str = f"value: {self.value}"
        tag_str = f"tag: {self.tag}"
        children_str = f"children: {str(self.children)}"
        props_str = f"props: {str(self.props)}"
        return "\n".join([value_str, tag_str, children_str, props_str])


    def to_html(self):
        raise NotImplementedError("Not implemented")


    def props_to_html(self):
        """
        Returns a string that represents the HTML attributes of the node
        """
        if self.props:
            prop_strings = []
            for k, v in self.props.items():
                prop_strings.append(f"{k}=\"{v}\"")
            return " ".join(prop_strings)
        return None
