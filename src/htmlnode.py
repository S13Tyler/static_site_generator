#


class HTMLNode():
    def __init__(self,
                 tag: str = None,
                 value: str = None,
                 children: list = None,
                 props: dict = None):
        """
        HTMLNode represents a "node" in an HTML document tree and is purpose-built to render itself as HTML

        :param tag:  string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        :param value: string representing the value of the HTML tag (e.g. the text inside a paragraph)
        :param children: list of HTMLNode objects representing the children of this node
        :param props: dictionary of key-value pairs representing the attributes of the HTML tag
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, props: {self.props})"

    def to_html(self):
        raise NotImplementedError("Function: to_html() not implemented. Try on child variant.")

    def props_to_html(self):
        """
        Returns a string that represents the HTML attributes of the node
        """
        if not self.props:
            return ""
        prop_strings = []
        for k, v in self.props.items():
            prop_strings.append(f"{k}=\"{v}\"")
        return " ".join(prop_strings)

    def wrap_tags(self, value = None):
        content = self.value
        if value:
            content = value
        if self.props:
            return f"<{self.tag} {self.props_to_html()}>{content}</{self.tag}>"
        return f"<{self.tag}>{content}</{self.tag}>"

    def textnode_to_htmlnode(text_node):
        match(text_node.text_type):
            case "text":
                return LeafNode(None, text_node.text, None)
            case "bold":
                return LeafNode("b", text_node.text, None)
            case "italic":
                return LeafNode("i", text_node.text, None)
            case "code":
                return LeafNode("code", text_node.text, None)
            case "link":
                return LeafNode("a", text_node.text, {"href": text_node.url})
            case "image":
                return LeafNode("img", None, {"src": text_node.url, "alt": text_node.text})
        raise Exception("Invalid HTML (type: TextNode) -> Invalid 'type'")



class LeafNode(HTMLNode):
    def __init__(self,
                 tag: str,
                 value: str,
                 props: dict = None):
        """
        A LeafNode is a type of HTMLNode that represents a single HTML tag with no children

        :param tag:         string representing the HTML tag name (e.g. "p", "a", "h1", etc.)`
        :param value:       string representing the value of the HTML tag (e.g. the text inside a paragraph)
        :param props:       dictionary of key-value pairs representing the attributes of the HTML tag
        """
        super().__init__(tag, value, None, props)


    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def to_html(self):
        if not self.value:
            raise ValueError("Invalid HTML (type: LeafNode) -> No value")
        if not self.tag:
            return self.value
        return self.wrap_tags()


class ParentNode(HTMLNode):
    def __init__(self,
                 tag: str,
                 children: list,
                 props: dict = None):
        """
        Handles the nesting of HTML nodes inside of one another.
        Any HTML node that's not "leaf" node (i.e. it has children) is a "parent" node.

        :param children: list of HTMLNode objects representing the children of this node
        :param tag:  string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
        :param props: dictionary of key-value pairs representing the attributes of the HTML tag
        """
        super().__init__(tag, None, children, props)

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

    def to_html(self):
        if not self.tag:
            raise ValueError("Invalid HTMLNode (type: ParentNode) -> No tag")
        if not self.children:
            raise ValueError("Invalid HTMLNode (type: ParentNode) -> No children")

        html_str = ""
        for child in self.children:
            html_str += child.to_html()
        return self.wrap_tags(html_str)
