from textnode import *
from htmlnode import *
from tools import *

def main():
    my_text_node = TextNode("Hellouuu", TextType.LINK, "https://www.boot.dev")
    print(my_text_node)

    html_node = HTMLNode("a", "Click me!",None, {"href": "https://www.google.com"})
    print(html_node)
    print(html_node.props_to_html())

    leaf_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(leaf_node.to_html())

    node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

    print(node.to_html())

    node = TextNode("`code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    print(new_nodes)


if __name__ == "__main__":
    main()