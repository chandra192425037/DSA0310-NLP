"""EXP9: Rule-based POS Tagging using Regular Expressions
DSA03 - Natural Language Processing Lab
"""
import re
patterns = [
    (r".*ing$", "VBG"), (r".*ed$", "VBD"),
    (r".*ly$", "RB"), (r".*ous$", "JJ"),
    (r".*s$", "NNS"), (r".*", "NN")
]
sentence = "Students are happily reading interesting books".split()
print("Rule-based POS tagging:")
for word in sentence:
    tag = next(tag for pattern, tag in patterns if re.fullmatch(pattern, word.lower()))
    if word.lower() == "are": tag = "VBP"
    print(f"{word:15} {tag}")
