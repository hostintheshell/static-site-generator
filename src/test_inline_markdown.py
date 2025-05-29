import unittest

from textnode import *
from inline_markdown import *

class TestDelimiterFunc(unittest.TestCase):
    def test_single_pair(self):
        test_node = TextNode("This is text with a `code block` word", TextType.TEXT)
        test_delimiter = split_nodes_delimiter([test_node], "`", TextType.CODE)
        expected_list = [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT)]
        self.assertEqual(test_delimiter, expected_list)

    def test_multiple_pairs(self):
        test_node = TextNode("This is text with a `code block` word and another `code block` word", TextType.TEXT)
        test_delimiter = split_nodes_delimiter([test_node], "`", TextType.CODE)
        expected_list = [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), 
                         TextNode(" word and another ", TextType.TEXT), TextNode("code block", TextType.CODE), TextNode(" word", TextType.TEXT)]
        self.assertEqual(test_delimiter, expected_list)

    def test_unmatched_pair(self):
        test_node = TextNode("This is text with a **bold block word", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([test_node], "**", TextType.BOLD)
        self.assertIn("Invalid Markdown Syntax", str(context.exception))

    def test_no_delimiter(self):
        test_node = TextNode("This is text with a line of text with no delimiter", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([test_node], "", TextType.TEXT)

    def test_delimiter_beginning(self):
        test_node = TextNode("_This_ is italic at the beginning", TextType.TEXT)
        test_delimiter = split_nodes_delimiter([test_node], "_", TextType.ITALIC)
        expected_list = [TextNode("This", TextType.ITALIC), TextNode(" is italic at the beginning", TextType.TEXT)]
        self.assertEqual(test_delimiter, expected_list)
    
    def test_delimiter_end(self):
        test_node = TextNode("This is italic at the _end_", TextType.TEXT)
        test_delimiter = split_nodes_delimiter([test_node], "_", TextType.ITALIC)
        expected_list = [TextNode("This is italic at the ", TextType.TEXT), TextNode("end", TextType.ITALIC)]
        self.assertEqual(test_delimiter, expected_list)

    def test_mixed_nodes(self):
        test_node = TextNode("This is text with a `code block` word and a **bold block** word", TextType.TEXT)
        test_delimiter = split_nodes_delimiter(split_nodes_delimiter([test_node], "**", TextType.BOLD), "`", TextType.CODE)
        expected_list = [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE), 
                         TextNode(" word and a ", TextType.TEXT), TextNode("bold block", TextType.BOLD), TextNode(" word", TextType.TEXT)]
        self.assertEqual(test_delimiter, expected_list)


if __name__ == "__main__":
    unittest.main()