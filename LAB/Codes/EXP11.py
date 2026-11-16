"""EXP11: Top-down CFG Parser
DSA03 - Natural Language Processing Lab
"""
grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"]],
    "N": [["cat"], ["mouse"]],
    "V": [["chased"]]
}
tokens = "the cat chased the mouse".split()

def parse(symbol, position):
    results = []
    for production in grammar.get(symbol, []):
        states = [(position, [])]
        for item in production:
            new_states = []
            for pos, children in states:
                if item in grammar:
                    for end, tree in parse(item, pos):
                        new_states.append((end, children + [tree]))
                elif pos < len(tokens) and tokens[pos] == item:
                    new_states.append((pos + 1, [item] + children))
            states = new_states
        results.extend((pos, (symbol, children)) for pos, children in states)
    return results

trees = parse("S", 0)
print("Sentence:", " ".join(tokens))
print("Accepted:", any(end == len(tokens) for end, _ in trees))
print("Parse tree:", trees[0][1] if trees else "No parse")
