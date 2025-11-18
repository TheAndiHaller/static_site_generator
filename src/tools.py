import re
from htmlnode import *
from textnode import *

"""
# I don't see it
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    text_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            text_nodes.append(node)
            continue
        text = node.text
        split_nodes = []
        sections = text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")

        for i in range(len(sections)):
            if len(sections[i]) == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        text_nodes.extend(split_nodes)
    return text_nodes

"""

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes



def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches


def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            extracted = extract_markdown_images(node.text)
            if len(extracted) == 0:
                new_nodes.append(node)
            else:
                original_text = node.text

                for i in range(len(extracted)):
                    sections = original_text.split(f"![{extracted[i][0]}]({extracted[i][1]})", 1)
                    
                    if len(sections) != 2:
                        raise ValueError("invalid markdown, image section not closed")
                    
                    if sections[0] != "":
                        new_nodes.append(TextNode(sections[0], TextType.TEXT))
                    new_nodes.append(TextNode(extracted[i][0], TextType.IMAGE, extracted[i][1]))
                    original_text = sections[1]
                if original_text != "":
                    new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            extracted = extract_markdown_links(node.text)
            if len(extracted) == 0:
                new_nodes.append(node)
            else:
                original_text = node.text

                for i in range(len(extracted)):
                    sections = original_text.split(f"[{extracted[i][0]}]({extracted[i][1]})", 1)
                    
                    if len(sections) != 2:
                        raise ValueError("invalid markdown, link section not closed")
                    
                    if sections[0] != "":
                        new_nodes.append(TextNode(sections[0], TextType.TEXT))
                    new_nodes.append(TextNode(extracted[i][0], TextType.LINK, extracted[i][1]))
                    original_text = sections[1]
                if original_text != "":
                    new_nodes.append(TextNode(original_text, TextType.TEXT))

    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


def markdown_to_blocks(markdown):
    new_blocks = []
    splits = markdown.split("\n\n")
    for item in splits:
        item = item.strip()
        item = item.strip("\n")
        if len(item) > 0:
            new_blocks.append(item)


    return new_blocks