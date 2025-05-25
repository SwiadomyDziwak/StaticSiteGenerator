from enum import Enum

# TextType = Enum('text_type', ['normal', 'bold', 'italic', 'code', 'link', 'image'])

class TextType(Enum):
    normal = 'normal'
    bold = 'bold'
    italic = 'italic'
    code = 'code'
    link = 'link'
    image = 'image'

    
class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, another_text):
        if (self.text == another_text.text and
            self.text_type == another_text.text_type and
            self.url == another_text.url):
            return True
    
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'