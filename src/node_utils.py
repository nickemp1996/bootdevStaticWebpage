from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType

def text_node_to_html_node(text_node):
	if not isinstance(text_node.text_type, TextType):
		raise Exception("text node text type is not a member of TextType")
	print(text_node.text_type)
	if text_node.text_type == TextType.TEXT:
		leaf_node = LeafNode(None, text_node.text)
		return leaf_node
	if text_node.text_type == TextType.BOLD:
		leaf_node = LeafNode("b", text_node.text)
		return leaf_node
	if text_node.text_type == TextType.ITALIC:
		leaf_node = LeafNode("i", text_node.text)
		return leaf_node
	if text_node.text_type == TextType.CODE:
		leaf_node = LeafNode("code", text_node.text)
		return leaf_node
	if text_node.text_type == TextType.LINK:
		leaf_node = LeafNode("a", text_node.text, {"href": text_node.url})
		return leaf_node
	if text_node.text_type == TextType.IMAGE:
		leaf_node = LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
		return leaf_node