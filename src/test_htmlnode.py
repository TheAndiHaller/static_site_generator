import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_raise(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_repr(self):
        node = HTMLNode("a", "boot.dev", props={"href": "https://www.boot.dev", "target": "_blank"})
        self.assertEqual("HTMLNode(a, boot.dev, None, {'href': 'https://www.boot.dev', 'target': '_blank'})", repr(node))

    def test_props_to_html(self):
        node = HTMLNode("a", "boot.dev", props={"href": "https://www.boot.dev", "target": "_blank"})
        self.assertEqual(" href=\"https://www.boot.dev\" target=\"_blank\"", node.props_to_html())


    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

    def test_no_val(self):
        node = LeafNode("a", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_no_child(self):
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_parentnode_with_props(self):
        child = LeafNode("span", "hi")
        parent = ParentNode("div", [child], {"class": "box"})
        self.assertEqual(parent.to_html(), '<div class="box"><span>hi</span></div>')

    def test_parentnode_multiple_children(self):
        children = [
            LeafNode("span", "one"),
            LeafNode("b", "two"),
            LeafNode("i", "three"),
        ]
        parent = ParentNode("div", children)
        self.assertEqual(
            parent.to_html(),
            "<div><span>one</span><b>two</b><i>three</i></div>"
        )
    def test_parentnode_no_tag_raises(self):
        child = LeafNode("span", "hey")
        node = ParentNode(None, [child])
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_parentnode_empty_child_list(self):
        node = ParentNode("div", [])
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_deep_nesting(self):
        deep = ParentNode("div", [
            ParentNode("section", [
                ParentNode("article", [
                    LeafNode("p", "deep text")
                ])
            ])
        ])
        self.assertEqual(
            deep.to_html(),
            "<div><section><article><p>deep text</p></article></section></div>"
        )

if __name__ == "__main__":
    unittest.main()