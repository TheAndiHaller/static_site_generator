class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        props_str = ""
        if self.props:
            for k, v in self.props.items():
                props_str += f" {k}=\"{v}\""
        return props_str

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("value is required")
        if self.tag == None:
            return f"{self.value}"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("tag is required")
        if not self.children:
            raise ValueError("A parent has to have a child (duh)")
        else:
            html_str = f"<{self.tag}{self.props_to_html()}>"
            for child in self.children:
                html_str += child.to_html()
        
            html_str += f"</{self.tag}>"
            return html_str

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.children}, {self.props})"