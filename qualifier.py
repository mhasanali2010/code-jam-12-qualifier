from __future__ import annotations

from node import Node

def query_selector_all(node: Node, selector: str) -> list[Node]:
    has_class = "class" in node.attributes
    has_id = "id" in node.attributes
    final_list = []
    selectors = selector.split(',')
    for sel in selectors:
        sel = sel.strip()
        if sel[0] == "#" and '.' not in sel and has_id: #single id
            if has_id and sel[1:] == node.attributes["id"]:
                final_list.append(node)
        elif sel[0] == "." and '#' not in sel and has_class: #single and multi classes
            if has_class:
                classes = set(node.attributes["class"].split(" "))
                sel = set(sel.split('.')[1:])
                if sel.issubset(classes):
                    final_list.append(node)
        elif '#' in sel and sel[0] != '#' and '.' not in sel and has_id: # tag#id
            if sel.split('#')[0] == node.tag and (sel.split('#')[1] == node.attributes["id"]):
                final_list.append(node)
        elif '.' in sel and sel[0] != '.' and '#' not in sel and has_class: # tag.class.class2.classN
            tag = sel.split('.')[0]
            sel_classes = set(sel.split('.')[1:])
            node_classes = set(node.attributes["class"].split(" "))
            if tag == node.tag and sel_classes.issubset(node_classes):
                final_list.append(node)
        elif '#' in sel and '.' in sel and sel[0] != '#' and sel[0] != '.' and has_class and has_id: # tag.class.class2.classN#id or tag#id.class.class2.classN
            tokens = sel.replace('#', '.#').split('.')
            sel_classes = []
            for token in tokens:
                if '#' in token:
                    sel_id = token.split('#')[1]
                elif token != tokens[0]:
                    sel_classes.append(token)
                else:
                    sel_tag = tokens[0]
            if sel_tag == node.tag and sel_id == node.attributes["id"] and set(sel_classes).issubset(set(node.attributes["class"].split(' '))):
                final_list.append(node)
        elif '#' in sel and '.' in sel and has_id and has_class and (sel[0] == '.' or sel[0] == '#'): # .class1.class2#id or #id.class1.class2
            sel_classes = []
            sel_id = None
            tokens = sel.replace('#', '.#').split('.')
            for token in tokens:
                token = token.strip()
                if not token:
                    continue
                if '#' in token:
                    sel_id = token.split('#')[1]
                else:
                    sel_classes.append(token)
            node_classes = set(node.attributes["class"].split())
            if sel_id == node.attributes["id"] and set(sel_classes).issubset(node_classes):
                final_list.append(node)
        else: #single tag
            if sel == node.tag:
                final_list.append(node)

    for child in node.children: #searching node's children
        final_list = final_list + query_selector_all(child, selector)


    final_list = list(set(final_list))
    return final_list
