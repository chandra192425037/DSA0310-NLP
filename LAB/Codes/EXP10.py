"""EXP10: Transformation-based Tagging
DSA03 - Natural Language Processing Lab
"""
sentence = [("The", "NN"), ("dogs", "NN"), ("bark", "NN"), ("loudly", "NN")]
print("Initial tags:", sentence)
# Transformation rules correct common errors.
transformed = []
for word, tag in sentence:
    if word.lower() == "the":
        tag = "DT"
    elif word.endswith("s") and word.lower() != "loudly":
        tag = "NNS"
    elif word.lower() in {"bark", "run", "walk"}:
        tag = "VB"
    elif word.endswith("ly"):
        tag = "RB"
    transformed.append((word, tag))
print("After transformation rules:")
for word, tag in transformed:
    print(f"{word:10} {tag}")
