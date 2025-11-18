from textnode import *
from htmlnode import *
from tools import *
from block_type import *

def main():
    markdown = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item"
"""
    result = markdown_to_blocks(markdown)
    

    for item in result:
        print(f"TYPE: {block_to_block_type(item)} = {item}")
        




    return


if __name__ == "__main__":
    main()