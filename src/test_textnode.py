import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_in_eq(self):
        node = TextNode("This is a text nod", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_text_node_plain_text(self):
        tn = TextNode("hello", TextType.TEXT)
        html = text_node_to_html_node(tn)
        self.assertIsInstance(html, LeafNode)
        self.assertEqual(html.tag, None)
        self.assertEqual(html.value, "hello")
        self.assertEqual(html.props, None)

    def test_text_node_bold(self):
        tn = TextNode("bold text", TextType.BOLD)
        html = text_node_to_html_node(tn)
        self.assertEqual(html.tag, "b")
        self.assertEqual(html.value, "bold text")
        self.assertEqual(html.props, None)

    def test_text_node_code(self):
        tn = TextNode("print('hi')", TextType.CODE)
        html = text_node_to_html_node(tn)
        self.assertEqual(html.tag, "code")
        self.assertEqual(html.value, "print('hi')")
    
    def test_text_node_link(self):
        tn = TextNode("Google", TextType.LINK, "https://google.com")
        html = text_node_to_html_node(tn)
        self.assertEqual(html.tag, "a")
        self.assertEqual(html.value, "Google")
        self.assertEqual(html.props, {"href": "https://google.com"})

    """
    def test_text_node_link_missing_url(self):
        tn = TextNode("Click me", TextType.LINK, None)
        with self.assertRaises(TypeError):
            text_node_to_html_node(tn)
    """

    def test_text_node_img(self):
        tn = TextNode("cat pic", TextType.IMAGE, "cat.png")
        html = text_node_to_html_node(tn)
        self.assertEqual(html.tag, "img")
        self.assertEqual(html.value, "")
        self.assertEqual(html.props, {"src": "cat.png", "alt": "cat pic"})

    def test_text_node_round_trip(self):
        tn = TextNode("hello", TextType.BOLD)
        html = text_node_to_html_node(tn)
        self.assertEqual(html.to_html(), "<b>hello</b>")

if __name__ == "__main__":
    unittest.main()