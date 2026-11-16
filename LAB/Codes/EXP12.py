"""EXP12: Earley Parser for CFG
DSA03 - Natural Language Processing Lab
"""
# Compact Earley recognizer for S -> NP VP; NP -> Det N; VP -> V NP
grammar = {"S": [["NP", "VP"]], "NP": [["Det", "N"]],
           "VP": [["V", "NP"]], "Det": [["the"]],
           "N": [["cat"], ["mouse"]], "V": [["chased"]]}
tokens = "the cat chased the mouse".split()
chart = [set() for _ in range(len(tokens) + 1)]
chart[0].add(("S", tuple(["NP", "VP"]), 0, 0))

for i in range(len(chart)):
    changed = True
    while changed:
        changed = False
        for lhs, rhs, dot, origin in list(chart[i]):
            if dot < len(rhs):
                nxt = rhs[dot]
                if nxt in grammar:
                    for prod in grammar[nxt]:
                        item = (nxt, tuple(prod), 0, i)
                        if item not in chart[i]:
                            chart[i].add(item); changed = True
                elif i < len(tokens) and tokens[i] == nxt:
                    chart[i + 1].add((lhs, rhs, dot + 1, origin))
            else:
                for plhs, prhs, pdot, porigin in list(chart[origin]):
                    if pdot < len(prhs) and prhs[pdot] == lhs:
                        item = (plhs, prhs, pdot + 1, porigin)
                        if item not in chart[i]:
                            chart[i].add(item); changed = True
print("Sentence:", " ".join(tokens))
accepted = ("S", ("NP", "VP"), 2, 0) in chart[len(tokens)]
print("Earley parser result:", "ACCEPTED" if accepted else "REJECTED")
for i, states in enumerate(chart):
    print(f"Chart[{i}] states:", len(states))
