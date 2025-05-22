from textnode import *

print("hello world")

def main():
    dummy_values = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(dummy_values)


main()