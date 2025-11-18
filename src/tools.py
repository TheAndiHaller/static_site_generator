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
    new_nodes = []
    new_node = TextNode(text, TextType.TEXT)
    new_nodes.extend(split_nodes_delimiter([new_node], "**", TextType.BOLD))
    new_nodes.extend(split_nodes_delimiter(new_nodes, "_", TextType.ITALIC))
    new_nodes.extend(split_nodes_delimiter(new_nodes, "`", TextType.CODE))
    new_nodes.extend(split_nodes_image(new_nodes))
    new_nodes.extend(split_nodes_link(new_nodes))
    return new_nodes