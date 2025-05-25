from textnode import TextNode
from textnode import TextType

def main():
    text_node = TextNode('Hello world', TextType.normal)
    print(text_node)

if __name__ == '__main__':
    main()