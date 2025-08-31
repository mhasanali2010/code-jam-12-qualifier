from qualifier import query_selector_all

from node import Node


node = Node(
            tag="div",
            attributes={"id": "topDiv"},
            children=[
                Node(
                    tag="div",
                    attributes={"id": "innerDiv", "class": "container colour-primary"},
                    children=[
                        Node(tag="h1", text="This is a heading!"),
                        Node(
                            tag="p",
                            attributes={"class": "colour-secondary", "id": "innerContent"},
                            text="I have some content within this container also!",
                        ),
                        Node(
                            tag="p",
                            attributes={"class": "colour-secondary", "id": "two"},
                            text="This is another paragraph.",
                        ),
                        Node(
                            tag="p",
                            attributes={"class": "colour-secondary important"},
                            text="This is a third paragraph.",
                        ),
                        Node(
                            tag="a",
                            attributes={"id": "home-link", "class": "colour-primary button"},
                            text="This is a button link.",
                        ),
                    ],
                ),
                Node(
                    tag="div",
                    attributes={"class": "container colour-secondary"},
                    children=[
                        Node(
                            tag="p",
                            attributes={"class": "colour-primary"},
                            text="This is a paragraph in a secondary container.",
                        ),
                    ],
                ),
            ],
        )


selector = '#home-link'
matched_nodes = query_selector_all(node, selector)

for each in matched_nodes:
    print(each)