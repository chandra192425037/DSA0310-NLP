"""EXP18: FOPC Parser
DSA03 - Natural Language Processing Lab
"""
import re
expression = "FORALL x (Human(x) -> Mortal(x))"
tokens = re.findall(r"[A-Za-z]+|->|[(),]", expression)
print("Expression:", expression)
print("Tokens:", tokens)
# Validate a simple quantified implication form.
valid = bool(re.fullmatch(
    r"FORALL\s+[a-z]\s+\([A-Za-z]+\([a-z]\)\s*->\s*[A-Za-z]+\([a-z]\)\)",
    expression))
print("FOPC syntax:", "VALID" if valid else "INVALID")
print("Meaning: For every x, if x is human then x is mortal.")
