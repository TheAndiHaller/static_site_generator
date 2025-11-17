from textnode import *
from htmlnode import *
from tools import *

def main():

    text_1 = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    text_2 = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"

    print(extract_markdown_images(text_1))
    print(extract_markdown_images(text_2))
    print(extract_markdown_links(text_1))
    print(extract_markdown_links(text_2))

if __name__ == "__main__":
    main()