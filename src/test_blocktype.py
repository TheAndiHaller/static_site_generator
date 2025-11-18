
import unittest
from tools import *
from block_type import *
from textnode import TextNode, TextType

class TestBlockTypeMarkdown(unittest.TestCase):
    def test_block_to_block_type_paragraph(self):
        block = "This is a normal paragraph."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_heading(self):
        block = "# This is a heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_block_to_block_type_code_block(self):
        block = "```\n some code \n some more code \n even more code \n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_block_to_block_type_quote(self):
        block = "> This is a quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_block_to_block_type_unordered_list(self):
        block = "- item 1\n- item 2"
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)
    
    def test_block_to_block_type_ordered_list(self):
        block = "1. first item\n2. second item"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)

    def test_block_to_block_type_heading_not_matched(self):
        block = "## Not detected by this function"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_block_to_block_typesss(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.ULIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.OLIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_unordered_list_missing_space(self):
        block = "-item"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_block_to_block_type_ordered_list_not_one(self):
        block = "2. item"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)



if __name__ == "__main__":
    unittest.main()