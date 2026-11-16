"""EXP22: Reference Resolution
DSA03 - Natural Language Processing Lab
"""
text = "Ravi bought a laptop. He uses it every day."
sentences = text.split(". ")
antecedents = {"He": "Ravi", "it": "a laptop"}
print("Text:", text)
for pronoun, referent in antecedents.items():
    print(f"{pronoun} -> {referent}")
print("Resolved text: Ravi bought a laptop. Ravi uses the laptop every day.")
