"""EXP21: Syntax-driven Semantic Analysis
DSA03 - Natural Language Processing Lab
"""
import re
sentence = "The smart student reads a book"
tokens = sentence.split()
noun_phrases = re.findall(r"\b(?:The|A|An|the|a|an)\s+(?:\w+\s+)?\w+\b", sentence)
print("Sentence:", sentence)
print("Noun phrases:")
for phrase in noun_phrases:
    words = phrase.split()
    head = words[-1]
    modifier = " ".join(words[1:-1]) or "none"
    print(f"  {phrase!r}: head={head!r}, modifier={modifier!r}")
print("Semantic interpretation: a student performs the action of reading a book.")
