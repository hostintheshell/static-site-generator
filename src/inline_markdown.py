from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_list = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            node_split = node.text.split(delimiter)
            if len(node_split) % 2 == 0:
                raise Exception("Invalid Markdown Syntax")
            
            for i, split in enumerate(node_split):
                if split == "":
                    continue
                if i % 2 == 0:
                    node_list.append(TextNode(split, TextType.TEXT))
                else:
                    node_list.append(TextNode(split, text_type))
        
        else:
            node_list.append(node)
    
    return node_list