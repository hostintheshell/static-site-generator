import unittest

from htmlnode import *

class TestHTMLNode(unittest.TestCase):
# HTMLNode Test Cases ------------------------

    def test_props_to_html_empty(self):
        node = HTMLNode(props={})
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_one_prop(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com"')

    def test_props_to_html_multiple_props(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertTrue(node.props_to_html() == ' href="https://www.google.com" target="_blank"' or
                        node.props_to_html() == ' target="_blank" href="https://www.google.com"')


# LeafNode Test Cases ------------------------

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "This is bold text.")
        self.assertEqual(node.to_html(), "<b>This is bold text.</b>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "This is a link.", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">This is a link.</a>')


# ParentNode Test Cases ----------------------

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")

    def test_to_html_with_nested_parents(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        parent_node2 = ParentNode("div", [parent_node])
        self.assertEqual(parent_node2.to_html(), "<div><div><span>child</span></div></div>")

    def test_to_html_with_multiple_children(self):
        child_node = LeafNode("span", "child")
        child_node2 = LeafNode("b", "child2")
        parent_node = ParentNode("div", [child_node, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><b>child2</b></div>")

    def test_to_html_with_parent_leaf_children(self):
        child_node = LeafNode("span", "child")
        child_node2 = LeafNode("b", "child2")
        parent_node = ParentNode("div", [child_node2])
        parent_node2 = ParentNode("div", [parent_node, child_node])
        self.assertEqual(parent_node2.to_html(), "<div><div><b>child2</b></div><span>child</span></div>")


if __name__ == "__main__":
    unittest.main()