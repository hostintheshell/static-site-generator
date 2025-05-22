from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(textnode_1, textnode_2):
        return (textnode_1.text == textnode_2.text) and (textnode_1.text_type == textnode_2.text_type) and (textnode_1.url == textnode_2.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"