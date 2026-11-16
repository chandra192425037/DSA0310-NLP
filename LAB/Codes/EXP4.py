"""EXP4: Finite State Morphology - plural nouns
DSA03 - Natural Language Processing Lab
"""
def plural(noun):
    if noun.endswith(("s", "x", "z", "ch", "sh")):
        return noun + "es"
    if noun.endswith("y") and len(noun) > 1 and noun[-2] not in "aeiou":
        return noun[:-1] + "ies"
    return noun + "s"

for noun in ["cat", "box", "city", "dish", "book"]:
    print(f"{noun:10} -> {plural(noun)}")
