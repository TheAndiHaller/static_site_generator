import unittest

from htmlnode import HTMLNode


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



if __name__ == "__main__":
    unittest.main()