import re
from htmlnode import *
from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    text_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            text_nodes.append(node)
        else:
            text = node.text
            if delimiter in text:
                sections = text.split(delimiter)
                for i in range(len(sections)):
                    if len(sections[i]) == 0:
                        continue
                    if i % 2 == 0:
                        text_nodes.append(TextNode(sections[i], TextType.TEXT))
                    else:
                        text_nodes.append(TextNode(sections[i], text_type))
            else:
                raise ValueError("Not valid Markdown")

    return text_nodes


def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
