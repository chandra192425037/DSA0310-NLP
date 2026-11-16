"""EXP13: Parse Tree Generation
DSA03 - Natural Language Processing Lab
"""
# Parse tree for: the boy sees a dog
tree = ("S", [
    ("NP", [("Det", ["the"]), ("N", ["boy"])]),
    ("VP", [("V", ["sees"]), ("NP", [("Det", ["a"]), ("N", ["dog"])])])
])
def show(node, level=0):
    label, children = node
    print("  " * level + label)
    for child in children:
        if isinstance(child, tuple):
            show(child, level + 1)
        else:
            print("  " * (level + 1) + child)
print("Parse tree:")
show(tree)
