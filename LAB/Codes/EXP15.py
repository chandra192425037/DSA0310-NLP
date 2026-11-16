"""EXP15: Probabilistic CFG Parsing
DSA03 - Natural Language Processing Lab
"""
# Small PCFG with rule probabilities; scores a known parse.
rules = {
    "S": [(("NP", "VP"), 1.0)],
    "NP": [(("Det", "N"), 0.7), (("Name",), 0.3)],
    "VP": [(("V", "NP"), 0.8), (("V",), 0.2)],
    "Det": [(("the",), 1.0)], "N": [(("dog",), 1.0)],
    "V": [(("sees",), 1.0)]
}
parse_probability = 1.0
chosen_rules = [("S", ("NP", "VP")), ("NP", ("Det", "N")), ("VP", ("V", "NP"))]
for lhs, rhs in chosen_rules:
    probability = next(p for r, p in rules[lhs] if r == rhs)
    parse_probability *= probability
print("Sentence: the dog sees the dog")
print("Selected grammar rules:")
for lhs, rhs in chosen_rules:
    print(f"  {lhs} -> {' '.join(rhs)}")
print(f"Parse probability = {parse_probability:.4f}")
