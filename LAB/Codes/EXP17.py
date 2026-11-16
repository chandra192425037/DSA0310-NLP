"""EXP17: WordNet Synsets
DSA03 - Natural Language Processing Lab
"""
word = "bank"
try:
    from nltk.corpus import wordnet as wn
    synsets = wn.synsets(word)
    print("WordNet synsets for:", word)
    for syn in synsets[:5]:
        print(syn.name(), "-", syn.definition())
except Exception:
    print("WordNet-style meaning exploration for:", word)
    meanings = [
        ("bank.n.01", "financial institution that accepts deposits"),
        ("bank.n.02", "sloping land beside a body of water"),
        ("bank.v.01", "to deposit money in a bank")
    ]
    for name, definition in meanings:
        print(name, "-", definition)
