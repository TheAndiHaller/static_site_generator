from textnode import *
from htmlnode import *
from tools import *

def main():

    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    result = text_to_textnodes(text)
    
    for item in result:
        print(f"- {item.text_type} = {item}")


    return


if __name__ == "__main__":
    main()