from textnode import TextType, TextNode

def main():
	text = "this is some anchor text"
	text_type = TextType.LINK
	url = "https://www.boot.dev"
	test = TextNode(text, text_type, url)
	print(test)

if __name__ == "__main__":
	main()